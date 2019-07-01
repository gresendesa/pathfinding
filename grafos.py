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