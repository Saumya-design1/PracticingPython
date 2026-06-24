# ToDo List 

tasks = []

def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added to the list.')

def show_tasks():
    if tasks:
        print("Tasks in the list:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("The list is empty.")

def remove_task(task_number):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f'Task "{removed_task}" removed from the list.')
    else:
        print("Invalid task number.")

add_task(input("Enter a task to add: "))

enter_choice = input("Do you want to add another task? (yes/no): ").strip().lower()
while enter_choice == 'yes':
    add_task(input("Enter a task to add: "))
    enter_choice = input("Do you want to add another task? (yes/no): ").strip().lower() 
else:
    show_tasks()
    remove_choice = input("Do you want to remove a task? (yes/no): ").strip().lower()
    if remove_choice == 'yes':
        task_number = int(input("Enter the task number to remove: "))
        remove_task(task_number)
        show_tasks()
    else:
        print("No tasks removed.")