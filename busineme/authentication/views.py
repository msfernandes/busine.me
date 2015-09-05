from django.views.generic import View
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


class LoginView(View):
    http_method_names = [u'get', u'post']

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


class ForgotPasswordView(View):
    http_method_names = [u'get', u'post']

    def get(self, request):
        render_to_response('login.html')

    def post(self, request):
        render_to_response('login.html')


class RegisterUserView(View):
    http_method_names = [u'get', u'post']

    def get(self, request):
        render_to_response('login.html')

    def post(self, request):
        render_to_response('login.html')
