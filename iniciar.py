# -*- coding: utf-8 -*-
from algoritmos import dijkstra, bellman_ford
from grafos import Grafo

while 1:
	filename = raw_input("Digite o nome do arquivo .dot (exemplo: g2.dot): ")
	try:
		grafo = Grafo(dot_filename=filename)
		break
	except:
		print "O arquivo '%s' não existe. Tente novamente" % filename

msg = lambda s : "Nó de %s [%s] " % (s,'|'.join(str(e) for e in grafo.vertices))
vertice_inicial = int(raw_input(msg('origem')))
vertice_destino=int(raw_input(msg('destino')))

algoritmo = None
while (algoritmo != '1' and algoritmo != '2'):

	algoritmo = raw_input("Qual algoritmo? 1=Dijkstra 2=Bellman Ford ")

	if algoritmo == '1':
		grafo = Grafo(dot_filename=filename)
		dijkstra(grafo=grafo,vertice_inicial=vertice_inicial,vertice_destino=vertice_destino)
	elif algoritmo == '2':
		grafo = Grafo(dot_filename=filename, directed=True)
		bellman_ford(grafo=grafo,vertice_inicial=vertice_inicial,vertice_destino=vertice_destino)