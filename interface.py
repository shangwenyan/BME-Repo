def interface():
    keep_running = True
    print("Blodd Test Analysis")
    while keep_running:
        print("Options:")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice == 9:
            keep_running = False
    return
   
interface()