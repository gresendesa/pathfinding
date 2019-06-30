import pydot

class DOT:

	def __init__(self, filename):
		graph = pydot.graph_from_dot_file(filename)
		edges = graph[0].obj_dict["edges"]
		self.vertices = list(set([edge[0] for edge in edges] + [edge[1] for edge in edges]))
		self.edges = [{"edge": edge, "label":edges[edge][0]['attributes']['label']} for edge in edges]