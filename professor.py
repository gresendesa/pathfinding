# -*- coding: utf-8 -*-

from igraph import Graph, plot

from parser import RegexDot

#cria o objeto Graph (o grafo)
g = Graph()

dot = RegexDot("g1.dot")

edges = [v["edge"] for v in dot.edges]
weights = [v["label"] for v in dot.edges]
vertices = dot.vertices
print weights

g.add_vertices(len(vertices)) #adiciona 4 vértices ao grafo (índices 0 a 3)
g.add_edges(edges) #adiciona 4 arestas ao grafo (índices de 0 a 3)

g.vs["name"] = ['v%d' % v for v in vertices]
g.es["weight"] = weights #atribui peso às arestas

#mostrando o grafo na tela

g.vs["label"] = g.vs["name"] #rotula os vértices com seus respectivos nomes
g.es["label"] = g.es["weight"] #rotula as arestas com seus respectivos pesos

layout = g.layout("kk") #atribui um layout para plotagem do grafo

print g #imprime o grafo na linha de comando

plot(g,layout = layout) #apresenta o grafo usando interface gráfica