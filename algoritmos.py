# -*- coding: utf-8 -*-
import sys
from grafos import Grafo

#Explicação: https://www.youtube.com/watch?v=aJ_2c9NVCIc&t=15s
def dijkstra(grafo, vertice_inicial, vertice_destino):
	tabela = {int(i) : {'peso':sys.maxint, 'origem':None} for i in grafo.igraph.vs.indices} #Inicia a tabela com infinito
	vertices_nao_visitados = grafo.igraph.vs.indices #Inicia a lista de vértices não visitados
	vertices_visitados = []
	vertice_sob_analise = vertice_inicial #Primeiro vértice sob análise é o vértice inicial
	tabela.update({vertice_inicial: {'peso':0, 'origem':None}}) #Inicia a tabela do primeiro vértice com 0

	while len(vertices_nao_visitados) > 0: #O loop vai continuar até que o processo tenha sido finalizado

		vertices_visitados.append(vertice_sob_analise)
		vertices_nao_visitados.remove(vertice_sob_analise)

		for vertice in vertices_nao_visitados:
			try:
				peso = grafo.igraph.es.find(_within=[vertice_sob_analise,vertice])['weight']
				if tabela[vertice_sob_analise]['peso'] + peso <= tabela[vertice]['peso']:
					tabela.update({vertice: {'peso': tabela[vertice_sob_analise]['peso'] + peso, 'origem': vertice_sob_analise}})
			except ValueError:
				pass

		#Escolhe o próximo vértice sob análise
		min = sys.maxint
		for vertice in vertices_nao_visitados:
			if tabela[vertice]['peso'] <= min:
				min = tabela[vertice]['peso']
				vertice_sob_analise = vertice

	grafo.printar_tabela(tabela)
	grafo.plotar_caminho(tabela, vertice_inicial, vertice_destino)


#Explicação: https://www.youtube.com/watch?v=vEztwiTELWs
def bellman_ford(grafo, vertice_inicial, vertice_destino):
	tabela = {int(i) : {'peso':sys.maxint, 'origem':None} for i in grafo.igraph.vs.indices} #Inicia a tabela com infinito
	tabela.update({vertice_inicial: {'peso':0, 'origem':None}}) #Inicia a tabela do primeiro vértice com 0
	arestas = grafo.igraph.get_edgelist()
	for i in range(0,len(grafo.igraph.vs.indices) - 1):
		for aresta in arestas:
			try:
				peso = grafo.igraph.es.find(_from=aresta[0],_to=aresta[1])['weight']
				if tabela[aresta[0]]['peso'] + peso < tabela[aresta[1]]['peso']:
					tabela.update({aresta[1]: {'peso': tabela[aresta[0]]['peso'] + peso, 'origem': aresta[0]}})
			except ValueError:
				pass
		#relaxamento
		for aresta in arestas:
			try:
				peso = grafo.igraph.es.find(_from=aresta[0],_to=aresta[1])['weight']
				if tabela[aresta[0]]['peso'] + peso < tabela[aresta[1]]['peso']:
					tabela.update({aresta[1]: {'peso': tabela[aresta[0]]['peso'] + peso, 'origem': aresta[0]}})
			except ValueError:
				pass

	grafo.printar_tabela(tabela)
	grafo.plotar_caminho(tabela, vertice_inicial, vertice_destino)

def rpf():
	pass

def spanning_tree():
	pass

