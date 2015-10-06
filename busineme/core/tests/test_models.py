from django.test import TestCase
from ..models import Busline
from ..models import Terminal


class TestBusline(TestCase):

    def setUp(self):
        self.busline = Busline()

        self.busline.line_number = '001'
        self.busline.description = 'route'
        self.busline.route_size = 0.1
        self.busline.fee = 3.50
        self.terminal = Terminal(description="terminal")
        self.terminal.save()
        self.busline.save()
        self.busline.terminals.add(self.terminal)

    def test_str(self):
        self.assertEquals(
            "001 - route", self.busline.__str__())

    def test_filter_by_line_number(self):
        bus = self.busline.api_filter_contains('001')
        self.assertEquals(bus[0], self.busline)
