# -*- coding: utf-8 -*-

from igraph import Graph, plot
import re

'''
Esta classe, criada por nós, lê arquivos .dot
'''
class RegexDot:
	def __init__(self, nome_do_arquivo):
		conteudo = f=open(nome_do_arquivo, "r").read()
		linhas = re.findall(r'.+ -> .+ \[label=.+\]',conteudo)
		vertices = []
		arestas = []
		for linha in linhas:
			pedacos = re.findall(r'(.+) -> (.*) \[label=(.*)\]',re.sub(r'[\n\t]','',linha))
			vertices.extend([int(pedacos[0][0]),int(pedacos[0][1])])
			vertices = list(set(vertices))
			arestas.append({"aresta":(int(pedacos[0][0]),int(pedacos[0][1])), "peso":float(pedacos[0][2])})

		self.vertices = vertices
		self.arestas = arestas

class Grafo:
	def __init__(self, dot_filename, directed=False):

		self.igraph = Graph(directed=directed)

		dot = RegexDot(dot_filename)
		self.arestas = [v["aresta"] for v in dot.arestas]
		weights = [v["peso"] for v in dot.arestas]
		self.vertices = dot.vertices
		#print(self.vertices)
		self.igraph.add_vertices(int(len(self.vertices))) #adiciona vértices ao grafo (índices 0 a 3)
		self.igraph.add_edges(self.arestas) #adiciona 4 arestas ao grafo (índices de 0 a 3)
		#print self.igraph.get_edgelist()
		self.igraph.vs["name"] = ['%d' % v for v in self.vertices]
		self.igraph.es["weight"] = weights #atribui peso às arestas

		#mostrando o grafo na tela

		self.igraph.vs["label"] = self.igraph.vs["name"] #rotula os vértices com seus respectivos nomes
		self.igraph.es["label"] = self.igraph.es["weight"] #rotula as arestas com seus respectivos pesos

	def plot(self):
		layout = self.igraph.layout("kk") #atribui um layout para plotagem do grafo
		plot(self.igraph,layout=layout) #apresenta o grafo usando interface gráfica


	def plot_path(self, tabela, vinicial, vdestino):

		self.igraph.es["color"] = "gray"
		self.igraph.vs["color"] = "gray"

		self.igraph.vs[vinicial]["color"] = "red"
		self.igraph.vs[vdestino]["color"] = "red"

		
		def color_edge(graph, v1, v2):
			try:
				edges = graph.es.find(_within=[v1,v2])
				edges["color"] = "red"
			except ValueError:
				pass

		def print_path(graph, tabela, vinicial, vdestino):

			if tabela[vdestino]['origem'] == vinicial:
				color_edge(graph, vinicial, vinicial)
			elif tabela[vdestino]['origem'] is None:
				pass
			else:
				color_edge(graph, vdestino, tabela[vdestino]['origem'])
				print_path(graph, tabela, vdestino, tabela[vdestino]['origem'])

		print_path(self.igraph, tabela, vinicial, vdestino)
		#
		self.plot()
