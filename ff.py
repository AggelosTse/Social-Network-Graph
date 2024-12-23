import networkx as nx
import matplotlib.pyplot as plt
import os
import platform


def clear_screen():
    system_name = platform.system()
    if system_name == "Windows":
        os.system("cls")
    else:
        os.system("clear")
        
# Initialize the graph as an adjacency list
graph = {}
while True:
    
   print("1. Display the graph")
   print("2. Add a node to the graph")
   print("3. Remove a node from the graph")
   print("4. Display any node's neighbors")
   print("5. Save Graph in txt file")
   print("6. Terminate program\n")
   
   answer = input("Give a number (1-4)\n")
   while answer not in ["1","2","3","4","5","6"]:
       clear_screen()
       answer = input("Error occured. Try again\n")
   
   clear_screen()
   if answer == "1":
            # Create a directed graph (DiGraph) from the adjacency list
            G = nx.DiGraph()
            
            # Add edges to the graph
            for node, neighbors in graph.items():
                for neighbor in neighbors:
                    G.add_edge(node, neighbor)
            
            # Draw the graph
            plt.figure(figsize=(6, 6))
            nx.draw(
                G, 
                with_labels=True, 
                node_color='lightblue', 
                node_size=4000, 
                arrowstyle='->', 
                arrowsize=20, 
                font_size=15
            )
            plt.title("Graph Visualization")
            plt.show()
        
   elif answer == "2":
            
            while True:
                print("Enter node name: (Enter no to stop)\n")
                nodename = input().strip().lower()
                
                if nodename == "no":
                    clear_screen()
                    break  # Exit the loop if the user types "no"
                clear_screen()
                # Ensure the node is in the graph
                if nodename not in graph:
                    graph[nodename] = []
                
                # Ask if the user wants to connect with other nodes
                answer1 = input("Do you want to connect with other nodes? (yes/no)\n").strip().lower()
                
                # Handle valid input for "yes" or "no"
                while answer1 not in ["yes", "no"]:
                    clear_screen()
                    answer1 = input("Error occurred, please try again: \n").strip().lower()
                clear_screen()
                # If they want to connect
                if answer1 == "yes":
                    while True:
                        print(f"Give a node to connect with {nodename}: \n")
                        newnode = input().strip()
                        clear_screen()
                        # Add the connection to the graph
                        if nodename in graph:
                            graph[nodename].append(newnode)     #paei sto dictionary tou graph, kai opou dei to nodename: [], prosthetei to newnode stin lista, diladi: nodename: [newnode]
                        else:
                            graph[nodename] = [newnode]

                        # Ask if the user wants to continue adding connections
                        answer1 = input("Do you want to connect with another node? (yes/no)\n").strip().lower()
                        while answer1 != "yes" and answer1 != "no":
                            clear_screen()
                            answer1 = input("Error occurred, please try again: \n").strip().lower()
                        clear_screen()
                        if answer1 == "no":
                            break  # Exit inner connection loop if the user answers "no"
                an = input("Do you want to add another node? (yes/no) \n").strip().lower()
                clear_screen()
                if(an == "no"): break
                    
   elif answer == "3":
            removenode = input("Which node would you like to remove?").strip().lower()
            while removenode not in graph:
                       removenode = input("Node not in graph. Give another node").strip().lower()
            del graph[removenode]
    
   elif answer == "4":
       usernode = input(("Enter the node you want to find its neighbors:\n"))
       clear_screen()
       if usernode in graph:
           print(graph[usernode])
       else:
           print("Error orccured, node is not in the graph.")
        
        
   elif answer == "5":
       with open("test.txt", "a") as myfile:
        myfile.write(str(graph) + "\n")
        
   else:
       print("Program terminated.")
       break