from django.views.generic import View
from django.shortcuts import render_to_response


class LoginView(View):

    def get(self, request):
        return render_to_response('login.html')
