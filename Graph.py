# -*- coding: utf-8 -*-

class Vertex:
	def __init__(self,numVertices, weight):
		self.id = chr(numVertices + 97)
		self.weight = weight
		self.connectedTo = []

	def addNeighbor(self,nbr,weight):
		newEdge = Edge(self,nbr,weight)
		self.connectedTo.append(newEdge)
	
	def removeNeighbor(self, nbr):
		for e in self.connectedTo:
			if e.end == nbr:
				connectedTo.remove(e) 		

	def isNeighbor(self,nbr):
		for e in self.connectedTo:
			if e.end == nbr:
				return True
			else:
				return False

	def connectedWith(self,x):
		try:
			if self.connectedTo[x] is not None:
				return True
		except KeyError:
			return False
		
	def __str__(self):
		return str(self.id) + ' connectedTo: ' + str([x.end.id for x in self.connectedTo])

class Edge:
	def __init__(self,a,b, weight):
		self.weight = weight
		self.start = a
		self.end = b


class Graph:
	def __init__(self):
		self.vertList = {}
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
		if a and b in self.vertList.keys():
			self.vertList[a].addNeighbor(self.vertList[b],w)

	def getVertices(self):
		return self.vertList.keys()

	def removeEdge(self, a, b):
		if a and b in self.vertList.keys():
			self.vertList[a].removeNeighbor(self.vertList[b])

	def topologicalOrdering(self):
		g = self.vertList.copy()
		sorted = []
		noIncEdges = []
		add = True
		for v in self.vertList:
			for w in self.vertList:
				if self.vertList[w].isNeighbor(self.vertList[v]):
					add = False
				 
			if add:	
				noIncEdges.append(self.vertList[v])
		#print str([x.id for x in noIncEdges])		
		while noIncEdges:
			sorted.append(noIncEdges.pop())
			vertex = sorted[-1]
			for v in g:
				if vertex.isNeighbor(v):
					print g.getVertex(vertex)
					g.removeEdge(vertex, v)
					print g.getVertex(vertex)
					
					
			
					
			





	  
			