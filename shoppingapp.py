

def greeting(): 
    print("----------------------------------------")
    print("--------------Shopping List-------------")
    print("----------------------------------------")

def instructions():
    print("Instructions:")
    print(" - Use [q] at anytime to quit and print your list")
    print(" - Use [a] to add items")
    print(" - Use [r] to remove items")
    print(" - Use [v] to view your list progress")
    print(" - Use [i] to see these instructions again")


your_list = [] 

def shopping_add(): 
    while True:
        items = input("What item would you like to add? (Use [b] to go back) ").strip()
        if items == "b":
            break
        else:
            your_list.append(items)

def shopping_remove(): 
    while True: 
        items = input("Which items would you like to remove? (Use [b] to go back) ").strip()
        if items == "b": 
            break
        else: 
            try: 
                your_list.remove(items)
            except ValueError: 
                print("That's not on your list, silly. ") 
                

def shopping_view_list(): 
    for items in your_list:
        print(f"-{items}")
    

def shopping_main():
    greeting()
    instructions()
    while True:
        cue = input("What would you like to do? ").lower().strip() 
        if cue == "q" and not your_list:
            print("See ya!") 
            break
        elif cue == "q" and your_list:
            print("\nHere's your list!\n")
            for items in your_list:
                print(f"-{items}")
            print("\nSee ya!")
            break    
        elif cue == "a": 
            shopping_add()
        elif cue == "r": 
            shopping_remove()
        elif cue == "v": 
            shopping_view_list()
        elif cue =="i": 
            instructions()
        else: 
            print("I didn't get that command. Press [i] to repeat instructions. ")

shopping_main()
