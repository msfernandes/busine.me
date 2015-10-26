from defaults.models import BusinemeModel
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.dispatch import receiver
from django.conf import settings


class RankPosition(BusinemeModel):
    description = models.CharField(max_length=100)
    min_points = models.IntegerField()
    max_points = models.IntegerField()

    def __str__(self):
        return "{} - ({}) {}".format(self.id, self.min_points,
                                     self.description)


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


@receiver(models.signals.post_save, sender=settings.AUTH_USER_MODEL)
def calculate_position(sender, instance, **kwargs):
    rank = RankPosition.objects.get(min_points__lte=instance.pontuation,
                                    max_points__gt=instance.pontuation)
    sender.objects.filter(id=instance.id).update(rank=rank)
    instance.refresh_from_db()
