# -*- coding: utf-8 -*-

from igraph import Graph, plot

#cria o objeto Graph (o grafo)
g = Graph()

g.add_vertices(4) #adiciona 4 vértices ao grafo (índices 0 a 3)
g.add_edges([(0,1),(1,2),(0,2),(2,3)]) #adiciona 4 arestas ao grafo (índices de 0 a 3)

g.vs["name"] = ["v0","v1","v2","v3"] #atribui nomes aos vértices
g.es["weight"] = [1,2,3,4] #atribui peso às arestas


#mostrando o grafo na tela

g.vs["label"] = g.vs["name"] #rotula os vértices com seus respectivos nomes
g.es["label"] = g.es["weight"] #rotula as arestas com seus respectivos pesos

layout = g.layout("kk") #atribui um layout para plotagem do grafo

print g #imprime o grafo na linha de comando

plot(g,layout = layout) #apresenta o grafo usando interface gráfica