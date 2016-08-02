# -*- coding: utf-8 -*-
from django.contrib import admin

from django_utils.admin import (
    PUBLISHING_INFO, make_hidden, make_published, make_unpublished)

from .models import (Place)


class PlaceAdmin(admin.ModelAdmin):
    """ A class for the Place admin
    """
    def view_link(self):
        """ Returns a link to the Place """
        return "<a href='{}' target='_parent'>View</a>".format(
            self.get_absolute_url()
        )

    # Change list settings
    view_link.short_description = 'View on Site'
    view_link.allow_tags = True
    list_display = (
        'title', 'status', view_link,
    )
    list_display_links = ('title',)
    list_editable = ('status',)
    list_filter = ('status', 'updated_at')
    search_fields = ('title',)
    actions = [make_hidden, make_published, make_unpublished]

    # Form settings
    fieldsets = [
        PUBLISHING_INFO,
        (None, {'fields': [
            'title',
        ]}),
    ]
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True
admin.site.register(Place, PlaceAdmin)
