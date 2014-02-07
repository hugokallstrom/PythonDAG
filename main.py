# -*- coding: utf-8 -*-
import Graph

# Main function calling the GUI 
def main():
	gui()

# Lets the user control the program via the text bases GUI
def gui():
	g = Graph.Graph()
	#For test purpose
	a = g.add_vertex(2)
	b = g.add_vertex(4)
	g.addEdge(a,b,6)
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
	print "8. TEST"

# Create an empty graph
def create_graph():
	return Graph.Graph()

# Run main
main()