from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View

from .models import Busline, Favorite


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

        context = {}

        if request.user.is_authenticated():
            user = request.user
            user_favorites = Favorite.objects.filter(user=user)
            user_favorites = [favorite.busline for favorite in user_favorites]
            context = {'user_favorites': user_favorites}

        response = render_to_response("search_result.html", locals(),
                                      context_instance=RequestContext(request,
                                                                      context))
        return response
