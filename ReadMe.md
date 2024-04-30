# To-do List App
Command-line project that is capable of storing your tasks across different sessions into a database.



## Features

- Add/delete a task.
- Set due dates for tasks.
- Priority system for tasks.
- Display tasks sorted by due date & priority.
- Data persistence across sessions.





## Installation
Python needs a MySQL driver to access the MySQL database.

Also you should have [MySQL](https://dev.mysql.com/downloads/installer/) installed in your system.

Install the following library after cloning the repository:

```bash
  python -m pip install mysql-connector-python
```
And then 
`import mysql.connector`
## Run Locally

Clone the project

```bash
  https://github.com/Ameya29/Coding-Raja-Technologies-Internship
```

Go to the project directory

```bash
  cd Coding-Raja-Technologies-Internship
```

- Create a database named `todo_list` in your `MySQL` client
- Create a table named `mytasks` with the following columns and datatypes:
    - `task_id` -> `PRIMARY KEY` `SERIAL`
    - `task` -> `TEXT`
    - `due_date` -> `DATE`
    - `priority` -> `ENUM('High','Medium','Low') DEFAULT Medium`
    - `task_completed` -> `ENUM('Yes','No') DEFAULT No`

Run the project
```bash
    python todo_sql.py
```

## Screenshots

1. Add a task
[![Add-task.png](https://i.postimg.cc/cH7cGKDm/Add-task.png)](https://postimg.cc/ygdRFNCg)

2. Delete a task
[![Delete-task.png](https://i.postimg.cc/jjPHywrb/Delete-task.png)](https://postimg.cc/94XwhfM8)

3. Display empty to-do list
[![Display-Empty.png](https://i.postimg.cc/CLRfjBjQ/Display-Empty.png)](https://postimg.cc/gnPJp0tV)

4. Display by due-date
[![Display-by-date.png](https://i.postimg.cc/R0B65g2k/Display-by-date.png)](https://postimg.cc/CRcLbsh7)

5. Display by priority
[![Display-by-priority.png](https://i.postimg.cc/v8kmwPV0/Display-by-priority.png)](https://postimg.cc/dDRF8jnC)

6. Display tasks normally
[![Display-tasks.png](https://i.postimg.cc/PqXXQ9g5/Display-tasks.png)](https://postimg.cc/4Y0RJL4D)

7. Database image
[![Database-status1.png](https://i.postimg.cc/Y0WMSHWb/Database-status1.png)](https://postimg.cc/zH89d4pg)

8. Clear all tasks
[![All-tasks-cleared.png](https://i.postimg.cc/44DhQ4B4/All-tasks-cleared.png)](https://postimg.cc/G9j2cCW6)

9. Quit
[![Quit.png](https://i.postimg.cc/1z3g385B/Quit.png)](https://postimg.cc/BjRZhQFP)




## Author

- [@Ameya](https://github.com/Ameya29)

