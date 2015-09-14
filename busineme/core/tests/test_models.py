from django.test import TestCase
from ..models import BusinemeBusline
from ..models import BusinemeTerminal


class TestBusinemeBusline(TestCase):

    def setUp(self):
        self.busline = BusinemeBusline()

        self.busline.line_number = '001'
        self.busline.description = 'route'
        self.busline.route_size = 0.1
        self.busline.fee = 3.50
        self.terminal = BusinemeTerminal(description="terminal")
        self.terminal.save()
        self.busline.save()
        self.busline.terminals.add(self.terminal)

    def test_str(self):
        self.assertEquals(
            "001 - route", self.busline.__str__())

    def test_filter_by_line_number(self):
        bus = self.busline.api_filter_startswith('001')
        self.assertEquals(bus[0], self.busline)
