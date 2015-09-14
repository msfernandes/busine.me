from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import (LoginView, ForgotPasswordView, UpdatePasswordView,
                    RegisterUserView, UserProfileView, DeactivateUserView,
                    LogoutView)

urlpatterns = [
    url(r'^login/$', LoginView.as_view(),
        name='login'),

    url(r'^logout/$', login_required(LogoutView.as_view()),
        name='logout'),

    url(r'^password/reset/$', ForgotPasswordView.as_view(),
        name='forgot_password'),

    url(r'^password/update/$', login_required(UpdatePasswordView.as_view()),
        name='update_password'),

    url(r'^register/$', RegisterUserView.as_view(),
        name='register_user'),

    url(r'^profile/$', login_required(UserProfileView.as_view()),
        name='user_profile'),

    url(r'^deactivate/$', login_required(DeactivateUserView.as_view()),
        name='deactivate_user'),
]
