from django.conf.urls import url
from .views import BuslineSearchView

urlpatterns = [
    url(r'^search/busline/$', BuslineSearchView.as_view(),
        name='buline_search'),
]
