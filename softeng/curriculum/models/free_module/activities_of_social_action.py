from core import Query, Sesame


class ActivitiesOfSocialAction(object):
    """
    Activities of Social Action Citizenship and Environment.
    """

    def __init__(self):
        """
        Create Activities of Social Action Citizenship and Environment model.
        """

        result = self.get_information()

        self.title = result['title']['value']
        self.description = result['description']['value']

    def get_information(self):
        """
        Get the data from triple store.
        """

        query = """
            PREFIX es: <http://www.semanticweb.org/ontologies/2018/Software_Engineering/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>

            SELECT DISTINCT ?title ?description
            WHERE {
              es:Activities_of_Social_Action_Citizenship_and_Environment dc:title ?title ;
              dc:description ?description
            }
        """

        result = Query.run(Sesame.endpoint, query)

        return result[0]
