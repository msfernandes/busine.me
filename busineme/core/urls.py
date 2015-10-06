from django.conf.urls import url
from django.views.generic import TemplateView
from .views import BuslineSearchResultView, BuslineProfileView

urlpatterns = [
    url(r'^search/busline/$', BuslineSearchResultView.as_view(),
        name='search_results'),
    url(r'busline/(?P<line_number>[0-9]+)/$', BuslineProfileView.as_view(),
        name='busline_profile'),
    url(r'busline/(?P<line_number>[0-9]+\.[0-9]+)/$',
        BuslineProfileView.as_view(), name='busline_profile'),
    url(r'^search/', TemplateView.as_view(template_name="search.html"),
        name="search"),
]
