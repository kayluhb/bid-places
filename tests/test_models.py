#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_bid-places
------------

Tests for `bid-places` models module.
"""

from django.test import TestCase

from bid_places.models import Place, PlaceCategory


class TestBid_places(TestCase):

    def setUp(self):
        pass

    def test_places(self):
        Place.objects.create(name='foo')

    def test_place_categories(self):
        PlaceCategory.objects.create(title='foo')

    def tearDown(self):
        pass
