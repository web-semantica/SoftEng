from core import Query, Sesame


class CoreBasicContent(object):
    """
    Core basic content to software engineering curriculum.
    """

    def __init__(self):
        """
        Create the core basic content model.
        """

        result = self.get_information()

        self.title = result['title']['value']
        self.description = result['description']['value']
        self.knowledges = self.get_knowledges()

    def get_information(self):
        """
        Get the data from triple store.
        """

        query = """
            PREFIX es: <http://www.semanticweb.org/ontologies/2018/Software_Engineering/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>

            SELECT DISTINCT ?title ?description
            WHERE {
              es:Core_Basic_Content dc:title ?title ;
              dc:description ?description
            }
        """

        result = Query.run(Sesame.endpoint, query)

        return result[0]

    def get_knowledges(self):
        """
        Get the knowledges from triple store.
        """

        query = """
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX es: <http://www.semanticweb.org/ontologies/2018/Software_Engineering/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>

            SELECT DISTINCT ?title
            WHERE {
              es:Core_Basic_Content rdfs:subClassOf ?restriction .
              ?restriction owl:onProperty es:hasKnowledgeArea .
              ?restriction owl:someValuesFrom ?knowledges .
              ?knowledges dc:title ?title
            }
        """

        result = Query.run(Sesame.endpoint, query)

        knowledges = []
        for knowledge in result:
            knowledges.append(knowledge['title']['value'])

        return knowledges
