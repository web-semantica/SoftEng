from core import Query, Sesame
from .algorithmic_analysis import AlgorithmicAnalysis
from .algorithmic_analysis_strategies import AlgorithmicAnalysisStrategies
from .algorithmic_design_strategies import AlgorithmicDesignStrategies
from .attributes_of_algorithms import AttributesOfAlgorithms
from .overview_of_algorithms import OverviewOfAlgorithms


class AlgorithmsAndComplexity(object):
    """
    Topic: Algorithms and Complexity
    """

    ALGORITHMIC_ANALYSIS = 0
    ALGORITHMIC_ANALYSIS_STRATEGIES = 1
    ALGORITHMIC_DESIGN_STRATEGIES = 2
    ATTRIBUTES_OF_ALGORITHMS = 3
    OVERVIEW_OF_ALGORITHMS = 4

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
              es:Algorithms_and_Complexity dc:title ?title
            }
        """

        result = Query.run(Sesame.endpoint, query)

        return result[0]

    def get_subtopic(self, subtopic):
        """
        Get a specific subtopic.
        """

        if subtopic == self.ALGORITHMIC_ANALYSIS:
            return AlgorithmicAnalysis()
        elif subtopic == self.ALGORITHMIC_ANALYSIS_STRATEGIES:
            return AlgorithmicAnalysisStrategies()
        elif subtopic == self.ALGORITHMIC_DESIGN_STRATEGIES:
            return AlgorithmicDesignStrategies()
        elif subtopic == self.ATTRIBUTES_OF_ALGORITHMS:
            return AttributesOfAlgorithms()
        elif subtopic == self.OVERVIEW_OF_ALGORITHMS:
            return OverviewOfAlgorithms()
        else:
            return None
