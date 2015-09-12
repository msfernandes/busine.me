from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from ..models import BusinemeBusline


class TestBuslineSearchView(TestCase):

    def setUp(self):
        self.client = Client()
        self.busline = BusinemeBusline()
        self.busline.line_number = '001'
        self.busline.description = 'route'
        self.terminal = BusinemeTerminal(description="terminal")
        self.terminal.save()
        self.busline.save
        self.busline.terminals.add(terminal)

    def test_get(self):
        response = self.client.get("/resrc/search/busline/?busline=001")
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='search_result.html')
