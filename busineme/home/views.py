from django.views.generic import View
from django.shortcuts import render_to_response


class HomeView(View):

    def get(self, request):
        return render_to_response('home.html')
