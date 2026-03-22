import datetime

tasks = []

def add_task():
    name = input("Enter task name: ")
    date = input("Enter deadline (YYYY-MM-DD): ")
    tasks.append({"name": name, "deadline": date})
    print("Task added!\n")

def show_tasks():
    if not tasks:
        print("No tasks available\n")
        return
    
    print("\nYour Tasks:")
    for task in tasks:
        print(f"{task['name']} - Due: {task['deadline']}")
    print()

def check_reminders():
    today = datetime.date.today()
    
    for task in tasks:
        deadline = datetime.datetime.strptime(task["deadline"], "%Y-%m-%d").date()
        days_left = (deadline - today).days
        
        if days_left == 1:
            print(f"Reminder: '{task['name']}' is due tomorrow!")
        elif days_left == 0:
            print(f"Reminder: '{task['name']}' is due today!")
        elif days_left < 0:
            print(f"Missed: '{task['name']}' deadline passed!")

def menu():
    while True:
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Check Reminders")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            check_reminders()
        elif choice == "4":
            break
        else:
            print("Invalid choice\n")

menu()