import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="todo_list"
)
# print(mydb)

cursor = mydb.cursor()
# cursor.execute("CREATE DATABASE todo_list;")
# print(cursor.execute("SHOW TABLES;"))

if __name__ == '__main__':
    while True:
        print("\nTODO Menu: \n1. Add a task \n2. Delete a task \n3. Show tasks to do \n4. Clear current todo list \n5. Quit")

        choice = int(input("\nEnter Your Choice: "))
        match choice:
            case 1:
                try:
                    task = input("Enter task description: ")
                    due_date = input("Enter due date in DD-MM-YYYY format: ")
                    due_date = datetime.strptime(due_date, '%d-%m-%Y').strftime('%Y-%m-%d')
                    priority = input("Enter priority (High, Medium, Low): ")
                    sql = "INSERT INTO mytasks(task, due_date, priority) VALUES (%s, %s, %s)"
                    val = (task, due_date, priority)
                    cursor.execute(sql, val)
                    mydb.commit()

                    print("Task added successfully!")
                except Exception as e:
                    print("An error occurred {}".format(e))
            case 2:
                try:
                    task_id = int(input("Enter task number to delete: "))
                    sql = "DELETE FROM mytasks WHERE task_id=%s"
                    val = (task_id, )
                    cursor.execute(sql, val)
                    mydb.commit()

                    sql_update = "UPDATE mytasks SET task_id = task_id - 1 WHERE task_id > %s"
                    val_update = (task_id, )
                    cursor.execute(sql_update, val_update)
                    mydb.commit()

                    print("Task deleted and task IDs updated!")
                except Exception as e:
                    print("An error occurred {}".format(e))
            case 3:
                cursor.execute("SELECT COUNT(*) FROM mytasks;")
                row_count = cursor.fetchone()[0]
                if row_count == 0:
                    print("No tasks to do hurray!!")
                else:
                    print("Sort by: \n1. Date \n2. Priority \n3. Normal")
                    option = int(input("Option number: "))
                    match option:
                        case 1:
                            cursor.execute("SELECT * FROM mytasks ORDER BY due_date ASC;")
                            tasks = cursor.fetchall()
                            # print(tasks)
                            print("\nYour Tasks: \n---------------------------------------------------------")
                            for task in tasks:
                                due_date_formatted = task[2].strftime('%d-%m-%Y')
                                print("Task {}: {} \nDue: {} \nPriority: {} \n".format(task[0], task[1], due_date_formatted, task[3]))

                        case 2:
                            cursor.execute("SELECT * FROM mytasks ORDER BY FIELD(priority, 'HIGH', 'MEDIUM', 'LOW');")
                            tasks = cursor.fetchall()
                            # print(tasks)
                            print("\nYour Tasks: \n---------------------------------------------------------")
                            for task in tasks:
                                due_date_formatted = task[2].strftime('%d-%m-%Y')
                                print("Task {}: {} \nDue: {} \nPriority: {} \n".format(task[0], task[1], due_date_formatted, task[3]))

                        case 3:
                            cursor.execute("SELECT * FROM mytasks;")
                            tasks = cursor.fetchall()
                            # print(tasks)
                            print("\nYour Tasks: \n---------------------------------------------------------")
                            for task in tasks:
                                due_date_formatted = task[2].strftime('%d-%m-%Y')
                                print("Task {}: {} \nDue: {} \nPriority: {} \n".format(task[0], task[1], due_date_formatted, task[3]))
                        
                        case _:
                            print("Invalid input!")
            case 4:
                try:
                    sql = "TRUNCATE TABLE mytasks;"
                    cursor.execute(sql)
                    mydb.commit()

                    print("All tasks cleared!")
                except Exception as e:
                    print("An error occurred {}".format(e))
            case 5: 
                print("Thanks for using the todo list app")
                cursor.close()
                mydb.close()
                break
            case _:
                print("\nInvalid input!")

