tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task(index):
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        print(f"Removed task: {removed}")
    else:
        print("Invalid task number")

if __name__ == "__main__":
    print("Simple To-Do App")
    add_task("Learn Git")
    add_task("Learn Docker")
    view_tasks()
    delete_task(1)
    view_tasks()
