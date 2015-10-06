from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View
from .models import Busline


class BuslineSearchResultView(View):
    http_method_names = [u'get', u'post']

    def get(self, request):
        """
        Perform a search for bus lines that contain the input value entered\
        by the user then returns the result page and the list of results.
        """
        line_number = request.GET['busline']
        buslines = Busline.api_filter_contains(line_number)
        count_busline = len(buslines)
        response = render_to_response("search_result.html", locals(),
                                      context_instance=RequestContext(request))
        return response


class BuslineProfileView(View):
    http_method_names = [u'get']

    def get(self, request, line_number):
        busline = Busline.api_get(line_number)
        response = render_to_response("busline_profile.html", locals(),
                                      context_instance=RequestContext(request))
        return response
