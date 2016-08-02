# -*- coding: utf-8 -*-
try:
    from django.utils.translation import ugettext_lazy as _

    from cms.app_base import CMSApp
    from cms.apphook_pool import apphook_pool


    class BIDPlaces(CMSApp):
        """ A class to hook the Places into the django cms
        """
        name = _("Places")
        urls = ["bid_places.urls"]
    apphook_pool.register(BIDPlaces)

except ImportError:
    pass
