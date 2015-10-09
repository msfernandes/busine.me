from django.db import models

from authentication.models import BusinemeUser
from defaults.models import BusinemeModel


class Busline(BusinemeModel):

    """Busline Model."""

    line_number = models.CharField(max_length=5, unique=True)
    description = models.CharField(max_length=255)
    via = models.CharField(max_length=255)
    route_size = models.FloatField()  # unit: kilometers
    fee = models.DecimalField(decimal_places=2, max_digits=4)  # unit: BRL (R$)
    company = models.ForeignKey('Company', null=True)
    terminals = models.ManyToManyField('Terminal')

    def __str__(self):
        return "{} - {}".format(self.line_number, self.description)

    @classmethod
    def api_filter_contains(cls, line_number):
        r"""
        If API is up, send requisition and returns buslines with the \
        specified line number. If API is down, searches local database to\
        return buslines with the specified line number.
        """
        objects = cls.objects.filter(line_number__contains=line_number)
        return objects

    @classmethod
    def api_get(cls, line_number):
        line_number = cls.adapt_line_number(line_number)
        busline = cls.objects.get(line_number=line_number)
        return busline

    @classmethod
    def adapt_line_number(cls, line_number):
        if line_number.find('.') == -1:
            line_number = '0.' + line_number
        return line_number


class Company(BusinemeModel):

    """Company Model."""

    name = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.name)


class Terminal(BusinemeModel):

    """Terminal Model."""

    description = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True)

    def __str__(self):
        return "{}".format(self.description)


class Favorite(BusinemeModel):

    """Favorite Model."""

    user = models.ForeignKey(BusinemeUser)
    busline = models.ForeignKey('Busline')

    def __str__(self):
        return "{} - {}".format(self.user.username, self.busline.line_number)


class Post(BusinemeModel):

    """Post Model."""

    comment = models.CharField(max_length=255)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    traffic = models.IntegerField()
    capacity = models.IntegerField()
    busline = models.ForeignKey(Busline)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    user = models.ForeignKey(BusinemeUser)

    def __str__(self):
        return 'id: %s date: %s %s busline_id: %s' % (self.id, str(self.date),
                                                      str(self.time),
                                                      self.busline_id)

    @classmethod
    def api_all(cls):
        objects = cls.objects.all()
        return objects

    @classmethod
    def api_filter_contains(cls, busline, limit=None):
        objects = Post.objects.filter(busline__id=busline.id).order_by(
            '-date', '-time')[:limit]
        return objects

    @classmethod
    def api_get(cls, post_id):
        post = cls.objects.get(id=post_id)
        return post
