from django.test import TestCase, Client
from ..models import BusinemeBusline
from ..models import BusinemeTerminal


class TestBusinemeBuslineSearchView(TestCase):

    def setUp(self):
        self.client = Client()
        self.busline = BusinemeBusline()
        self.busline.line_number = '001'
        self.busline.description = 'route'
        self.busline.route_size = 0.1
        self.busline.fee = 3.50
        self.terminal = BusinemeTerminal(description="terminal")
        self.terminal.save()
        self.busline.save()
        self.busline.terminals.add(self.terminal)

    def test_get(self):
        response = self.client.get("/search/busline/?busline=001")
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='search_result.html')
