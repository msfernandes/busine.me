from django.conf.urls import url
from .views import (LoginView, ForgotPasswordView,
                    RegisterUserView, UserProfileView)

urlpatterns = [
    url(r'^login/$', LoginView.as_view(),
        name='login'),

    url(r'^password/reset/$', ForgotPasswordView.as_view(),
        name='forgot_password'),

    url(r'^register/$', RegisterUserView.as_view(),
        name='register_user'),

    url(r'^profile/$', UserProfileView.as_view(),
        name='user_profile'),
]
