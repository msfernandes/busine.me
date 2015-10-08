from django.test import TestCase, Client, RequestFactory

from authentication.models import BusinemeUser
from ..models import Busline, Favorite, Terminal
from ..views import FavoriteBuslineView


class TestBuslineSearchView(TestCase):

    def setUp(self):
        self.client = Client()
        self.busline = Busline()
        self.busline.line_number = '001'
        self.busline.description = 'route'
        self.busline.route_size = 0.1
        self.busline.fee = 3.50
        self.terminal = Terminal(description="terminal")
        self.terminal.save()
        self.busline.save()
        self.busline.terminals.add(self.terminal)

    def test_get(self):
        response = self.client.get("/search/busline/?busline=001")
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='search_result.html')


class TestFavoriteBuslineView(TestCase):

    def setUp(self):
        self.client = Client()
        self.request = RequestFactory()
        self.busline = Busline()
        self.user = BusinemeUser()
        self.favorite = Favorite()
        self.busline.line_number = '001'
        self.busline.description = 'route'
        self.busline.route_size = 0.1
        self.busline.fee = 3.50
        self.busline.save()
        self.user = BusinemeUser.objects.create_user(username='johndoe',
                                                     password='secret')

    def test_favorite_line(self):
        self.client.login(username='johndoe', password='secret')

        favorite_count = len(Favorite.objects.all())

        self.assertGreaterEqual(favorite_count, 0)

        for favorite in Favorite.objects.all():
            favorite.delete()

        favorite_count = len(Favorite.objects.all())

        self.assertEquals(favorite_count, 0)

        request = self.request.get("/favorite/busline/?line_number=001")
        request.META['HTTP_REFERER'] = "/search/busline/?busline=001"
        request.user = self.user

        response = FavoriteBuslineView.as_view()(request)
        # Since it redirects at the end, it should return 302 statuc code
        self.assertEquals(response.status_code, 302)

        favorite_count = len(Favorite.objects.all())

        self.assertEquals(favorite_count, 1)

    def test_unfavorite_line(self):
        self.client.login(username='johndoe', password='secret')

        favorite_count = len(Favorite.objects.all())

        self.assertGreaterEqual(favorite_count, 0)

        for favorite in Favorite.objects.all():
            favorite.delete()

        favorite_count = len(Favorite.objects.all())

        self.assertEquals(favorite_count, 0)

        self.favorite.busline = self.busline
        self.favorite.user = self.user
        self.favorite.save()

        request = self.request.get("/favorite/busline/?line_number=001")
        request.META['HTTP_REFERER'] = "/search/busline/?busline=001"
        request.user = self.user

        response = FavoriteBuslineView.as_view()(request)
        # Since it redirects at the end, it should return 302 statuc code
        self.assertEquals(response.status_code, 302)

        favorite_count = len(Favorite.objects.all())

        self.assertEquals(favorite_count, 0)
