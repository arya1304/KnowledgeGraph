from rdflib import Graph, Literal, RDF, URIRef, Namespace

g = Graph()

BAD = Namespace("http://example.org/badminton/")

g.add((BAD.LeeChongWei, BAD.playsFor, BAD.Malaysia))
g.add((BAD.LinDan, BAD.playsFor, BAD.China))
g.add((BAD.PVSindhu, BAD.playsFor, BAD.India))
g.add((BAD.ViktorAxelsen, BAD.playsFor, BAD.Denmark))

playerName = input()

qres = g.query(f"""
    SELECT ?country
    WHERE {{
        <http://example.org/badminton/{playerName}> <http://example.org/badminton/playsFor> ?country .
    }}
""")

for row in qres:
    print(f"{playerName} plays for:", row[0].split("/")[-1])
