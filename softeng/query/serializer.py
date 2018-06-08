from rest_framework import serializers
from core import Sesame
from .models import SPARQLQuery


class SPARQLQuerySerializer(serializers.ModelSerializer):
    """
    A serializer to queries SPARQL
    """

    query = serializers.CharField(
        style={
            'base_template': 'textarea.html',
            'rows': '10'
        }
    )

    class Meta:
        model = SPARQLQuery
        fields = ('id', 'question', 'query')


class SPARQLQueryResultSerializer(serializers.Serializer):
    """
    A serializer to queries SPARQL
    """

    endpoint = serializers.CharField(
        default=Sesame.endpoint,
        style={'placeholder': "Padrão: " + Sesame.endpoint}
    )

    query = serializers.CharField(
        style={
            'base_template': 'textarea.html',
            'rows': '10'
        }
    )
