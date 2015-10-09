from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from .views import HomeView, IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^home/$', login_required(HomeView.as_view()), name='home'),
]
