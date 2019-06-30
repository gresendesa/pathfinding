# -*- coding: utf-8 -*-
import re

'''
Esta classe, criada por nós, lê arquivos .dot e os transforma em um objeto
'''
class RegexDot:


	def __init__(self, filename):
		file_content = f=open(filename, "r").read()
		lines = re.findall(r'.+ -> .+ \[label=.+\]',file_content)
		vertices = []
		edges = []
		for line in lines:
			peaces = re.findall(r'(.+) -> (.*) \[label=(.*)\]',re.sub(r'[\n\t]','',line))
			vertices.extend([int(peaces[0][0]),int(peaces[0][1])])
			vertices = list(set(vertices))
			edges.append({"edge":(int(peaces[0][0]),int(peaces[0][1])), "label":float(peaces[0][2])})

		self.vertices = vertices
		self.edges = edges