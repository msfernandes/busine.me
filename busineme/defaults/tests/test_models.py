from django.test import TestCase
from ..models import BusinemeModel


class TestModels(TestCase):

    def setUp(self):
        self.model = BusinemeModel()

    def test_api_save(self):
        self.assertRaises(NotImplementedError, self.model.api_save)

    def test_api_delete(self):
        self.assertRaises(NotImplementedError, self.model.api_delete)

    def test_api_get(self):
        self.assertRaises(NotImplementedError, self.model.api_get)

    def test_api_all(self):
        self.assertRaises(NotImplementedError, self.model.api_all)

    def test_api_filter(self):
        self.assertRaises(NotImplementedError, self.model.api_filter)

    def test_api_filter_startswith(self):
        self.assertRaises(NotImplementedError,
                          self.model.api_filter_startswith)
