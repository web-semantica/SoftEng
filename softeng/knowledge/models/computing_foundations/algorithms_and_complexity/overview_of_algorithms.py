from core import Query, Sesame


class OverviewOfAlgorithms(object):
    """
    Subtopic: Overview of Algorithms
    """

    def __init__(self):
        """
        Create a subtopic.
        """

        result = self.get_information()

        self.title = result['title']['value']
        self.description = result['description']['value']

    def get_information(self):
        """
        Get the data from triple store
        """

        query = """
            PREFIX es: <http://www.semanticweb.org/ontologies/2018/Software_Engineering/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>

            SELECT DISTINCT ?title ?description
            WHERE {
              es:Overview_of_Algorithms dc:title ?title ;
              dc:description ?description
            }
        """

        result = Query.run(Sesame.endpoint, query)

        return result[0]
