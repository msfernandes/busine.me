from django.views.generic import View
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


class LoginView(View):

    def get(self, request):
        return render_to_response('login.html',
                                  context=RequestContext(request))

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        response = render_to_response('login.html',
                                      context=RequestContext(request))
        if user:
            if user.is_active:
                login(user)
                response = redirect('/')
            else:
                messages.add_message(request, messages.ERROR,
                                     "Inactive user.")
        else:
            messages.add_message(request, messages.ERROR, "Invalid user")

        return response
