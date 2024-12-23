from clearscreen import clear_screen
import time

def remove(graph):
       
    removenode = input("Which node would you like to remove?\n").strip().lower()
    clear_screen()
    while removenode not in graph:
           removenode = input("Node not in graph. Give another node\n").strip().lower()
           time.sleep(2)
           clear_screen()
    del graph[removenode]  
    print(f"{removenode} deleted successfully.") 
    time.sleep(2)