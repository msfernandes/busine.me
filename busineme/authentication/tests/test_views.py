from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from ..models import BusinemeUser


class TestLoginView(TestCase):

    def setUp(self):
        self.client = Client()

    def create_user(self, is_active=True):
        user = BusinemeUser()
        user.id = 1
        user.username = 'username'
        user.email = 'email@test.com'
        user.first_name = 'first'
        user.set_password('1234')
        user.is_active = is_active
        user.save()

    def test_put_method(self):
        response = self.client.put(reverse('login'))
        self.assertEquals(response.status_code, 405)

    def test_delete_methods(self):
        response = self.client.delete(reverse('login'))
        self.assertEquals(response.status_code, 405)

    def test_get(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='login.html')

    def test_post_valid_data(self):
        self.create_user()
        data = {'username': 'username', 'password': '1234',
                'next_url': '/auth/profile/'}
        self.client.post(reverse('login'), data=data)
        self.assertEqual(int(self.client.session['_auth_user_id']), 1)

    def test_post_invalid_password(self):
        self.create_user()
        data = {'username': 'username', 'password': 'invalid',
                'next_url': '/auth/profile/'}
        response = self.client.post(reverse('login'), data=data)
        self.assertEqual(200, response.status_code)

    def test_post_inactive_user(self):
        self.create_user(is_active=False)
        data = {'username': 'username', 'password': '1234',
                'next_url': '/auth/profile/'}
        response = self.client.post(reverse('login'), data=data)
        self.assertEqual(200, response.status_code)

    def test_next_url(self):
        data = {'username': 'username', 'password': '1234',
                'next_url': '/auth/profile/'}
        response = self.client.post(reverse('login'), data=data)
        self.assertEqual(200, response.status_code)


class TestForgotPasswordView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_put_method(self):
        response = self.client.put(reverse('forgot_password'))
        self.assertEquals(response.status_code, 405)

    def test_delete_methods(self):
        response = self.client.delete(reverse('forgot_password'))
        self.assertEquals(response.status_code, 405)


class TestRegisterUserView(TestCase):

    def setUp(self):
        self.client = Client()
        self.data = {'username': 'username',
                     'first_name': 'first_name',
                     'email': 'email@test.com',
                     'password': 'password', }

    def test_put_method(self):
        response = self.client.put(reverse('register_user'))
        self.assertEquals(response.status_code, 405)

    def test_delete_methods(self):
        response = self.client.delete(reverse('register_user'))
        self.assertEquals(response.status_code, 405)

    def test_get(self):
        response = self.client.get(reverse('register_user'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='register.html')

    def test_post_valid_data(self):
        before = len(BusinemeUser.objects.all())
        self.client.post(reverse('register_user'), data=self.data)
        after = len(BusinemeUser.objects.all())

        self.assertGreater(after, before)
