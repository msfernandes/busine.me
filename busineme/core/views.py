from django.contrib import messages
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.views.generic import View

from authentication.models import BusinemeUser
from .models import Busline, Favorite, Post


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
    http_method_names = [u'get']

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


class BuslinePostView(View):
    http_method_names = [u'get', u'post']

    def get(self, request):
        line_number = request.GET['line_number']
        busline = get_object_or_404(Busline, line_number=line_number)
        return render_to_response("post.html", locals(),
                                  context_instance=RequestContext(request))

    def post(self, request):
        post = Post()
        post.terminal = request.POST['terminal']
        post.traffic = request.POST['traffic']
        post.capacity = request.POST['capacity']
        post.comment = request.POST['comment']
        post.latitude = request.POST['latitude']
        post.longitude = request.POST['longitude']

        line_number = request.POST['line_number']
        post.busline = Busline.api_get(line_number)
        post.user = request.user
        post.save()

        return redirect('busline_profile', line_number=line_number)


class BuslineProfileView(View):
    http_method_names = [u'get']

    def get(self, request, line_number):
        if request.user.is_authenticated():
            user = request.user
            user_favorites = Favorite.objects.filter(user=user)
            user_favorites = [favorite.busline for favorite in user_favorites]
        busline = Busline.api_get(line_number)
        posts = Post.api_filter_contains(busline)
        response = render_to_response("busline_profile.html", locals(),
                                      context_instance=RequestContext(request))
        return response


class BuslinePostDetailView(View):
    http_method_names = [u'get']

    def get(self, request, post_id):
        post = Post.api_get(post_id)
        if request.user.is_authenticated():
            user = request.user
            user_favorites = Favorite.objects.filter(user=user)
            user_favorites = [favorite.busline for favorite in user_favorites]

        response = render_to_response("post_detail.html", locals(),
                                      context_instance=RequestContext(request))
        return response
