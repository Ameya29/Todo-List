todo_list = []

def add_task(task):
    todo_list.append(task)
    show_tasks()

def delete_task(task_num):
    if len(todo_list) == 0:
        print("\nNothing to delete!")
    else:
        todo_list.pop(task_num)
        show_tasks()

def show_tasks():
    if len(todo_list) == 0:
        print("\nTo Do List is empty!")
    else:
        print("\nYour tasks to do are: ")
        count = 1
        for x in todo_list:
            print(str(count)+". "+x)
            count = count + 1

def clear_list():
    del todo_list[:]
    print("\nYour list cleared!")

if __name__ == '__main__':
    while True:
        print("\nTODO Menu: \n1. Add a task \n2. Delete a task \n3. Show tasks to do \n4. Clear current todo list \n5. Quit")

        choice = int(input("\nEnter Your Choice: "))
        match choice:
            case 1:
                task = input("\nEnter your task to do: ")
                add_task(task)
            case 2:
                task_num = int(input("\nEnter task number: "))
                delete_task(task_num-1)
            case 3:
                show_tasks()
            case 4:
                clear_list()
            case 5: 
                print("Thanks for using the todo list app")
                break
            case _:
                print("\nInvalid input!")







