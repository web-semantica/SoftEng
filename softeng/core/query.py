import urllib
import httplib2
import json


class Query(object):
    """
    Class that run the SPARQL queries
    """

    @classmethod
    def run(cls, endpoint, query):
        """
        Run the query.
        """

        headers = {
            'content-type': 'application/x-www-form-urlencoded',
            'accept': 'application/sparql-results+json'
        }

        (response, content) = httplib2.Http().request(
            endpoint,
            'POST',
            urllib.parse.urlencode({'query': query}),
            headers=headers
        )

        print("Response %s" % response.status)

        results = json.loads(content.decode('utf-8'))

        return results['results']['bindings']
