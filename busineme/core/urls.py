from django.conf.urls import url
from django.views.generic import TemplateView
from .views import BuslineSearchResultView

urlpatterns = [
    url(r'^search/busline/$', BuslineSearchResultView.as_view(),
        name='search_results'),

    url(r'^search/', TemplateView.as_view(template_name="search.html"),
        name="search"),
]