import json
import os
from datetime import datetime

FILENAME = "C:/Users/hp/Desktop/dejiowoeye/Data Analysis/my_project/todo_list/todo_list.json"

def load_todo_list():
    """Load the to-do list from the JSON file."""
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return {}

def save_todo_list(todo_list):
    """Save the to-do list to the JSON file."""
    with open(FILENAME, "w") as f:
        json.dump(todo_list, f, indent=4)

def get_valid_time():
    """Prompt the user for a valid time in hh:mm format."""
    while True:
        Time01 = input("Enter time in format (hh:mm): ")
        try:
            Time01 = datetime.strptime(Time01, "%H:%M")
            original_time = Time01.strftime("%H:%M")
            return original_time
        except ValueError:
            print("Invalid time format. Please enter in hh:mm format.")

def create_list():
    """Creates a new to-do list"""
    todo_list = load_todo_list()
    while True:
        try:
            number_of_tasks = int(input("Number of tasks: "))
            if number_of_tasks < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid format, enter a non-negative integer e.g 1, 2, etc")

    for _ in range(number_of_tasks):
        time = get_valid_time()
        task = input("Enter task: ").strip()
        if task:
            todo_list[time] = task
        else:
            print("Task cannot be empty. Please enter a valid task.")

    save_todo_list(todo_list)
    print("Your list is:")
    for time, task in todo_list.items():
        print(f"Time: {time}, Task: {task}")

def delete_item():
    """Removes a specified item from the list"""
    todo_list = load_todo_list()
    key = get_valid_time()
    if key in todo_list:
        del todo_list[key]
        save_todo_list(todo_list)
        print(f"You deleted the task at {key}. Here is your new list:")
        for time, task in todo_list.items():
            print(f"Time: {time}, Task: {task}")
    else:
        print("Item not found")

def modify_item():
    """Modifies an item in the list"""
    todo_list = load_todo_list()
    key = get_valid_time()
    if key in todo_list:
        new_task = input("What is the new task: ").strip()
        if new_task:
            todo_list[key] = new_task
            save_todo_list(todo_list)
            print(f"The task at {key} is changed to {new_task}")
        else:
            print("New task cannot be empty.")
    else:
        print("Item not found")

def view_item():
    """View an item in the list"""
    todo_list = load_todo_list()
    key = get_valid_time()
    if key in todo_list:
        print(f"The task for {key} is {todo_list[key]}")
    else:
        print("Item not found")

def main():
    """Main function to initialize and manage the to-do application workflow."""
    print("Welcome to your to-do list")
    print("To create a new list input: 'c'")
    print("To modify an item in your list, input: 'm'")
    print("To delete an item in your list, input: 'd'")
    print("To view an item in your list, input: 'v'")
    print("To quit, input: 'q'")
    actions = {
        'c': create_list,
        'm': modify_item,
        'd': delete_item,
        'v': view_item
    }
    while True:
        action = input("Enter required action or 'q' to quit: ").strip().lower()
        if action in actions:
            actions[action]()
        elif action == 'q':
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()