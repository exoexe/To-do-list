import os
import json

TODO_FILE = "todo_list.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["completed"] else "✗"
        print(f"{i}. [{status}] {task['task']}")

def add_task(tasks):
    task_description = input("Enter the task description: ")
    tasks.append({"task": task_description, "completed": False})
    save_tasks(tasks)
    print("Task added successfully.")

def mark_task_completed(tasks):
    display_tasks(tasks)
    if not tasks:
        return
    try:
        task_number = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_number < len(tasks):
            tasks[task_number]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    display_tasks(tasks)
    if not tasks:
        return
    try:
        task_number = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_number < len(tasks):
            tasks.pop(task_number)
            save_tasks(tasks)
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Manager")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Mark task as completed")
        print("4. Delete a task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
