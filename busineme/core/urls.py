from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from .views import (BuslineSearchResultView, FavoriteBuslineView,
                    BuslineProfileView, BuslinePostView, BuslinePostDetailView)

urlpatterns = [
    url(r'^search/busline/$', BuslineSearchResultView.as_view(),
        name='search_results'),

    url(r'busline/(?P<line_number>[0-9]+)/$', BuslineProfileView.as_view(),
        name='busline_profile'),

    url(r'busline/(?P<line_number>[0-9]+\.[0-9]+)/$',
        BuslineProfileView.as_view(), name='busline_profile'),

    url(r'^search/', TemplateView.as_view(template_name="search.html"),
        name="search"),

    url(r'^favorite/busline/$', login_required(FavoriteBuslineView.as_view()),
        name="favorite_busline"),

    url(r'^post/busline/$', login_required(BuslinePostView.as_view()),
        name="post_busline"),

    url(r'^post/(?P<post_id>[0-9]+)/$', BuslinePostDetailView.as_view(),
        name="post_detail")
]
