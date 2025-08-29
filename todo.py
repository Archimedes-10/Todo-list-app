# todo.py

# Step 1: Start with an empty list to hold tasks
tasks = []

# Step 2: Add a task
def add_task(task):
    tasks.append(task)

# Step 3: View tasks
def view_tasks():
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
# Step 4: Delete a task

#def delete_task2(index):
    #tasks.pop(index)
    #print(f"Deleted: {tasks}")
    
def delete_task(index):
    finished_task = input("Is task complete? y or n")
    if finished_task == "y":
        task_number = input("what task did you finish")
        tasks.pop(int(task_number))
        print("Finished Task: " + task_number)




# Step 5: Mark task complete


# Step 6: Save/load tasks (extra stretch for today)


# Demo flow (you can run this file directly: python todo.py)
if __name__ == "__main__":
    add_task("Finish Cyber 201 assignment")
    add_task("Push code to GitHub")
    add_task("Push to github")
    add_task("Test delete_task")
    view_tasks()
    delete_task(1)
    #mark_complete(0)
    view_tasks()
    #save_tasks()