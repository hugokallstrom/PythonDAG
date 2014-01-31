

class Vertex:
    def __init__(self,numVertices, weight):
        self.id = chr(numVertices + 97)
	self.weight = weight
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
	self.vertWeightList = {}
        self.numVertices = 0

    def add_vertex(self,weight):
        newVertex = Vertex(self.numVertices, weight)
	self.vertList[(newVertex.id, newVertex.weight)] = newVertex
	self.numVertices = self.numVertices + 1
        return newVertex.id

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,a,b,weight):
	
	for x, y in self.vertList:
		if x == a: 
			print "Hej"
		else:
			print "finns ej"
	for x, y in self.vertList:
		if x == b:
			print "Då"
		else:
			print "bajs"

#        self.vertList[a].addNeighbor(self.vertList[b], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
