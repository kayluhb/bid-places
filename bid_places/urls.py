# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(
        regex="^Place/~create/$",
        view=views.PlaceCreateView.as_view(),
        name='Place_create',
    ),
    url(
        regex="^Place/(?P<pk>\d+)/~delete/$",
        view=views.PlaceDeleteView.as_view(),
        name='Place_delete',
    ),
    url(
        regex="^Place/(?P<pk>\d+)/$",
        view=views.PlaceDetailView.as_view(),
        name='Place_detail',
    ),
    url(
        regex="^Place/(?P<pk>\d+)/~update/$",
        view=views.PlaceUpdateView.as_view(),
        name='Place_update',
    ),
    url(
        regex="^Place/$",
        view=views.PlaceListView.as_view(),
        name='Place_list',
    ),
	url(
        regex="^PlaceCategory/~create/$",
        view=views.PlaceCategoryCreateView.as_view(),
        name='PlaceCategory_create',
    ),
    url(
        regex="^PlaceCategory/(?P<pk>\d+)/~delete/$",
        view=views.PlaceCategoryDeleteView.as_view(),
        name='PlaceCategory_delete',
    ),
    url(
        regex="^PlaceCategory/(?P<pk>\d+)/$",
        view=views.PlaceCategoryDetailView.as_view(),
        name='PlaceCategory_detail',
    ),
    url(
        regex="^PlaceCategory/(?P<pk>\d+)/~update/$",
        view=views.PlaceCategoryUpdateView.as_view(),
        name='PlaceCategory_update',
    ),
    url(
        regex="^PlaceCategory/$",
        view=views.PlaceCategoryListView.as_view(),
        name='PlaceCategory_list',
    ),
	]
