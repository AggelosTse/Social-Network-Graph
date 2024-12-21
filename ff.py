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
            for neighbor, weight in neighbors.items():
                G.add_edge(node, neighbor, weight=weight)
        
        # Get edge weights and normalize for visualization
        edge_weights = nx.get_edge_attributes(G, 'weight')
        edge_thickness = [abs(weight) * 10 for weight in edge_weights.values()]  # Scale weights for thickness

        # Draw the graph
        plt.figure(figsize=(6, 6))
        pos = nx.spring_layout(G)  # Layout for better visualization
        nx.draw(
            G, 
            pos, 
            with_labels=True, 
            node_color='lightblue', 
            node_size=2000, 
            arrowstyle='->', 
            arrowsize=20, 
            font_size=15, 
            width=edge_thickness  # Set edge thickness
        )
        # Add edge labels (weights)
        nx.draw_networkx_edge_labels(
            G, pos, edge_labels=edge_weights, font_size=12
        )
        plt.title("Graph Visualization with Edge Weights")
        plt.show()
    
    if apantisi == "no":
        print("Dose to username sou:")
        username = input().strip()

        # Ensure the username is in the graph
        if username not in graph:
            graph[username] = {}

        print("Thes na sindetheis me kombous? (yes/no)")
        while input().strip().lower() == "yes":
            print(f"Dose kombo gia {username}:")
            kombos = input().strip()

            print(f"Dose varos gia tin akmi apo {username} pros {kombos}, times mono apo -1 ews 1:")
            try:
                weight = float(input())
                while weight <= -1 or weight >= 1:  # Ensures the weight is strictly between -1 and 1
                    print("Sfalma: To varos prepei na einai metaksy -1 kai 1 (oxi symperilamvanomeno).")
                    weight = float(input())
            except ValueError:
                print("To varos prepei na einai arithmos.")
                continue

            # Append the new connection
            graph[username][kombos] = weight
            print(f"Sindesi apo {username} pros {kombos} me varos {weight} prostethike.")

        print("Telos sindesewn.")
    elif apantisi == "exit":
        print("Program terminated.")
        break

    else:
        print("Mi egkiros apantisi. Parakalw dose 'yes', 'no', i 'exit'.")