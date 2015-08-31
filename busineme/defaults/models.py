from django.db import models
from abc import abstractmethod


class BusinemeModel(models.Model):
    class Meta:
        abstract = True

    @abstractmethod
    def save(self, *args, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    def delete(self):
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def get(cls, **kwargs):
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def all(cls):
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def filter(cls, **kwargs):
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def filter_startswith(cls, **kwargs):
        raise NotImplementedError()
