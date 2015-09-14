# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from importer.parser import Parser


class Command(BaseCommand):

    def handle(self, *args, **options):
        parser = Parser()
        parser.import_data()
