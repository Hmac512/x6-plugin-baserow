import logging

from django.urls import path, include

from baserow.core.registries import Plugin

from .api import urls as api_urls


logger = logging.getLogger(__name__)


class PluginNamePlugin(Plugin):
    type = 'graph-visualization'

    def get_api_urls(self):
        return [
            path('graph-visualization/', include(api_urls, namespace=self.type)),
        ]
