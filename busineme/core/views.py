from django.shortcuts import render_to_response, redirect
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

        if request.user.is_authenticated():
            user = request.user
            user_favorites = Favorite.objects.filter(user=user)
            user_favorites = [favorite.busline for favorite in user_favorites]

        response = render_to_response("search_result.html", locals(),
                                      context_instance=RequestContext(request))
        return response


class FavoriteBuslineView(View):
    http_method_names = [u'get', u'post']

    def get(self, request):
        """
        (Un)Favorite selected busline.
        """
        line_number = request.GET['line_number']
        busline = Busline.objects.get(line_number=line_number)
        user = request.user

        print(user)
        print(busline)

        favorite = Favorite.objects.get_or_none(busline=busline, user=user)

        if favorite:
            favorite.delete()
        else:
            favorite = Favorite()
            favorite.user = user
            favorite.busline = busline
            favorite.save()

        # Go back to previous page, i.e., search result page
        return redirect(request.META.get('HTTP_REFERER'))
