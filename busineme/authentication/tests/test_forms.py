from django.test import TestCase
from ..forms import BusinemeUserForm


class TestBusinemeUserForm(TestCase):

    def setUp(self):
        self.data = {'username': 'username',
                     'first_name': 'first_name',
                     'email': 'email@test.com',
                     'password': 'password', }

    def test_valid_form(self):
        form = BusinemeUserForm(data=self.data)
        self.assertTrue(form.is_valid())

    def test_invalid_email(self):
        self.data['email'] = 'email'
        form = BusinemeUserForm(data=self.data)
        self.assertFalse(form.is_valid())

    def test_invalid_username(self):
        self.data['username'] = '(*&$#@!'
        form = BusinemeUserForm(data=self.data)
        self.assertFalse(form.is_valid())
