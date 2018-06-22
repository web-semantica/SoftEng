from core import Query, Sesame
from .alternate_abstractions import AlternateAbstractions
from .encapsulation import Encapsulation
from .hierarchy import Hierarchy
from .levels_of_abstraction import LevelsOfAbstraction


class Abstraction(object):
    """
    Topic: Abstraction
    """

    ALTERNATE_ABSTRACTIONS = 0
    ENCAPSULATION = 1
    HIERARCHY = 2
    LEVELS_OF_ABSTRACTION = 3

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
              es:Abstraction dc:title ?title
            }
        """

        result = Query.run(Sesame.endpoint, query)

        return result[0]

    def get_subtopic(self, subtopic):
        """
        Get a specific subtopic.
        """

        if subtopic == self.ALTERNATE_ABSTRACTIONS:
            return AlternateAbstractions()
        elif subtopic == self.ENCAPSULATION:
            return Encapsulation()
        elif subtopic == self.HIERARCHY:
            return Hierarchy()
        elif subtopic == self.LEVELS_OF_ABSTRACTION:
            return LevelsOfAbstraction()
        else:
            return None
