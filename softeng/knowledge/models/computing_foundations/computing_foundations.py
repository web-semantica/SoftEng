from core import Query, Sesame
from .problem_solving_techniques import ProblemSolvingTechniques
from .abstraction import Abstraction
from .programming_fundamentals import ProgrammingFundamentals
from .algorithms_and_complexity import AlgorithmsAndComplexity
from .basic_concept_of_a_system import BasicConceptOfASystem
from .basic_developer_human_factors import BasicDeveloperHumanFactors
from .basic_user_human_factors import BasicUserHumanFactors


class ComputingFoundations(object):
    """
    Computing Foundations Knowledge Area.
    """

    ABSTRACTION = 0
    ALGORITHMS_AND_COMPLEXITY = 1
    BASIC_CONCEPT_OF_A_SYSTEM = 2
    BASIC_DEVELOPER_HUMAN_FACTORS = 3
    BASIC_USER_HUMAN_FACTORS = 4
    COMPILER_BASICS = 5
    COMPUTER_ORGANIZATION = 6
    DATA_STRUCTURE_AND_REPRESENTATION = 7
    DATABASE_BASICS_AND_DATA_MANAGEMENT = 8
    DEBUGGING_TOOLS_AND_TECHNIQUES = 9
    NETWORK_COMMUNICATION_BASICS = 10
    OPERATING_SYSTEMS_BASICS = 11
    PARALLEL_AND_DISTRIBUTED_COMPUTING = 12
    PROBLEM_SOLVING_TECHNIQUES = 13
    PROGRAMMING_FUNDAMENTALS = 14
    PROGRAMMING_LANGUAGE_BASICS = 15
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

        if topic == self.ABSTRACTION:
            return Abstraction()
        elif topic == self.ALGORITHMS_AND_COMPLEXITY:
            return AlgorithmsAndComplexity()
        elif topic == self.BASIC_CONCEPT_OF_A_SYSTEM:
            return BasicConceptOfASystem()
        elif topic == self.BASIC_DEVELOPER_HUMAN_FACTORS:
            return BasicDeveloperHumanFactors()
        elif topic == self.BASIC_USER_HUMAN_FACTORS:
            return BasicUserHumanFactors()
        elif topic == self.PROBLEM_SOLVING_TECHNIQUES:
            return ProblemSolvingTechniques()
        elif topic == self.PROGRAMMING_FUNDAMENTALS:
            return ProgrammingFundamentals()
        else:
            return None
