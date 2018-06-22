from core import Query, Sesame


class SoftwareEngineering(object):
    """
    Class to get information about Software Enginering.
    """

    def __init__(self):
        """
        Create Software Engineering model.
        """

        result = self.get_information()
        self.title = result['title']['value']
        self.label = result['label']['value']
        self.version = result['version']['value']
        self.creator = result['creator']['value']
        self.habilitation = result['habilitation']['value']
        self.source = result['source']['value']
        self.performance = result['performance']['value']
        self.professional_profile = result['professional_profile']['value']
        self.description = result['description']['value']
        self.goals = result['goals']['value']

    def get_information(self):
        """
        Get all information about software engineering ontology
        """

        query = """
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX es: <http://www.semanticweb.org/ontologies/2018/Software_Engineering/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>

            SELECT DISTINCT ?title ?version ?creator ?habilitation ?source ?performance ?professional_profile
            ?description ?goals ?label
            WHERE {
              ?course dc:title "Software Engineering Course"@en ;
              dc:title ?title ;
              owl:versionInfo ?version ;
              dc:creator ?creator ;
              es:habilitation ?habilitation ;
              dc:source ?source ;
              es:performance ?performance ;
              es:professional_profile ?professional_profile ;
              dc:description ?description ;
              es:goals ?goals ;
              rdfs:label ?label
            }
        """

        result = Query.run(Sesame.endpoint, query)

        return result[0]
