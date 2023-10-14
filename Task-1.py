import json

# Initialize the list of tasks
tasks = []

# Load tasks from a file if it exists
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks.extend(json.load(file))
    except FileNotFoundError:
        pass

# Save tasks to a file
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Function to add a task
def add_task(title, description):
    task_id = len(tasks) + 1
    task = {"id": task_id, "title": title, "description": description, "completed": False}
    tasks.append(task)
    print(f"Task {task_id} added.")

# Function to list tasks
def list_tasks():
    print("Tasks:")
    for task in tasks:
        status = "Done" if task["completed"] else "Not Done"
        print(f"{task['id']}. {task['title']} - {task['description']} - {status}")

# Function to mark a task as complete/incomplete
def mark_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            print(f"Task {task_id} marked as {'Done' if task['completed'] else 'Not Done'}.")
            break
    else:
        print("Task not found.")

# Function to delete a task
def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print(f"Task {task_id} deleted.")
            break
    else:
        print("Task not found.")
load_tasks()

while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Complete/Incomplete")
    print("4. Delete Task")
    print("5. Save Tasks")
    print("6. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter the task title: ")
        description = input("Enter the task description: ")
        add_task(title, description)
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        task_id = int(input("Enter the task ID to mark as complete/incomplete: "))
        mark_task(task_id)
    elif choice == "4":
        task_id = int(input("Enter the task ID to delete: "))
        delete_task(task_id)
    elif choice == "5":
        save_tasks()
        print("Tasks saved.")
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")

save_tasks()
print("Goodbye!")
