# -*- coding: utf-8 -*-

import csv
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from core.models import Busline, Terminal, Company


class Parser(object):

    def import_data(self):
        self.import_companies()
        self.import_terminals()
        self.import_bus_lines()
        self.create_busline_terminal_relation()

    def read_file(self, file_name):
        csv_file = open(file_name)
        csv_file = csv.reader(csv_file, delimiter=',', quotechar="'")

        return csv_file

    def import_bus_lines(self):
        csv_file = self.read_file('importer/data/bus_lines.csv')

        print('Importing Buslines...')
        for row in csv_file:
            try:
                bus_line = Busline()
                bus_line.line_number = row[0]
                bus_line.description = row[1]
                bus_line.fee = row[2]
                bus_line.route_size = row[3]
                bus_line.company = Company.objects.get(name=row[4])
                bus_line.via = row[7]
                bus_line.save()
            except ObjectDoesNotExist:
                print('Busline', row[0], 'has incomplete data.')
            except IntegrityError:
                print('Busline', row[0], 'already registered.')

    def create_busline_terminal_relation(self):
        csv_file = self.read_file('importer/data/bus_lines.csv')

        print('Creating Busline-Terminal relation...')
        for row in csv_file:
            bus_line = Busline()
            try:
                bus_line = Busline.objects.get(line_number=row[0])
            except ObjectDoesNotExist:
                print('Busline', row[0], 'does not exist.')

            try:
                terminal1 = Terminal.objects.get(description=row[5])
                if terminal1 not in bus_line.terminals.all():
                    bus_line.terminals.add(terminal1)
                    bus_line.save()
            except ObjectDoesNotExist:
                print('Error for Busline ', row[0])
                print('Terminal', row[5], 'does not exist.')

            try:
                terminal2 = Terminal.objects.get(description=row[6])
                if terminal2 not in bus_line.terminals.all():
                    bus_line.terminals.add(terminal2)
                    bus_line.save()
            except ObjectDoesNotExist:
                print('Error for Busline ', row[0])
                print('Terminal', row[6], 'does not exist.')

    def import_terminals(self):
        csv_file = self.read_file('importer/data/terminals.csv')

        print('Importing Terminals...')

        for row in csv_file:
            self.import_terminal(row)

    def import_terminal(self, row):
        try:
            Terminal.objects.get(description=row[0])
            print('Terminal', row[0], 'already registered')
        except ObjectDoesNotExist:
            terminal = Terminal()
            terminal.description = row[0]
            terminal.save()

    def import_companies(self):
        csv_file = self.read_file('importer/data/companies.csv')

        print('Importing Companies...')
        for row in csv_file:
            try:
                Company.objects.get(name=row[0])
                print('Company', row[0], 'already registered.')
            except ObjectDoesNotExist:
                company = Company()
                company.name = row[0]
                company.save()
