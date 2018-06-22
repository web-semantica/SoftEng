from core import Query, Sesame
from .emergent_system_properties import EmergentSystemProperties
from .overview_of_a_computer_system import OverviewOfAComputerSystem
from .systems_engineering import SystemsEngineering


class BasicConceptOfASystem(object):
    """
    Topic: Basic Concept of a System
    """

    EMERGENT_SYSTEM_PROPERTIES = 0
    OVERVIEW_OF_A_COMPUTER_SYSTEM = 1
    SYSTEMS_ENGINEERING = 2

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
              es:Basic_Concept_of_a_System dc:title ?title
            }
        """

        result = Query.run(Sesame.endpoint, query)

        return result[0]

    def get_subtopic(self, subtopic):
        """
        Get a specific subtopic.
        """

        if subtopic == self.EMERGENT_SYSTEM_PROPERTIES:
            return EmergentSystemProperties()
        elif subtopic == self.OVERVIEW_OF_A_COMPUTER_SYSTEM:
            return OverviewOfAComputerSystem()
        elif subtopic == self.SYSTEMS_ENGINEERING:
            return SystemsEngineering()
        else:
            return None
