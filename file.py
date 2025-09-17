from rdflib import Graph, Namespace
import re

g = Graph()

BAD = Namespace("http://example.org/badminton/")

g.add((BAD.LeeChongWei, BAD.playsFor, BAD.Malaysia))
g.add((BAD.LinDan, BAD.playsFor, BAD.China))
g.add((BAD.PVSindhu, BAD.playsFor, BAD.India))
g.add((BAD.ViktorAxelsen, BAD.playsFor, BAD.Denmark))

g.add((BAD.LeeChongWei, BAD.coachedBy, BAD.MisbunSidek))
g.add((BAD.LinDan, BAD.coachedBy, BAD.XiaXuanze))
g.add((BAD.PVSindhu, BAD.coachedBy, BAD.KimJi))
g.add((BAD.ViktorAxelsen, BAD.coachedBy, BAD.PeterGade))

playerName = input("Enter player name: ")

# remove spaces and join the name
name = playerName.split()
name = "".join(name)

qres = g.query(f"""
    SELECT ?country
    WHERE {{
        <http://example.org/badminton/{name}> <http://example.org/badminton/playsFor> ?country .
    }}
""")

coachres = g.query(f"""
    SELECT ?coach
    WHERE {{
        <http://example.org/badminton/{name}> <http://example.org/badminton/coachedBy> ?coach .
    }}
""")


for row in qres:
    print(f"{playerName} plays for:", row[0].split("/")[-1])

for row in coachres:
    coachName = row[0].split("/")[-1]
    match = r'(?=[A-Z])'
    n = re.split(match, coachName)
    for i in n:
        if i == "":
            n.remove(i)
    print(f"{playerName} is coached by:",     " ".join(n))