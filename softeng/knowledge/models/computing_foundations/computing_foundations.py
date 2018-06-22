from core import Query, Sesame
from .problem_solving_techniques import ProblemSolvingTechniques


class ComputingFoundations(object):
    """
    Computing Foundations Knowledge Area.
    """

    PROBLEM_SOLVING_TECHNIQUES = 0
    ABSTRACTION = 1
    PROGRAMMING_FUNDAMENTALS = 2
    PROGRAMMING_LANGUAGE_BASICS = 3
    DEBUGGING_TOOLS_AND_TECHNIQUES = 4
    DATA_STRUCTURE_AND_REPRESENTATION = 5
    ALGORITHMS_AND_COMPLEXITY = 6
    BASIC_CONCEPT_OF_A_SYSTEM = 7
    COMPUTER_ORGANIZATION = 8
    COMPILER_BASICS = 9
    OPERATING_SYSTEMS_BASICS = 10
    DATABASE_BASICS_AND_DATA_MANAGEMENT = 11
    NETWORK_COMMUNICATION_BASICS = 12
    PARALLEL_AND_DISTRIBUTED_COMPUTING = 13
    BASIC_USER_HUMAN_FACTORS = 14
    BASIC_DEVELOPER_HUMAN_FACTORS = 15
    SECURE_SOFTWARE_DEVELOPMENT_AND_MAINTENANCE = 16

    def __init__(self):
        """
        Create a knowledge area.
        """

        result = self.get_information()

        self.title = result['title']['value']
        self.curriculum = result['curriculum']['value']

    def get_information(self):
        """
        Get the information from triple store
        """

        query = """
            PREFIX es: <http://www.semanticweb.org/ontologies/2018/Software_Engineering/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>

            SELECT DISTINCT ?title ?curriculum
            WHERE {
              es:Computing_Foundations dc:title ?title .
              es:Computing_Foundations rdfs:subClassOf ?restriction .
              ?restriction owl:onProperty es:isKnowledgeAreaOf .
              ?restriction owl:someValuesFrom ?curriculum_url .
              ?curriculum_url dc:title ?curriculum
            }
        """

        result = Query.run(Sesame.endpoint, query)

        return result[0]

    def get_topic(self, topic):
        """
        Get a specific topic
        """

        if topic == self.PROBLEM_SOLVING_TECHNIQUES:
            return ProblemSolvingTechniques()
        else:
            return None
