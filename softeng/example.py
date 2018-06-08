from core import Query, Sesame

endpoint = Sesame.endpoint
query_sesame = """
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX es: <http://www.semanticweb.org/ontologies/2018/engenhaira_de_software/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>

    SELECT DISTINCT ?disciplinas ?codigo ?sigla ?titulo ?creditos ?orgao ?ementa
    WHERE {
      ?disciplinas rdfs:subClassOf ?restricao1 .
      ?restricao1 owl:onProperty es:ePreRequisitoDe .
      ?restricao1 owl:someValuesFrom es:Aprendizado_de_Maquina .
      ?disciplinas rdfs:subClassOf ?restricao2 .
      ?restricao2 owl:onProperty es:estaNoFluxoDo .
      ?restricao2 owl:someValuesFrom es:Segundo_Semestre .
      ?disciplinas rdfs:subClassOf ?restricao3 .
      ?restricao3 owl:onProperty es:estaNoOrgao .
      ?restricao3 owl:someValuesFrom ?orgao .
      ?disciplinas dc:title ?titulo .
      ?disciplinas es:codigo ?codigo .
      ?disciplinas es:creditos ?creditos .
      ?disciplinas es:sigla ?sigla .
      ?disciplinas es:ementa ?ementa
    }
"""

# print(Query.run(endpoint, query))

query_software = """
    SELECT DISTINCT ?resumo
    WHERE {
        dbr:Software_engineering dbo:abstract ?resumo
        FILTER (lang(?resumo) = 'pt')
    }
"""

query_unb = """
    SELECT DISTINCT ?sigla ?nome ?cidade ?pais ?estado ?site ?resumo
    WHERE {
        dbr:University_of_Brasília dbp:sigla ?sigla ;
        rdfs:label ?nome ;
        foaf:homepage ?site ;
        dbo:abstract ?resumo ;
        dbo:city ?city .
        ?city rdfs:label ?cidade .
        dbr:University_of_Brasília dbo:country ?country .
        ?country rdfs:label ?pais .
        dbr:University_of_Brasília dbo:state ?state .
        ?state rdfs:label ?estado .

        FILTER (lang(?resumo) = 'pt')
        FILTER (lang(?cidade) = 'pt')
        FILTER (lang(?pais) = 'pt')
        FILTER (lang(?estado) = 'pt')
        FILTER (lang(?nome) = 'pt')
    }
"""

print(Query.run("http://dbpedia.org/sparql", query_unb))
