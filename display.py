import networkx as nx
import matplotlib.pyplot as plt

def displaygraph(graph):
    
    
    # Create a directed graph (DiGraph) from the adjacency list
    G = nx.DiGraph()

    # Add edges to the graph
    for node, neighbors in graph.items():
        if not isinstance(neighbors, list):
            print(f"Error: Neighbors for node {node} should be a list.")
            return
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
