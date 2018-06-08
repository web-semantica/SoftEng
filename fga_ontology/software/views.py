from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from core import Query
from .models import SPARQLQuery
from .serializer import (
    SPARQLQuerySerializer,
    SPARQLQueryResultSerializer
)


class SPARQLQueryListCreateAPIView(generics.ListCreateAPIView):
    """
    List and create specific SPARQL query.
    """

    serializer_class = SPARQLQuerySerializer

    queryset = SPARQLQuery.objects.all()


class SPARQLQueryDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update and destroy SPARQL queries.
    """

    serializer_class = SPARQLQuerySerializer

    queryset = SPARQLQuery.objects.all()


class SPARQLQueryAPIView(generics.GenericAPIView):
    """
    Return a result of query.
    """

    serializer_class = SPARQLQueryResultSerializer

    queryset = SPARQLQuery.objects.all()

    def get(self, request, *args, **kwargs):
        """
        See the results
        """

        return Response("Insert your SPARQL query")

    def post(self, request, *args, **kwargs):
        """
        Get the query and return the JSON result
        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        result = Query.run(
            serializer.data['endpoint'],
            serializer.data['query']
        )

        return Response(result, status=status.HTTP_200_OK)
