# -*- coding: utf-8 -*-
import itertools

from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from django_utils.models import (
    OrderedModel, StatusModel, StatusManager, TimeStampedModel)


class Place(StatusModel, TimeStampedModel):
    """ The place model
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    categories = models.ManyToManyField('PlaceCategory', blank=True)
    objects = StatusManager()


class PlaceCategory(OrderedModel, TimeStampedModel):
    """ The categories of the places
    """
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ('order', 'title')
        verbose_name_plural = 'Place Categories'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        """ Returns the absolute url of the event """
        return '{}?c={}'.format(reverse('places_index'), self.id)

    def save(self, *args, **kwargs):
        """ Save it and make sure we don't have a duplicate slug
        """

        if not self.slug:
            self.slug = PlaceCategory.generate_slug(self.title, self.id)

        super(PlaceCategory, self).save(*args, **kwargs)

    @classmethod
    def generate_slug(cls, title, current_pk):
        """ Generates a unique slug if not set in the form """
        new_slug = orig_slug = slugify(title)

        for idx in itertools.count(1):
            slug_exists = cls.objects.exclude(pk=current_pk)\
                .filter(slug=new_slug).exists()
            if not slug_exists:
                break
            new_slug = '%s-%d' % (orig_slug, idx)

        return new_slug
