from core import Query, Sesame
from .comments import Comments
from .structure import Structure


class BasicDeveloperHumanFactors(object):
    """
    Topic: Basic Developer Human Factors
    """

    COMMENTS = 0
    STRUCTURE = 1

    def __init__(self):
        """
        Create a topic.
        """

        result = self.get_information()

        self.title = result['title']['value']

    def get_information(self):
        """
        Get the information from triple store
        """

        query = """
            PREFIX es: <http://www.semanticweb.org/ontologies/2018/Software_Engineering/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>

            SELECT DISTINCT ?title
            WHERE {
              es:Basic_Developer_Human_Factors dc:title ?title
            }
        """

        result = Query.run(Sesame.endpoint, query)

        return result[0]

    def get_subtopic(self, subtopic):
        """
        Get a specific subtopic.
        """

        if subtopic == self.COMMENTS:
            return Comments()
        elif subtopic == self.STRUCTURE:
            return Structure()
        else:
            return None
