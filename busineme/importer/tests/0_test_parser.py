# -*- coding: utf-8 -*-

from configuration.tests import ParserTest
from importer.parser import Parser


class TestParser(ParserTest):

    """docstring for API_Views"""

    def test_parser(self):
        self.assertTrue(True)

    def test_parser_instance(self):
        parser = Parser()
        self.assertIsNotNone(parser)

    def test_parser_read_file(self):
        parser = Parser()
        print ''
        self.assertRaises(IOError, parser.read_file, '')
        self.assertRaises(IOError, parser.read_file, 'away')
        file = 'importer/data/bus_lines.csv'
        self.assertIsNotNone(parser.read_file(file))

    def test_parser_import_bus_lines(self):
        parser = Parser()
        print ''
        self.assertIsNone(parser.import_bus_lines())

    def test_parser_import_terminals_non_existing(self):
        parser = Parser()
        print ''
        self.assertIsNone(parser.import_terminals())

    def test_parser_import_terminal_existing(self):
        parser = Parser()
        parser.import_terminals()
        csv_file = parser.read_file('importer/data/terminals.csv')
        
        for row in csv_file:
            self.assertIsNone(parser.import_terminal(row))
            break
    
    def test_parser_import_data(self):
        parser = Parser()
        self.assertIsNone(parser.import_data())

    def test_parser_create_busline_terminal_relation(self):
        parser = Parser()
        self.assertIsNone(parser.create_busline_terminal_relation())

    def test_parser_import_companies(self):
        parser = Parser()
        self.assertIsNone(parser.import_companies())





