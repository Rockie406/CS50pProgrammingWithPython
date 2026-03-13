def main():
    history = []
    
    
    while True:    
        action = input("Actions: ")
        if action == "Undo":
            Undo = history.pop()
            print(f"Undo: {Undo}")
        elif action == "Restart":
            history.clear()
        
        else:
            history.append(action)
        print(history)
    
main()