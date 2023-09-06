import csv

# Initialize an empty list to store tasks
tasks = []

# TODO: Function to add a task to the list

# TODO: Function to remove a task from the list

# TODO: Function to list all tasks

# TODO: Function to load tasks from a CSV file
# Function to load tasks from a CSV file
def load_tasks(filename):
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                # TODO: Append each task to the 'tasks' list
                pass
        print(f"Tasks loaded from '{filename}'.")
    except FileNotFoundError:
        print(f"'{filename}' not found. Starting with an empty task list.")

# Function to save tasks to a CSV file
def save_tasks(filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for task in tasks:
            # TODO: Write each task to the CSV file
            pass
        print(f"Tasks saved to '{filename}'.")

# Load tasks from a CSV file when the program starts
load_tasks("tasks.csv")

# Main program loop
while True:
    print("\nTodo List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. List Tasks")
    print("4. Save and Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        task = input("Enter the task: ")
        # TODO: Call the add_task function here
    elif choice == "2":
        task = input("Enter the task to remove: ")
        # TODO: Call the remove_task function here
    elif choice == "3":
        # TODO: Call the list_tasks function here
        pass
    elif choice == "4":
        # TODO: Call the save_tasks function here
        print("Exiting the application.")
        break
    else:
        print("Invalid choice. Please try again.")
