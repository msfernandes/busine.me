from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.generic import View
from django.utils.translation import ugettext as _
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

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('login'))
            else:
                messages.error(request, _("Inactive user."))
        else:
            messages.error(request, _("Invalid username/password."))

        response = render_to_response('login.html',
                                      context=RequestContext(request))
        return response


class ForgotPasswordView(View):
    http_method_names = [u'get', u'post']

    def get(self, request):
        return render_to_response('login.html')

    def post(self, request):
        return render_to_response('login.html')


class UserProfileView(View):
    http_method_names = [u'get', u'post']

    def get(self, request):
        return render_to_response('profile.html',
                                  context=RequestContext(request))

class RegisterUserView(View):
    http_method_names = [u'get', u'post']

    def get(self, request):
        return render_to_response('register.html',
                                  context=RequestContext(request))

    def post(self, request):
        form = BusinemeUserForm(request.POST)
        if form.is_valid():
            form.save()
            response = redirect(reverse('login'))
            username = form.cleaned_data['username']
            messages.success(
                request,
                _("User {} successfully created!".format(username)))
        else:
            self.add_message_errors(form, request)
            response = redirect(reverse('register_user'))
        return response

    def add_message_errors(self, form, request):
        for error in form.errors:
            error_msg = form.errors.get(error).as_text()
            error_msg = error_msg[2:]
            messages.error(request, _(error_msg))
