from clearscreen import clear_screen


def printmenu():
    print("1. Display the graph")
    print("2. Add a node to the graph")
    print("3. Remove a node from the graph")
    print("4. Display any node's neighbors")
    print("5. Save Graph in txt file")
    print("6. Terminate program\n")
    
    answer = input("Give a number (1-4)\n")
    while answer not in ["1", "2", "3", "4", "5", "6"]:
        clear_screen()
        answer = input("Error occurred. Try again\n")
        
    clear_screen()
    return answer