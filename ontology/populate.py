import urllib
import httplib2

repository = 'softeng'
context = "http://www.semanticweb.org/ontologies/2018-1/engenharia_de_software"
filename = './ontology/RDF/softeng.rdf'

print("Loading %s into %s in Sesame tripleStore" % (filename, context))

params = {'context': '<' + context + '>'}

endpoint = "http://localhost:8001/openrdf-sesame/repositories/{0}/statements?{1}".format(
    repository,
    urllib.parse.urlencode(params)
)

data = open(filename, 'r').read()

(response, content) = httplib2.Http().request(
    endpoint,
    'PUT',
    body=data.encode('utf-8'),
    headers={'content-type': 'application/rdf+xml'}
)

print("Response %s" % response.status)
print("Content %s" % content)
