# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	Place,
	PlaceCategory,
)


class PlaceCreateView(CreateView):

    model = Place


class PlaceDeleteView(DeleteView):

    model = Place


class PlaceDetailView(DetailView):

    model = Place


class PlaceUpdateView(UpdateView):

    model = Place


class PlaceListView(ListView):

    model = Place


class PlaceCategoryCreateView(CreateView):

    model = PlaceCategory


class PlaceCategoryDeleteView(DeleteView):

    model = PlaceCategory


class PlaceCategoryDetailView(DetailView):

    model = PlaceCategory


class PlaceCategoryUpdateView(UpdateView):

    model = PlaceCategory


class PlaceCategoryListView(ListView):

    model = PlaceCategory

