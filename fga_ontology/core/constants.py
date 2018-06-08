class Sesame(object):
    """
    Constantes em relação ao banco de triplas e conexões.
    """

    repository = 'softeng'
    endpoint = "http://localhost:8001/openrdf-sesame/repositories/{0}".format(repository)
