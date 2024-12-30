todo_list = []

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Edit task")
    print("4. Delete task")
    print("5. Exit from Application")

def view_tasks():
    if not todo_list:
        print("Your to-do list is empty now please add tasks")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")

def add_task():
    task = input("Enter the task: ")
    todo_list.append(task)
    print(f"Task '{task}' added.")

def edit_task():
    view_tasks()
    task_number = int(input("Enter the task number to edit: ")) - 1
    if 0 <= task_number < len(todo_list):
        new_task = input("Enter the new task: ")
        todo_list[task_number] = new_task
        print("Task updated.")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    task_number = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_number < len(todo_list):
        deleted_task = todo_list.pop(task_number)
        print(f"Task '{deleted_task}' deleted.")
    else:
        print("Invalid task number.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            edit_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please Choose a number between 1 and 5.")

if __name__ == "__main__":
    main()

