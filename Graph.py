# -*- coding: utf-8 -*-
import copy

class Vertex:
	def __init__(self,numVertices, weight):
		self.id = chr(numVertices + 97)
		self.weight = weight
		self.incEdges = []
		self.outEdges = []

	def addNeighbor(self,nbr,dir):
		if dir > 0:
			self.incEdges.append(nbr)
		else:
			self.outEdges.append(nbr)
	
	def removeNeighbor(self, nbr, dir):
		if dir > 0:
			self.incEdges.remove(nbr)
		else:
			self.outEdges.remove(nbr)

	def isNeighbor(self,nbr):
		if nbr in self.outEdges:
			return True
		else:
			return False

	def hasIncEdges(self):
		if self.incEdges:
			return True
		else:
			return False

	def hasOutEdges(self):
		if self.outEdges:
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
		return str(self.id) + ' has incoming edges to ' + str([x.id for x in self.incEdges]) + ' has outgoing edges to ' + str([x.id for x in self.outEdges])

class Edge:
	def __init__(self,a,b,weight):
		self.weight = weight
		self.start = a
		self.end = b

class Graph:
	def __init__(self):
		self.vertList = {}
		self.edgeList = []
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
			newEdge = Edge(a,b,w)
			self.edgeList.append(newEdge)
			self.vertList[a].addNeighbor(self.vertList[b], 0)
                        self.vertList[b].addNeighbor(self.vertList[a], 1)

	def getVertices(self):
		return self.vertList.keys()

	def removeEdge(self, a, b):
		if a and b in self.vertList.keys():
			self.vertList[a].removeNeighbor(self.vertList[b],0)
			self.vertList[b].removeNeighbor(self.vertList[a],1)

	def getEdgeWeight(self, a, b):
		if a and b in self.vertList.keys():
			for e in self.edgeList:
				if e.start == a and e.end == b:
					return e.weight
			return 0

	def topologicalOrdering(self):
		g = copy.deepcopy(self.vertList)
		sortedList = []
		noIncEdges = []
		for vertex in g.keys():
			if not g[vertex].hasIncEdges():
				noIncEdges.append(g[vertex])
				del g[vertex]
		while noIncEdges:
			vertex = noIncEdges.pop()
			sortedList.append(self.vertList[vertex.id])
			for nextVertex in g.keys():
				if vertex.isNeighbor(g[nextVertex]):
					vertex.removeNeighbor(g[nextVertex],0)
					g[nextVertex].removeNeighbor(vertex,1)
					if not g[nextVertex].hasIncEdges():
						noIncEdges.append(g[nextVertex])
						del g[nextVertex]
		return sortedList
	
	def weightOfLongestPath(self,a,b):
		sortedList = self.topologicalOrdering()
		weightedList = {}
		pathList = []
		for v in sortedList:
			if v.id == a:
				pathList.append(v)
		notFull = True
		while notFull:
			added = False
			for v in pathList:
				for w in v.outEdges:
					if w not in pathList:
						pathList.append(w)
						added = True
			if not added:
				notFull = False
		ok = False
		for v in pathList:
			if v.id == b:
				ok = True
		if not ok:	
			print a, " can't reach ", b 
		else:
			for v in pathList:
				weight = 0
				for w in v.incEdges:
					if w in pathList:
						if weight < (weightedList[w.id] + self.getEdgeWeight(w.id,v.id)):
							weight = weightedList[w.id] + self.getEdgeWeight(w.id, v.id)
				weight += v.weight
				weightedList[v.id] = weight
			#goal = b
			#path = []
			#path.insert(0, goal)
			#while goal != a:
			#	for v in self.vertList[goal].incEdges:
			#		if v in pathList:
			#			if (weightedList[self.vertList[goal].id] - (self.vertList[goal].weight + self.getEdgeWeight(v.id, goal))) == weightedList[v.id]:
			#				goal = v.id
			#				path.insert(0, goal)
			goal = self.vertList[b]
			path = []
			path.insert(0, goal)
			while goal.id != a:
				for v in goal.incEdges:
					if v in pathList:
						if weightedList[goal.id] - (goal.weight + self.getEdgeWeight(v.id, goal.id)) == weightedList[v.id]:
							goal = v
							path.insert(0, goal)
			weight = 0
			for v in path:
				if v != path[-1]:
					weight += v.weight + self.getEdgeWeight(v.id, path[path.index(v)+1].id)
				else:
					weight += v.weight
			print str([x.id for x in path]), " with weight ", weight


