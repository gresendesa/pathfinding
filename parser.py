import pydot
from pprint import pprint

graph = pydot.graph_from_dot_file("g1.dot")

edges = graph[0].obj_dict["edges"]

pprint(edges)