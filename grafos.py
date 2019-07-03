# -*- coding: utf-8 -*-

from igraph import Graph, plot
import sys
import re

color = lambda color, txt='': "{}{}\033[00m".format(color, txt)
fundo_laranja = 	lambda txt='': color(color="\033[43m", txt=txt)
fundo_azul = 		lambda txt='': color(color="\033[44m", txt=txt)
magenta = 			lambda txt='': color(color="\033[36m", txt=txt)
white = 			lambda txt='': color(color="\033[37m", txt=txt)
azul =  			lambda txt='': color(color="\033[34m", txt=txt)
vermelho_claro = 	lambda txt='': color(color="\033[91m", txt=txt)
fundo_cinza_claro = lambda txt='': color(color="\033[47m", txt=txt)
preto = 			lambda txt='': color(color="\033[98m", txt=txt)
amarelo = 			lambda txt='': color(color="\033[93m", txt=txt)
purpura_claro = 	lambda txt='': color(color="\033[94m", txt=txt)

'''
Esta classe, criada por nós, lê arquivos .dot 
'''
class ArquivoDot:
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

		dot = ArquivoDot(dot_filename)
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

	def printar_tabela(self, tabela):

		teams_list = ["Vertice", "V Origem", "Custo"]
		data = [(v,d['origem'],d['peso'] if d['peso'] < sys.maxint else 'infinito') for v, d in tabela.items()]
		row_format ="{:>12}" * (len(teams_list) + 1)
		print(fundo_azul(vermelho_claro('\n                 Tabela de rotas                ')))
		print(fundo_cinza_claro(azul(row_format.format("", *teams_list))))
		for row in data:
			print(fundo_cinza_claro(amarelo(row_format.format("",*row))))

	def plotar_caminho(self, tabela, vinicial, vdestino):

		self.igraph.es["color"] = "gray"
		self.igraph.vs["color"] = "gray"

		self.igraph.vs[vinicial]["color"] = "red"
		self.igraph.vs[vdestino]["color"] = "red"

		def color_edge(graph, v1, v2):
			try:
				edges = graph.es.find(_from=v1,_to=v2)
				edges["color"] = "red"
			except ValueError:
				edges = graph.es.find(_within=[v1,v2])
				edges["color"] = "red"
			except ValueError:
				pass

		def print_path(graph, tabela, vdestino):
			if tabela[vdestino]['origem'] is not None:
				color_edge(graph, tabela[vdestino]['origem'], vdestino)
				print_path(graph, tabela, tabela[vdestino]['origem'])
				print(white(vdestino))
			else:
				print(white("Rota não disponível" if tabela[vdestino]['peso'] >= sys.maxint else vdestino))
			
		print(fundo_laranja(azul("\nTrajeto do vértice %d até o vértice %d:" % (vinicial, vdestino))))
		print_path(self.igraph, tabela, vdestino)
		self.plot()
