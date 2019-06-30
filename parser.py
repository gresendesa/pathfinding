import pydot
from pprint import pprint

graph = pydot.graph_from_dot_file("g1.dot")

pprint(vars(graph[0]))