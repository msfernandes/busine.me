#! -*- coding: utf-8 -*-

""" View that deals with Busine.me's homepage methods
"""
from django.views.generic import View
from django.shortcuts import render_to_response


class HomeView(View):
    """ Representation of Busine.me's homepage
    """

    def get(self, request):
        """ GET request for homepage
        It displays the homepage as it is
        """
        return render_to_response('home.html')
