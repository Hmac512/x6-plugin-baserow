from baserow.contrib.database.views.registries import ViewType

from .models import GraphView


class GraphViewType(ViewType):
    type = 'graph'
    model_class = GraphView