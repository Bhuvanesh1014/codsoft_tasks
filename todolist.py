import os

TASKS_FILE = "todo_data.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 4:
                    tasks.append({
                        "status": parts[0],
                        "description": parts[1],
                        "deadline": parts[2],
                        "priority": parts[3]
                    })
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            line = f"{task['status']}|{task['description']}|{task['deadline']}|{task['priority']}\n"
            f.write(line)

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\n--- Your Tasks ---")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['status']} {task['description']} | Due: {task['deadline']} | Priority: {task['priority']}")

def add_task(tasks):
    desc = input("Enter task description: ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    priority = input("Enter priority (High/Medium/Low): ")
    tasks.append({
        "status": "[Not Done]",
        "description": desc,
        "deadline": deadline,
        "priority": priority.capitalize()
    })
    save_tasks(tasks)
    print("Task added!")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        idx = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["status"] = "[Done]"
            save_tasks(tasks)
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a valid number.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        idx = int(input("Enter task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            tasks.pop(idx)
            save_tasks(tasks)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Menu")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting To-Do List App.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
