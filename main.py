# -*- coding: utf-8 -*-
import Graph

# Main function calling the GUI 
def main():
	gui()

# Lets the user control the program via the text bases GUI
def gui():
	g = Graph.Graph()
	#For test purpose
	a = g.add_vertex(4)
	b = g.add_vertex(5)
	c = g.add_vertex(3)
	d = g.add_vertex(2)
	e = g.add_vertex(7)
	g.addEdge(a,b,2)
	g.addEdge(a,c,2)
	g.addEdge(b,d,1)
	g.addEdge(c,d,1)
	g.addEdge(c,e,1)
	g.addEdge(d,e,3)
#	a = g.add_vertex(7)
#	b = g.add_vertex(5)
#	c = g.add_vertex(3)
#	d = g.add_vertex(11)
#	e = g.add_vertex(8)
#	f = g.add_vertex(2)
#	h = g.add_vertex(9)
#	i = g.add_vertex(10)
#	g.addEdge(a,d,1)
#	g.addEdge(a,e,1)
#	g.addEdge(b,d,1)
#	g.addEdge(c,e,1)
#	g.addEdge(c,i,1)
#	g.addEdge(d,f,1)
#	g.addEdge(d,h,1)
#	g.addEdge(d,i,1)
#	g.addEdge(e,h,1)
#	g.addEdge(h,i,5)
	print_menu()
	while True:
                input = raw_input("Input selection \n")
                
                if(input == '1'):
			print "Noob"
                elif(input == '2'):
			weight = raw_input("Choose a weight to the vertice \n")
                        v = g.add_vertex(weight)
			print "Vertex identifier: " + v
                elif(input == '3'):
			a = raw_input("Choose first vertice \n")
			b = raw_input("Choose second vertice \n")
			w = raw_input("Choose a weight for the edge \n")
			g.addEdge(a,b,w)
		elif(input == '4'):
			print g.getVertices()
                elif(input == '5'):
			n = raw_input("Choose vertice \n")
			print g.getVertex(n)
                elif(input == '6'):    
			print_menu()
		elif(input == '7'):
			break;
		elif(input == '8'):
			g.topologicalOrdering()
		elif(input == '9'):
			a = raw_input("Choose start vertice\n")
			b = raw_input("Choose end vertice\n")
			g.weightOfLongestPath(a,b)

# Prints the menu
def print_menu():
	print "Options"
        print "1. Help" 
        print "2. Add node" 
        print "3. Add edge" 
	print "4. Display vertices"
        print "5. Display connections"
	print "6. Display menu"     
        print "7. Quit program"
	print "8. Topological Ordering"
	print "9. Longest Path"

# Create an empty graph
def create_graph():
	return Graph.Graph()

# Run main
main()