# Importing necessary modules
import os
import pickle


# Function to display the menu
def display_menu():
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Save and Quit")


# Function to load existing tasks from a file
def load_tasks():
    if os.path.exists("tasks.pkl"):
        with open("tasks.pkl", "rb") as file:
            tasks = pickle.load(file)
    else:
        tasks = []
    return tasks


# Function to save tasks to a file
def save_tasks(tasks):
    with open("tasks.pkl", "wb") as file:
        pickle.dump(tasks, file)


# Function to display tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['task']} - {'Done' if task['done'] else 'Pending'}")


# Function to add a new task
def add_task(tasks, new_task):
    tasks.append({'task': new_task, 'done': False})
    print("Task added successfully!")


# Function to mark a task as done
def mark_task_done(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]['done'] = True
        print("Task marked as done!")
    else:
        print("Invalid task index.")


# Main function to run the application
def main():
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            new_task = input("Enter the new task: ")
            add_task(tasks, new_task)
        elif choice == '3':
            display_tasks(tasks)
            task_index = int(input("Enter the task number to mark as done: "))
            mark_task_done(tasks, task_index)
        elif choice == '4':
            save_tasks(tasks)
            print("To-Do List saved. Exiting.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
