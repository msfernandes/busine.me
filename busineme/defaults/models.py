from django.db import models
from abc import abstractmethod


class BusinemeModel(models.Model):
    class Meta:
        abstract = True

    @abstractmethod
    def api_save(self):
        raise NotImplementedError()

    @abstractmethod
    def api_delete(self):
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def api_get(cls, **kwargs):
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def api_all(cls):
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def api_filter(cls, **kwargs):
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def api_filter_startswith(cls, **kwargs):
        raise NotImplementedError()
