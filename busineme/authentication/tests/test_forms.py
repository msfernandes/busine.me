from django.test import TestCase
from django.contrib.auth.hashers import check_password
from ..forms import BusinemeUserForm, UpdateUserForm, UpdatePasswordForm
from ..models import BusinemeUser
from mock import Mock


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


class TestUpdateUserForm(TestCase):

    def setUp(self):
        self.data = {'first_name': 'first_name',
                     'email': 'email@test.com'}

        user = BusinemeUser()
        user.id = 1
        user.first_name = 'name'
        user.username = 'username'
        user.email = 'email@email.com'
        user.set_password('1234')
        self.user = user
        self.user.save()

    def test_is_valid(self):
        request = Mock(POST=self.data)
        form = UpdateUserForm(request)
        self.assertTrue(form.is_valid())

    def test_is_invalid(self):
        self.data['email'] = 'invalid_email'
        request = Mock(POST=self.data)
        form = UpdateUserForm(request)
        self.assertFalse(form.is_valid())

    def test_save(self):
        request = Mock(POST=self.data, user=self.user)
        form = UpdateUserForm(request)
        form.is_valid()
        form.save()

        user = BusinemeUser.objects.get(pk=1)
        self.assertEquals('first_name', user.first_name)
        self.assertEquals('email@test.com', user.email)


class TestUpdatePasswordForm(TestCase):

    def setUp(self):
        self.data = {'password': '1234',
                     'confirm_password': '1234'}

        user = BusinemeUser()
        user.id = 1
        user.first_name = 'name'
        user.username = 'username'
        user.email = 'email@email.com'
        user.set_password('1234')
        self.user = user
        self.user.save()

    def test_is_valid(self):
        request = Mock(POST=self.data)
        form = UpdatePasswordForm(request)
        self.assertTrue(form.is_valid())

    def test_is_invalid(self):
        self.data['confirm_password'] = '4321'
        request = Mock(POST=self.data)
        form = UpdatePasswordForm(request)
        self.assertFalse(form.is_valid())

    def test_save(self):
        request = Mock(POST=self.data, user=self.user)
        form = UpdatePasswordForm(request)
        form.is_valid()
        form.save()

        user = BusinemeUser.objects.get(pk=1)
        self.assertTrue(check_password(self.data['password'], user.password))
