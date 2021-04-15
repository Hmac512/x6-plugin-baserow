from django.conf.urls import url
from .views import ExampleView

app_name = 'graph_visualization.api'

urlpatterns = []


urlpatterns = [
    url(r'example/$', ExampleView.as_view(), name='example'),
]
