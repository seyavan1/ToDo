tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added: ", task)

def view_tasks():
    for i, task in enumerate(tasks):
        print(i + 1, task)

def delete_task(index):
    index -= 1
    del tasks[index]
    print("Task deleted at index: ", index + 1)

while True:
    print("Enter 1 to add task")
    print("Enter 2 to view tasks")
    print("Enter 3 to delete task")
    print("Enter 4 to exit")

    choice = int(input())

    if choice == 1:
        task = input("Enter task: ")
        add_task(task)
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        index = int(input("Enter index of task to delete: "))
        delete_task(index)
    elif choice == 4:
        break
    else:
        print("Invalid choice")
