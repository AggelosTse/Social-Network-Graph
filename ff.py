import networkx as nx
import matplotlib.pyplot as plt

# Initialize the graph as an adjacency list
graph = {}

while True:
    print("Thes na emfanistei o grafos? (yes/no/exit)")
    apantisi = input().strip().lower()
    
    if apantisi == "yes":
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
            node_size=2000, 
            arrowstyle='->', 
            arrowsize=20, 
            font_size=15
        )
        plt.title("Graph Visualization")
        plt.show()
    
    elif apantisi == "no":
        print("Dose to username sou:")
        username = input().strip()
        
        # Ensure the username is in the graph
        if username not in graph:
            graph[username] = []
        
        print("Thes na sindetheis me kombous? (yes/no)")
        while input().strip().lower() == "yes":
            print(f"Dose kombo gia {username}:")
            kombos = input().strip()
            
            # Append the new connection
            graph = {
                username : [kombos]
            }
        
    elif apantisi == "exit":
        print("Program terminated.")
        break

    else:
        print("Mi egkiros apantisi. Parakalw dose 'yes', 'no', i 'exit'.")
