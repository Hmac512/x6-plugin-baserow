from django.apps import AppConfig

from baserow.core.registries import plugin_registry

from baserow.contrib.database.views.registries import view_type_registry


class PluginNameConfig(AppConfig):
    name = 'graph_visualization'

    def ready(self):
            from .plugins import PluginNamePlugin
            from .view_types import GraphViewType

            plugin_registry.register(PluginNamePlugin())
            view_type_registry.register(GraphViewType())
