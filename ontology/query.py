import urllib
import httplib2
import json

query = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX es: <http://www.semanticweb.org/ontologies/2018/engenhaira_de_software/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>

    SELECT ?disciplinas ?titulo ?ementa
    WHERE {
      ?disciplinas rdfs:subClassOf ?restricao1 .
      ?restricao1 owl:onProperty es:ePreRequisitoDe .
      ?restricao1 owl:someValuesFrom es:%s .
      ?disciplinas rdfs:subClassOf ?restricao2 .
      ?restricao2 owl:onProperty es:estaNoFluxoDo .
      ?restricao2 owl:someValuesFrom es:%s .
      ?disciplinas dc:title ?titulo .
      ?disciplinas es:ementa ?ementa
    }
""" % (
    "Aprendizado_de_Maquina",
    "Segundo_Semestre"
)

repository = 'softeng'
endpoint = "http://localhost:8001/openrdf-sesame/repositories/{0}".format(repository)

print("POST SPARQL query to %s" % endpoint)

params = {'query': query}

headers = {
    'content-type': 'application/x-www-form-urlencoded',
    'accept': 'application/sparql-results+json'
}

(response, content) = httplib2.Http().request(
    endpoint,
    'POST',
    urllib.parse.urlencode(params),
    headers=headers
)

print("Response %s" % response.status)

results = json.loads(content.decode('utf-8'))

for result in results['results']['bindings']:
    print("URI: " + str(result['disciplinas']['value']))
    print("Título: " + result['titulo']['value'])
    print("Ementa: " + result['ementa']['value'])
    print("")
