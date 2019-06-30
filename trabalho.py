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



def djikstra():
	pass

def bellman_ford():
	pass

def rpf():
	pass

def spanning_tree():
	pass

def plota_arquivo_dot():
	g = Graph()

	dot = RegexDot("g1.dot")
	edges = [v["aresta"] for v in dot.arestas]
	weights = [v["peso"] for v in dot.arestas]
	vertices = dot.vertices

	g.add_vertices(len(vertices)) #adiciona 4 vértices ao grafo (índices 0 a 3)
	g.add_edges(edges) #adiciona 4 arestas ao grafo (índices de 0 a 3)

	g.vs["name"] = ['%d' % v for v in vertices]
	g.es["weight"] = weights #atribui peso às arestas

	#mostrando o grafo na tela

	g.vs["label"] = g.vs["name"] #rotula os vértices com seus respectivos nomes
	g.es["label"] = g.es["weight"] #rotula as arestas com seus respectivos pesos

	layout = g.layout("kk") #atribui um layout para plotagem do grafo

	print g #imprime o grafo na linha de comando

	plot(g,layout = layout) #apresenta o grafo usando interface gráfica

plota_arquivo_dot()


