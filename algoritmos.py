# -*- coding: utf-8 -*-
import sys
from pprint import pprint
from grafos import Grafo

#Explicação: https://www.youtube.com/watch?v=aJ_2c9NVCIc&t=15s
def dijkstra(dot, vertice_inicial, vertice_destino):
	tabela = {int(i) : {'weight':sys.maxint, 'origem':None} for i in dot.grafo.vs.indices} #Inicia a tabela com infinito
	vertices_nao_visitados = dot.grafo.vs.indices #Inicia a lista de vértices não visitados
	vertices_visitados = []
	vertice_sob_analise = vertice_inicial #Primeiro vértice sob análise é o vértice inicial
	tabela.update({vertice_inicial: {'weight':0, 'origem':vertice_inicial}}) #Inicia a tabela do primeiro vértice com 0

	while len(vertices_nao_visitados) > 0: #O loop vai continuar até que o processo tenha sido finalizado

		#print "__ Nó sob análise: %d" % vertice_sob_analise
		#print "Nó %d adicionado à lista de visitados e removido da lista de não visitados" % vertice_sob_analise
		vertices_visitados.append(vertice_sob_analise)
		vertices_nao_visitados.remove(vertice_sob_analise)
		#print "Vertices visitados %s" % ', '.join(str(e) for e in vertices_visitados)
		#print "Vertices não visitados %s" % ', '.join(str(e) for e in vertices_nao_visitados)

		for vertice in vertices_nao_visitados:
			try:
				weight = dot.grafo.es.find(_within=[vertice_sob_analise,vertice])['weight']
				#print "Aresta (%d %d) %d < %f?" % (vertice_sob_analise, vertice,tabela[vertice_sob_analise]['weight'] + weight,tabela[vertice]['weight'])
				if tabela[vertice_sob_analise]['weight'] + weight < tabela[vertice]['weight']:
					tabela.update({vertice: {'weight': tabela[vertice_sob_analise]['weight'] + weight, 'origem': vertice_sob_analise}})
			except ValueError:
				#print "Aresta (%d %d) não encontrada" % (vertice_sob_analise, vertice)
				pass


		#print tabela
		#Escolhe o próximo vértice sob análise
		min = sys.maxint
		for vertice in vertices_nao_visitados:
			if tabela[vertice]['weight'] <= min:
				min = tabela[vertice]['weight']
				vertice_sob_analise = vertice
		#print "Próximo vértice escolhido: %d" % vertice_sob_analise
	pprint(tabela)

def bellman_ford():
	pass

def rpf():
	pass

def spanning_tree():
	pass

dot = Grafo("g1.dot")
msg = lambda s : "Nó de %s [%s] " % (s,'|'.join(str(e) for e in dot.vertices))
dijkstra(dot=dot,vertice_inicial=int(input(msg('origem'))),vertice_destino=int(input(msg('destino'))))