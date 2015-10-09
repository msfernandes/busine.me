#! -*- coding: utf-8 -*-

""" View that deals with Busine.me's homepage methods
"""
from django.views.generic import View
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from core.models import Favorite, Post


class IndexView(View):
    """ Representation of Busine.me's homepage
    """

    def get(self, request):
        """ GET request for homepage
        It displays the homepage as it is
        """
        if request.user.is_authenticated():
            response = redirect('home')
        else:
            response = render_to_response(
                'index.html',
                context_instance=RequestContext(request))
        return response


class HomeView(View):
    """ Representation of Busine.me's homepage
    """

    def get(self, request):
        favorites = Favorite.objects.filter(user=request.user)
        favorites = [favorite.busline for favorite in favorites]

        favorites_posts = []
        for busline in favorites:
            posts = Post.api_filter_contains(busline, limit=1)
            favorites_posts = favorites_posts + list(posts)

        return render_to_response('home.html', locals(),
                                  context_instance=RequestContext(request))
