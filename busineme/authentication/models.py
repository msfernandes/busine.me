from defaults.models import BusinemeModel
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class RankPosition(BusinemeModel):
    description = models.CharField(max_length=100)
    min_points = models.IntegerField()

    def __str__(self):
        return "{} - {}".format(self.id, self.description)


class BusinemeUser(BusinemeModel, AbstractUser):
    pontuation = models.IntegerField(default=0)
    rank = models.ForeignKey(RankPosition, null=True)
    deactivation_reason = models.CharField(max_length=255, null=True)
    objects = UserManager()

    def save(self, *args, **kwargs):
        self.username = self.username.lower()
        super(BusinemeUser, self).save(*args, **kwargs)

    def __str__(self):
        return "{} - {} {}".format(self.id, self.username, self.email)
