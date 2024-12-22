import networkx as nx
import matplotlib.pyplot as plt
# Initialize the graph as an adjacency list
graph = {}
while True:
    
   print("1. Display the graph")
   print("2. Add a node to the graph")
   print("3. Remove a node from the graph")
   print("4. Save Graph in txt file")
   print("5. Terminate program")
   
   answer = input("Give a number (1-4)\n")
   while answer != "1" and answer != "2" and answer != "3" and answer != "4" and answer != "5":
       answer = input("Error occured. Try again\n")
   
    
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
                    break  # Exit the loop if the user types "no"
                
                # Ensure the node is in the graph
                if nodename not in graph:
                    graph[nodename] = []
                
                # Ask if the user wants to connect with other nodes
                answer1 = input("Do you want to connect with other nodes? (yes/no)\n").strip().lower()
                
                # Handle valid input for "yes" or "no"
                while answer1 not in ["yes", "no"]:
                    answer1 = input("Error occurred, please try again: \n").strip().lower()

                # If they want to connect
                if answer1 == "yes":
                    while True:
                        print(f"Give a node to connect with {nodename}: \n")
                        newnode = input().strip()

                        # Add the connection to the graph
                        if nodename in graph:
                            graph[nodename].append(newnode)
                        else:
                            graph[nodename] = [newnode]

                        # Ask if the user wants to continue adding connections
                        answer1 = input("Do you want to connect with another node? (yes/no)\n").strip().lower()
                        while answer1 != "yes" and answer1 != "no":
                            answer1 = input("Error occurred, please try again: \n").strip().lower()
                        
                        if answer1 == "no":
                            break  # Exit inner connection loop if the user answers "no"
                an = input("Do you want to add another node? (yes/no) \n").strip().lower()
                if(an == "no"): break
                    
   elif answer == "3":
            removenode = input("Which node would you like to remove?").strip().lower()
            while removenode not in graph:
                       removenode = input("Node not in graph. Give another node").strip().lower()
            del graph[removenode]
    
   elif answer == "4":
      with open("test.txt", "a") as myfile:
        myfile.write(str(graph) + "\n")
        
        
   else:
       break