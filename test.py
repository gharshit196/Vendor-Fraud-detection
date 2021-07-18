from py2neo import Graph
graph = Graph("bolt://3.233.241.33:7687", auth=("neo4j", "knees-gear-wreck"))
try:
    graph.run("Match () Return 1 Limit 1")
    print('ok')
except Exception:
    print('not ok')