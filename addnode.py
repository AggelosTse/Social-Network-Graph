from clearscreen import clear_screen

def add(graph):
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
                       graph[nodename].append(newnode)
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