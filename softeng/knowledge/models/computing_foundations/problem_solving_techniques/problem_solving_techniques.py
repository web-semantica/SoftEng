from core import Query, Sesame
from .definition_of_problem_solving import DefinitionOfProblemSolving
from .formulating_the_real_problem import FormulatingTheRealProblem
from .analyze_the_problem import AnalyzeTheProblem
from .design_a_solution_search_strategy import DesignASolutionSearchStrategy
from .problem_solving_using_programs import ProblemSolvingUsingPrograms


class ProblemSolvingTechniques(object):
    """
    Topic: Problem Solving Techniques
    """

    ANALYZE_THE_PROBLEM = 0
    DEFINITION_OF_PROBLEM_SOLVING = 1
    DESIGN_A_SOLUTION_SEARCH_STRATEGY = 2
    FORMULATING_THE_REAL_PROBLEM = 3
    PROBLEM_SOLVING_USING_PROGRAMS = 4

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
              es:Problem_Solving_Techniques dc:title ?title
            }
        """

        result = Query.run(Sesame.endpoint, query)

        return result[0]

    def get_subtopic(self, subtopic):
        """
        Get a specific subtopic.
        """

        if subtopic == self.ANALYZE_THE_PROBLEM:
            return AnalyzeTheProblem()
        elif subtopic == self.DEFINITION_OF_PROBLEM_SOLVING:
            return DefinitionOfProblemSolving()
        elif subtopic == self.DESIGN_A_SOLUTION_SEARCH_STRATEGY:
            return DesignASolutionSearchStrategy()
        elif subtopic == self.FORMULATING_THE_REAL_PROBLEM:
            return FormulatingTheRealProblem()
        elif subtopic == self.PROBLEM_SOLVING_USING_PROGRAMS:
            return ProblemSolvingUsingPrograms()
        else:
            return None
