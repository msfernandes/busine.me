from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View
from .models import BusinemeBusline


class BuslineSearchView(View):
    http_method_names = [u'get', u'post']

    def get(self, request):
        """
        Perform a search for bus lines that contain the input value entered\
        by the user then returns the result page and the list of results.
        """
        line_number = request.GET['busline']
        buslines = BusinemeBusline.api_filter_startswith(line_number)
        count_busline = len(buslines)
        response = render_to_response("search_result.html",
                                      {'buslines': buslines,
                                       'count_busline': count_busline,
                                       'searched_number': line_number},
                                      context_instance=RequestContext(request))
        return response
