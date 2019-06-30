from igraph import *

inf = 2000000

def legrafo(ndg):
	ndg = ndg + ".dot"
	arq = open(ndg,'r')
	ca =  arq.read()
	ng = ca.split()
	x = len(ng)
	z = 0
	A = "A"
	nv = 0
	vnos1 = []
	vnos2 = []
	vv = []
	vpesos = []
	c1 = '->'
	c2 = '='
	while(z < x):
		if(ng[z] == c1):
			vnos1 += (ng[z-1])
			vnos2 += (ng[z+1])
		if(ng[z] == c2):
			vpesos += (ng[z+1])
		z += 1
	g = Graph()
	print(vpesos[0])
	z = 0
	if(len(vnos1) != len(vpesos)):
		print("ta tudo errado essa merda")

	
	m1 = max(vnos1, key = int)
	m2 = max(vnos2, key = int)

	if(m1>m2):
		nv = m1
	elif(m1 == m2):
		nv = m1
	elif(m2>m1):
		nv = m2

	g.add_vertices(nv)

	while(z <= len(vnos2)):
		g.add_edges(int(vnos1[z]),int(vnos2[z]))
		g.es['peso'] += vpesos[z]
		g.es['name'] += (A)
		A = A+1
		z += 1
	return g

def dijkstra(grafo):
	i = 0;
	j = len(grafo.vs['label'])
	while(i<j):
		if(i==0):
			grafo.es['label'][i] = 0

		grafo.es['label'][i] = 1000000000 		#estimativa de infinito 
		i= i+1;
	
	print(g.es['peso'][0])

g = Graph()

g.add_vertices(5)
g.add_edges([(0,1), (1,2), (2,3), (1,3), (0,3)])

g.vs["name"] = ["A", "B", "C", "D"]
g.es["peso"] = [4,2,2,10,1]


g.vs["label"] = g.vs["name"]
g.es["label"] = g.es["peso"]

layout = g.layout("kk")

print (g)

print("_________________________________")

dijkstra(g)


plot(g,layout = layout )


nome = raw_input("Nome do Grafo que Deseja ler: ")

f = legrafo(nome)
