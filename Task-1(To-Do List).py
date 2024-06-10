tasks = []

def add_task(task):
  tasks.append(task)
  print("Task added successfully!")

def display_tasks():
  if not tasks:
    print("Your to-do list is empty.")
  else:
    print("Your To-Do List:")
    for idx, task in enumerate(tasks, start=1):
      print(f"{idx}. {task}")

def update_task(index, new_task):
  if 1 <= index <= len(tasks):
    tasks[index - 1] = new_task
    print("Task updated successfully!")
  else:
    print("Invalid task index. No task updated.")

def delete_task(index):
  if 1 <= index <= len(tasks):
    del tasks[index - 1]
    print("Task deleted successfully!")
  else:
    print("Invalid task index. No task deleted.")

while True:
  print("\n1. Add Task")
  print("2. Display Tasks")
  print("3. Update Task")
  print("4. Delete Task")
  print("5. Exit")
  choice = input("Enter your choice: ")
  if choice == '1':
    task = input("Enter task: ")
    add_task(task)
  elif choice == '2':
    display_tasks()
  elif choice == '3':
    try:
      index = int(input("Enter task index to update: "))
      new_task = input("Enter new task: ")
      update_task(index, new_task)
    except ValueError:
      print("Invalid input. Please enter a valid integer.")
  elif choice == '4':
    try:
      index = int(input("Enter task index to delete: "))
      delete_task(index)
    except ValueError:
      print("Invalid input. Please enter a valid integer.")
  elif choice == '5':
    print("Exiting...")
    break
  else:
    print("Invalid choice. Please enter a number between 1 and 5.")
