class Sesame(object):
    """
    Constants in relation to the triple store and connections
    """

    repository = 'softeng'
    endpoint = "http://localhost:8001/openrdf-sesame/repositories/{0}".format(repository)
