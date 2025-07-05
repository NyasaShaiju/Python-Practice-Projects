# todo_list.py

tasks = []

def show_menu():
    print("\nTo-Do List Menu")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Mark task as complete")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks):
            status = "DONE" if task["done"] else "NOT DONE"
            print(f"{i + 1}. {task['name']} - {status}")

def add_task():
    name = input("Enter task: ")
    tasks.append({"name": name, "done": False})
    print("Task added.")

def remove_task():
    view_tasks()
    try:
        idx = int(input("Enter task number to remove: ")) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            print(f"Removed task: {removed['name']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def complete_task():
    view_tasks()
    try:
        idx = int(input("Enter task number to mark as complete: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["done"] = True
            print(f"Marked '{tasks[idx]['name']}' as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        complete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
