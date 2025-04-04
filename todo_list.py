from datetime import datetime  
todo_list = []
def create_list ():
    """this module help us create a to do list"""
    number_of_task = int(input("how many task do you want to enter: "))
    i= 0
    while i < number_of_task:
        time01 = input("Enter time in format(hhmm): ")
        time01 = datetime.strptime(time01, "%H%M")
        orig_time = time01.strftime("%H:%M")
        task = input("Enter task: ")
        todo_list.append({orig_time : task})
        i += 1
    else:
        action = input("Enter required action or 'q' to quit")
    print(f"Here is a your list {todo_list}")

    

def delete_item():
    """this option deletes unwanted items from our list"""
    key = input("what time will should i delete: ")
    time01 = datetime.strptime(key, "%H%M")
    orig_time = time01.strftime("%H:%M")
    for i in range(0, len(todo_list)):
        if orig_time in todo_list[i].keys():
            del todo_list[i]
            break
    print(f"You deleted {orig_time}, here is your new list {todo_list}")

def modify_item():
    """modify items in our list"""
    key = input("which item will you modify: ")
    time01 = datetime.strptime(key, "%H%M")
    orig_time = time01.strftime("%H:%M")
    new_task= input("what is the ney task: ")
    for i in range(0, len(todo_list)):
        if orig_time in todo_list[i].keys():
            todo_list[i][orig_time] = new_task   
    print(f"the task {orig_time} is changed to {todo_list[i][orig_time]} ")

def view_item():
    """we will view items in our to do list """
    key = input("which item do you want to view: ")
    time01 = datetime.strptime(key, "%H%M")
    orig_time = time01.strftime("%H:%M")
    for i in range (0, len(todo_list)):
        if orig_time in todo_list[i]:
            print(f"The task for {orig_time} is {todo_list[i][orig_time]}")
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