from core import Query, Sesame
from .error_messages import ErrorMessages
from .software_robustness import SoftwareRobustness
from .user_input_and_output import UserInputAndOutput


class BasicUserHumanFactors(object):
    """
    Topic: Basic User Human Factors
    """

    ERROR_MESSAGES = 0
    SOFTWARE_ROBUSTNESS = 1
    USER_INPUT_AND_OUTPUT = 2

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
              es:Basic_User_Human_Factors dc:title ?title
            }
        """

        result = Query.run(Sesame.endpoint, query)

        return result[0]

    def get_subtopic(self, subtopic):
        """
        Get a specific subtopic.
        """

        if subtopic == self.ERROR_MESSAGES:
            return ErrorMessages()
        elif subtopic == self.SOFTWARE_ROBUSTNESS:
            return SoftwareRobustness()
        elif subtopic == self.USER_INPUT_AND_OUTPUT:
            return UserInputAndOutput()
        else:
            return None
