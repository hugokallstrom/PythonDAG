# -*- coding: utf-8 -*-

class Vertex:
	def __init__(self,numVertices, weight):
		self.id = chr(numVertices + 97)
		self.weight = weight
		self.connectedTo = {}

	def addNeighbor(self,nbr,weight):
		self.connectedTo[nbr] = weight

	def __str__(self):
		return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

class Graph:
	def __init__(self):
		self.vertList = {}
		self.vertWeightList = {}
		self.numVertices = 0

	def add_vertex(self,weight):
		newVertex = Vertex(self.numVertices, weight)
		self.vertList[newVertex.id] = newVertex
		self.numVertices = self.numVertices + 1
		return newVertex.id

	def getVertex(self,n):
		if n in self.vertList:
			return self.vertList[n]
		else:
			return None

	def addEdge(self,a,b,w):
		if a and b in self.vertList:
			self.vertList[a].addNeighbor(self.vertList[b], w)

	def getVertices(self):
		return self.vertList.keys()

	def topologicalOrdering(self):
		sorted = []
		noIncEdges = []
		add = True
		for v in self.vertList:
			for w in self.vertList:
				if v in self.vertList[w].connectedTo:
					add = False
					print "hej"
			if add:	
				noIncEdges.append(v)
		print noIncEdges
	
