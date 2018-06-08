from django.urls import path
from . import views

app_name = 'query'

urlpatterns = [
    # /
    path(
        "",
        views.SPARQLQueryAPIView.as_view(),
        name='query-list-create'
    ),
    # /queries
    path(
        "queries/",
        views.SPARQLQueryListCreateAPIView.as_view(),
        name='query-list-create'
    ),
    # /queries/<pk>/details/
    path(
        "queries/<int:pk>/details/",
        views.SPARQLQueryDetailsAPIView.as_view(),
        name='query-details'
    ),
]
