import networkx as nx
import matplotlib.pyplot as plt

def displaygraph(graph):
    
    
    
    G = nx.DiGraph()        #initializes an empty graph from nx library

    # Add edges to the graph
    for node, neighbors in graph.items():       
        for neighbor in neighbors:
            G.add_edge(node, neighbor)          #updates the graph and adds edges on every node in the adjucency list

    # Draw the graph
    plt.figure(figsize=(6, 6))                  #displays the graph
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
