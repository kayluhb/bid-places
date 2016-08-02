# -*- coding: utf-8 -*-
from django.views.generic import (
    DetailView,
    ListView
)

from .models import (
    Place,
    PlaceCategory,
)


class PlaceDetailView(DetailView):
    """ A class for the PlaceDetailView
    """
    model = Place


class PlaceListView(ListView):
    """ A class for the PlaceListView
    """
    model = Place


class PlaceCategoryDetailView(DetailView):
    """ A class for the PlaceCategoryDetailView
    """
    model = PlaceCategory


class PlaceCategoryListView(ListView):
    """ A class for the PlaceCategoryListView
    """
    model = PlaceCategory
