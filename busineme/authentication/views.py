from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.generic import View
from .forms import BusinemeUserForm


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
                login(request, user)
                response = redirect('/')
            else:
                messages.error(request, "Inactive user.")
        else:
            messages.error(request, "Invalid user")

        return response


class ForgotPasswordView(View):
    http_method_names = [u'get', u'post']

    def get(self, request):
        return render_to_response('login.html')

    def post(self, request):
        return render_to_response('login.html')


class RegisterUserView(View):
    http_method_names = [u'get', u'post']

    def get(self, request):
        return render_to_response('register.html',
                                  context=RequestContext(request))

    def post(self, request):
        form = BusinemeUserForm(request.POST)
        form.save()
        return render_to_response('login.html')
