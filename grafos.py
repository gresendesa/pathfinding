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
	def __init__(self, dot_filename):

		self.grafo = Graph()

		dot = RegexDot(dot_filename)
		edges = [v["aresta"] for v in dot.arestas]
		weights = [v["peso"] for v in dot.arestas]
		self.vertices = dot.vertices

		self.grafo.add_vertices(len(self.vertices)) #adiciona 4 vértices ao grafo (índices 0 a 3)
		self.grafo.add_edges(edges) #adiciona 4 arestas ao grafo (índices de 0 a 3)

		self.grafo.vs["name"] = ['%d' % v for v in self.vertices]
		self.grafo.es["weight"] = weights #atribui peso às arestas

		#mostrando o grafo na tela

		self.grafo.vs["label"] = self.grafo.vs["name"] #rotula os vértices com seus respectivos nomes
		self.grafo.es["label"] = self.grafo.es["weight"] #rotula as arestas com seus respectivos pesos

	def plot(self):
		layout = self.grafo.layout("kk") #atribui um layout para plotagem do grafo
		plot(self.grafo,layout = layout) #apresenta o grafo usando interface gráfica