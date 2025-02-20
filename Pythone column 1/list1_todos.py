#Empty to do list
todo_list=[]

#Function to  add the task
def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added.")

#Function to remove a task
def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Task '{task}' removed.")
    else:
        print(f"Task '{task}' not found.")

#Function to display all tasks
def display_tasks():
    print("To-Do List:")
    for task in todo_list:
        print(f"-{task}")

#Adding tasks
add_task("Play with Princess")
add_task("Play with Lukas")
add_task("Go for a Walk")
add_task("Update READ_ME for Dance Finder")
add_task("Write some Code")

#Displaying tasks
display_tasks()

#Removing a task
remove_task("Go for a Walk")

#Displaying tasks again
display_tasks()
