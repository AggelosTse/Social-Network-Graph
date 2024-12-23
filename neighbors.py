from clearscreen import clear_screen
        
def findneighbors(graph):
    usernode = input("Enter the node you want to find its neighbors:\n")
    clear_screen()
    if usernode in graph:
        print(graph[usernode])
    else:
        print("Error occurred, node is not in the graph.")   