from defaults.models import BusinemeModel
from django.db import models


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
    def api_filter_startswith(cls, line_number):
        r"""
        If API is up, send requisition and returns buslines with the \
        specified line number. If API is down, searches local database to\
        return buslines with the specified line number.
        """
        objects = cls.objects.filter(line_number__startswith=line_number)
        return objects


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
