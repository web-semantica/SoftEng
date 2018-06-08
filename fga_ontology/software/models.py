from django.db import models


class SPARQLQuery(models.Model):
    """
    Model to store querys.
    """

    question = models.CharField(
        "Question",
        max_length=100,
        help_text="Question to specific query."
    )

    query = models.TextField(
        "Query",
        help_text="SPARQL Query to get specific result from triplestore"
    )

    def __str__(self):
        """
        Return the object by his question.
        """

        return self.question

    class Meta:
        verbose_name = "SPARQL Query"
        verbose_name_plural = "SPARQL Queries"
