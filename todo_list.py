todo_list = []
def create_list ():
    """this module help us create a to do list"""
    number_of_task = int(input("how many task do you want to enter: "))
    i= 0
    while i < number_of_task:
        time01 = input("Enter time in format(hhmm): ")
        task = input("Enter task: ")
        todo_list.append({time01: task})
        i += 1
    else:
        action = input("Enter required action or 'q' to quit")
    print(todo_list)

    

def delete_item():
    """this option deletes unwanted items from our list"""
    key = input("what time will should i delete: ")
    for i in range(0, len(todo_list)):
        if key in todo_list[i].keys():
            del todo_list[i]
            break
    print(todo_list)

def modify_item():
    """modify items in our list"""
    key = input("which item will you modify: ")
    new_task= input("what is the ney task: ")
    for i in range(0, len(todo_list)):
        if key in todo_list[i].keys():
            todo_list[i][key] = new_task   
    print(todo_list)

def view_item():
    """we will view items in our to do list """
    item = input("which item do you want to view: ")
    for i in range (0, len(todo_list)):
        if item in todo_list[i]:
            print(f"The task for {item} is {todo_list[i][item]}")
def list_management():
    """main function to run the todo app"""
    print("Welcome to your to do list")
    print("To create a new list input 'c' ")
    print("To modify an item in your list, input'm' ")
    print("To delete an item in your list, input'd' ")
    print("To view an item in your list, input'v' ")
    while True:
        action = input("Enter required action or 'q' to quit")
        if action == "c":
            create_list()
        elif action == "m":
            modify_item()
        elif action == "v":
            view_item()
        elif action == "d":
            delete_item()
list_management()