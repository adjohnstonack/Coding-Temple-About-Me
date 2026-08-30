# todo_manager.py
# A simple interactive to-do list manager

# Pre-populated list of tasks
tasks = ["Buy groceries", "Finish homework", "Call the dentist"]

def display_list():
    """Display the current to-do list with numbering."""
    print("\n========================================")
    print("             My To-Do List")
    print("========================================")
    
    # Numbered list starting from 1
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    
    print(f"\nTotal tasks: {len(tasks)}\n")


while True:
    # Show the current list
    display_list()

    # Menu options
    print("What would you like to do?")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Exit")

    choice = input("\nChoice: ")

    # ADD A TASK
    if choice == "1":
        new_task = input("Enter new task: ")
        tasks.append(new_task)  # append() to add
        print("\nUpdated list:")
        display_list()

    # REMOVE A TASK
    elif choice == "2":
        try:
            task_num = int(input("Enter the task number to remove: "))
            # Convert 1-based user input to 0-based index
            removed = tasks.pop(task_num - 1)
            print(f"\nRemoved: {removed}")
            print("\nUpdated list:")
            display_list()
        except (ValueError, IndexError):
            print("\nInvalid task number. Please try again.\n")

    # EXIT PROGRAM
    elif choice == "3":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice. Please enter 1, 2, or 3.\n")