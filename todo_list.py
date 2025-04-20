import json
from datetime import datetime
filename = "C:/Users/hp/Desktop/dejiowoeye/Data Analysis/my_project/todo_list/todo_list.json"
def create_list ():
    """Creates a new to do list"""
    
    number_of_task = input("Number of tasks: ")
    try:
        number_of_task = int(number_of_task)
    except:
        print("Invalid format, enter integer e.g 1,2, etc")
    else: 
        with open (filename, "r") as f:
            todo_list = json.load(f)    
        i= 0

        while i < number_of_task:
            Time01 = input("Enter time in format(hhmm): ")
            Time01 = datetime.strptime(Time01, "%H%M")
            original_time = Time01.strftime("%H%M")
            task = input("Enter task: ")
           
            todo_list.update({original_time : task})
            i += 1
    
    with open (filename, "w") as f:
        json.dump(todo_list,f)
    print(f"your list is {todo_list}")

            
def delete_item():
    """Removes a specified item from the list"""
    print("Enter time in format(hhmm)")
    Time01 = input("what time will you delete: ")
    Time01 = datetime.strptime(Time01, "%H%M")
    original_time = Time01.strftime("%H%M")
    with open (filename, "r") as f:
        data = json.load(f)
    if original_time in data.keys():
        data.pop(original_time)
        with open (filename, "w") as f:
            json.dump(data, f)
        print(f"You deleted {original_time}, here is your new list {data}")
    else:
        print("item not found")

def modify_item():
    """Modifies an item in the list"""
    print("Enter time in format(hhmm): ")
    Time01 = input("which time will you modify: ")
    Time01 = datetime.strptime(Time01, "%H%M")
    original_time = Time01.strftime("%H%M")
    with open (filename, "r") as f:
        data = json.load(f)
    if original_time in data.keys():
        new_task= input("what is the new task: ")
        data[original_time] = new_task
        with open (filename, "w") as f:
            json.dump(data, f)
        print(f"the task {original_time} is changed to {new_task} ")
    else:
        print("item not found")
    

def view_item():
    """View an item in the list"""
    print("Enter time in format(hhmm)")
    Time01 = input("what time do you want to view: ")
    Time01 = datetime.strptime(Time01, "%H%M")
    original_time = Time01.strftime("%H%M")
    with open (filename, "r") as f:
        data = json.load(f)
    if original_time in data.keys()       :
        print(f"The task for {original_time} is {data[original_time]}")
    else:
        print("item not found")
def main():
    """Main function to initialize and manage the to-do application workflow."""
    print("Welcome to your to do list")
    print("To create a new list input: 'c' ")
    print("To modify an item in your list, input: 'm' ")
    print("To delete an item in your list, input: 'd' ")
    print("To view an item in your list, input: 'v' ")
    print("To quit, input: 'q' ")
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
        elif action == "q":
            break
        else:
            print("Invalid input")
main()  