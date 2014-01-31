# -*- coding: utf-8 -*-
import Graph

# Main function calling the GUI 
def main():
	gui()

# Lets the user control the program via the text bases GUI
def gui():
	g = Graph.Graph()
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
			print "Lägger till kant"
		elif(input == '4'):
			print g.getVertices()
                elif(input == '5'):
			print "Visar connections"
                elif(input == '6'):    
			print_menu()
		elif(input == '7'):
			break;

# Prints the menu
def print_menu():
	print "Options"
        print "1. Help" 
        print "2. Add node" 
        print "3. Add edge" 
	print "4. Display nodes"
        print "5. Display connections"
	print "6. Display menu"     
        print "7. Quit program"

# Create an empty graph
def create_graph():
	return Graph.Graph()

# Run main
main()