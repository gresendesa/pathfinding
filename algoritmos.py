# -*- coding: utf-8 -*-
import sys

from grafos import Grafo

def dijkstra(arquivo_dot, vertice_inicial):
	dot = Grafo(arquivo_dot)
	tabela = {int(i) : sys.maxint for i in dot.grafo.vs.indices} #Inicia a tabela com infinito
	vertices_nao_visitados = [dot.grafo.vs.indices] #Inicia a lista de vértices não visitados
	
	vertice_sob_analise = vertice_inicial #Primeiro vértice sob análise é o vértice inicial
	vertices_nao_visitados.remove(vertice_sob_analise) #Remove-se o vértice inicial da lista de vértices não visitados

	while not finalizado:

		for vertice in vertices_nao_visitados:
			vertices_visitados.append(vertice_sob_analise)


	for vertice_analisado in vertices_nao_visitados:
		for proximo_vertice in vertices_nao_visitados
	#print tabela

def bellman_ford():
	pass

def rpf():
	pass

def spanning_tree():
	pass


g = Grafo("g1.dot")

#g.plot()
#print g.grafo.vs.indices
#print len(g.grafo.es.select(_from=0))
#print len(g.grafo.es.select(_to=5))
#print g.grafo.es.select(_within=[2,4]) 

#print g.grafo.es.find(_from=1,_to=3) 

#dijkstra(arquivo_dot="g1.dot",vertice_inicial=0)