from django.test import TestCase
from ..models import BusinemeModel


class TestModels(TestCase):

    def setUp(self):
        self.model = BusinemeModel()

    def test_save(self):
        self.assertRaises(NotImplementedError, self.model.save)

    def test_delete(self):
        self.assertRaises(NotImplementedError, self.model.delete)

    def test_get(self):
        self.assertRaises(NotImplementedError, self.model.get)

    def test_all(self):
        self.assertRaises(NotImplementedError, self.model.all)

    def test_filter(self):
        self.assertRaises(NotImplementedError, self.model.filter)

    def test_filter_startswith(self):
        self.assertRaises(NotImplementedError, self.model.filter_startswith)
