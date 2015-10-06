from .models import Busline, Favorite
from authentication.models import BusinemeUser
from django.contrib import messages
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.views.generic import View


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
        user = BusinemeUser.objects.get(pk=request.user.id)

        favorite = Favorite.objects.get_or_none(busline=busline, user=user)

        if favorite:
            favorite.delete()
            messages.success(request, _('Deleted line from favorite lines'),
                             fail_silently=True)
        else:
            favorite = Favorite()
            favorite.user = user
            favorite.busline = busline
            favorite.save()
            messages.success(request, _('Added line to favorite lines'),
                             fail_silently=True)

        http_referer = request.META.get('HTTP_REFERER', None)

        if not http_referer:
            messages.warning(request, _("Can't find previous page,"
                                        " returning to home page"),
                             fail_silently=True)
            return redirect('/')
        # Go back to previous page, i.e., search result page
        return redirect(http_referer)


class BuslineProfileView(View):
    http_method_names = [u'get']

    def get(self, request, line_number):
        busline = Busline.api_get(line_number)
        response = render_to_response("busline_profile.html", locals(),
                                      context_instance=RequestContext(request))
        return response
