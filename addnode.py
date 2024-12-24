from clearscreen import clear_screen

def add(graph):
    while True:
           print("Enter node name: (Enter no to stop)\n")
           nodename = input().strip().lower()                      #asks for nodes to add repeatedly until the user enters "no"

           if nodename == "no":
               clear_screen()
               break  
           clear_screen()
           
           if nodename not in graph:           #if the node isnt in the dictionary, it initializes its list of neighbors
               graph[nodename] = []

           # Asks repeatedly if the user wants to connect with other nodes until user types no
           answer1 = input("Do you want to connect with other nodes? (yes/no)\n").strip().lower()

           while answer1 not in ["yes", "no"]:
               clear_screen()
               answer1 = input("Error occurred, please try again: \n").strip().lower()
           clear_screen()
           if answer1 == "yes":
               while True:
                   print(f"Give a node to connect with {nodename}: \n")
                   newnode = input().strip()
                   clear_screen()
                   if nodename in graph:
                       graph[nodename].append(newnode)      #adds the new node in the list of neighbors of the nodename in the dictionary
                   else:
                       graph[nodename] = [newnode]

                   answer1 = input("Do you want to connect with another node? (yes/no)\n").strip().lower()      
                   while answer1 != "yes" and answer1 != "no":
                       clear_screen()
                       answer1 = input("Error occurred, please try again: \n").strip().lower()
                   clear_screen()
                   if answer1 == "no":
                       break  # Exit inner connection loop if the user answers "no"
           an = input("Do you want to add another node? (yes/no) \n").strip().lower()
           clear_screen()
           if an == "no":
               break