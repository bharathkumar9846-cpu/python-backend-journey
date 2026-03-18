class TaskManager:

    def __init__(self):
        self.tasks = []

    def add_task(self):
        name = input("Enter task: ")
        self.tasks.append({"task": name, "status": "pending"})
        print("Task added")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available")
            return

        for i, t in enumerate(self.tasks, start=1):
            print(f"{i}. {t['task']} - {t['status']}")

    def mark_done(self):
        if not self.tasks:
            print("No tasks to update")
            return

        self.view_tasks()
        try:
            num = int(input("Enter task number: "))
            if 1 <= num <= len(self.tasks):
                self.tasks[num - 1]["status"] = "done"
                print("Task marked as done")
            else:
                print("Invalid number")
        except:
            print("Invalid input")

    def delete_task(self):
        if not self.tasks:
            print("No tasks to delete")
            return

        self.view_tasks()
        try:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(self.tasks):
                self.tasks.pop(num - 1)
                print("Task deleted")
            else:
                print("Invalid number")
        except:
            print("Invalid input")

    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            for t in self.tasks:
                f.write(f"{t['task']},{t['status']}\n")
        print("Tasks saved")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                self.tasks = []
                for line in f:
                    task, status = line.strip().split(",")
                    self.tasks.append({"task": task, "status": status})
            print("Tasks loaded")
        except FileNotFoundError:
            print("No saved file found")


tm = TaskManager()

while True:
    print("\n1 : Add Task")
    print("2 : View Tasks")
    print("3 : Mark Task Done")
    print("4 : Delete Task")
    print("5 : Save Tasks")
    print("6 : Load Tasks")
    print("7 : Exit")

    try:
        choice = int(input("Enter choice: "))
    except:
        print("Invalid input")
        continue

    if choice == 1:
        tm.add_task()
    elif choice == 2:
        tm.view_tasks()
    elif choice == 3:
        tm.mark_done()
    elif choice == 4:
        tm.delete_task()
    elif choice == 5:
        tm.save_tasks()
    elif choice == 6:
        tm.load_tasks()
    elif choice == 7:
        print("Exiting...")
        break
    else:
        print("Invalid choice") 
        
        
