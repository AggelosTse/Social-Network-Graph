import networkx as nx
import matplotlib.pyplot as plt
from clearscreen import clear_screen
from display import displaygraph
from addnode import add
from removenode import remove
from neighbors import findneighbors
from menu import printmenu
import time

        
# Initialize the graph as an adjacency list
graph = {}
while True:
   clear_screen()
   
   answer = printmenu() 
   if answer == "1":
       displaygraph(graph)
   elif answer == "2":
       add(graph)      
   elif answer == "3":
       if graph == {}:
              print("You cant remove nodes. Graph is empty.\n")
              time.sleep(2)
       else:
              remove(graph)            
   elif answer == "4":
       findneighbors(graph)    
   elif answer == "5":
       with open("test.txt", "a") as myfile:
           myfile.write(str(graph) + "\n")
   else:
       print("Program terminated.")
       break
