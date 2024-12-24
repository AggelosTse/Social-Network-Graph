from clearscreen import clear_screen
from display import displaygraph
from addnode import add
from removenode import remove
from neighbors import findneighbors
from menu import printmenu
import time

        
graph = {}      #initialize graph as a dictionary
while True:
   clear_screen()
   
   answer = printmenu()     #user gives a answer and depending on it it calls the right functions.
   if answer == "1":
       displaygraph(graph)  #displays the graph on the screen
   elif answer == "2":
       add(graph)           #adds nodes on the graph
   elif answer == "3":
       if graph == {}:     
              print("You cant remove nodes. Graph is empty.\n")     #removes nodes from the graph (if the graph is empty it prints error message)
              time.sleep(2)
       else:
              remove(graph)            
   elif answer == "4":
       findneighbors(graph)     #prints all the neighbor's from a specific node.
   elif answer == "5":
       with open("test.txt", "a") as myfile:        #saves it in a txt file
           myfile.write(str(graph) + "\n")
   else:
       print("Program terminated.")
       break
