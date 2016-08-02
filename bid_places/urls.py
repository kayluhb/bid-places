# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex="^places/(?P<pk>\d+)/$",
        view=views.PlaceDetailView.as_view(),
        name='Place_detail',
    ),
    url(
        regex="^places/$",
        view=views.PlaceListView.as_view(),
        name='Place_list',
    ),
    url(
        regex="^categories/(?P<pk>\d+)/$",
        view=views.PlaceCategoryDetailView.as_view(),
        name='PlaceCategory_detail',
    ),
    url(
        regex="^categories/$",
        view=views.PlaceCategoryListView.as_view(),
        name='PlaceCategory_list',
    ),
]
