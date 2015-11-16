import requests
from urllib.request import urljoin
from django.conf import settings
from .models import Busline, Terminal, Company


class TemplateAPI(object):

    def __init__(self):
        self.url = self.url()

    # Template Method
    def all(self):
        data = requests.get(self.url)
        return self.get_list(data.json())

    # Template Method
    def filter(self, **kwargs):
        """
        Send requisition to get buslines depending on the arguments. \
        This will be handled by the API, so only certain arguments names and \
        values can be handled.
        """
        url = self.url + '?' 
        for arg, value in kwargs.items():
            url += arg + '=' + value + '&'
        data = requests.get(url)
        return self.get_list(data.json())

    def url(self):
        raise NotImplementedError()

    def api_model(self):
        raise NotImplementedError()

    def get_list(self, data):
        data_list = []
        for json_obj in data['objects']:
            data_list.append(self.json_to_object(json_obj, self.api_model()))
        return data_list

    def json_to_object(self, json_obj, clz):
        obj = clz()
        if json_obj is not None:
            for attribute in json_obj.keys():
                if attribute in obj.__dict__.keys():
                    setattr(obj, attribute, json_obj[attribute])
        return obj


class BuslineAPI(TemplateAPI):



    def url(self):
        return urljoin(settings.API_URL, 'buslines')

    def api_model(self):
        return Busline

    def json_to_object(self, json_obj, clz):
        obj = clz()
        for attribute in json_obj.keys():
            if attribute in obj.__dict__.keys():
                if attribute == 'company':
                    print(attribute)
                    print(json_obj[attribute])
                    print(super().json_to_object(json_obj[attribute], Company))
                    setattr(obj, attribute,
                            super().json_to_object(json_obj[attribute],
                                                   Company))
                if attribute == 'terminals':
                    setattr(obj, attribute,
                            self.get_terminals_list(json_obj[attribute]))
                else:
                    setattr(obj, attribute, json_obj[attribute])
        return obj

    def get_terminals_list(self, json_data):
        terminals_list = []
        for terminal in json_data:
            terminals_list.append(super().json_to_object(terminal, Terminal))

        return terminals_list


class CompanyAPI(TemplateAPI):

    def url(self):
        return urljoin(settings.API_URL, 'company')

    def api_model(self):
        return Company


class TerminalAPI(TemplateAPI):

    def url(self):
        return urljoin(settings.API_URL, 'terminal')

    def api_model(self):
        return Terminal


class BusinemeAPI(object):

    def __init__(self):
        self.buslines = BuslineAPI()
        self.companies = CompanyAPI()
        self.terminals = TerminalAPI()
