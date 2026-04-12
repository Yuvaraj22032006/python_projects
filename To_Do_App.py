import json

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    
    #Checks if the file is not found
    except FileNotFoundError:
        tasks = []

    # Checks if the file is empty
    except json.JSONDecoderError:
        tasks = []

    return tasks


tasks = load_tasks()


def toggle_task_status():
    print("Here are the tasks: ")
    print(view_tasks())

    user_input = input("Enter task number to mark as done: ").strip()
    if not user_input:
        print("Enter a valid index number.")
    
    else:
        try:
            mark_done = int(user_input)

            if 1 <= mark_done <= len(tasks):
                    
                #toggles to the opposite value, used only for boolean    
                tasks[mark_done - 1]["done"] = not tasks[mark_done - 1]["done"]

                print(f"Task has been marked {'done' if tasks[mark_done - 1]['done'] else 'Undone'}")

                save_tasks(tasks)

            else:
                print("Invalid task number.")

        except ValueError:
            print("Enter a valid location.")
        
        


def save_tasks(tasks):

    # writes the tasks into the json file, json.dump is used to rewrite the file
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def add_task():
    input_task = input("Enter a Task to add: ").strip()

    if not input_task:
        print("Input Cannot be empty. Please enter a valid task.")

    else:
        tasks.append({"task" : input_task, "done" : False})
        print(f"Task '{input_task}' added.")
        save_tasks(tasks) # Here we calling the save_tasks to save the tasks list
        print()

def view_tasks():

    if not tasks:
        return "No tasks to show."
    else:
        result = "Tasks:\n"
        # enumrate(tasks, start = 1), This built-in function takes the tasks iterable and adds a counter (index) to each item. 
        # The key part is start = 1, which tells the function to begin the counter at 1 instead of the default 0.
        for i, task in enumerate(tasks, start = 1):
            if task["done"] == False:
                symbol = "[ ]"
            else:
                symbol = "[✅]"
            result += f"{i}. {symbol} {task['task']}\n"
            
        return result
   
def delete_task():
    
    if not tasks:
        print("No tasks to delete.")
    else:
        print(view_tasks())

        # try ... except ValueError: This is a safety net. If the user types "apple" instead of a number, the int() function will fail.
        # Instead of the program crashing, it jumps to the bottom and prints "Please Enter a valid Number."
        # 1. Get input and .strip() it immediately to remove all spaces
        try:
            user_Input = input("What task to be removed: ").strip()

            # 1 <= remove_task: Checks if the number is at least 1 (since your list starts at 1, not 0 or a negative number).
            # remove_task <= len(tasks): Checks if the number is not higher than the total number of items you have.

            if not user_Input:
                print("Input Cannot be empty. Please enter a valid number.")

            else:

                remove_task = int(user_Input)

                if 1 <= remove_task <= len(tasks):
                    removed_task = tasks.pop(remove_task - 1)
                    print(f"Task has been removed: {removed_task}")
                    print("Updated task list: ")
                    print(view_tasks())
                    save_tasks(tasks)

                else:
                    print("Invalid Task Number.\n")
            
                print()
        
        except ValueError:
            print("Please Enter a valid Number.\n")
            
while True:
    print("1. Add Task.")
    print("2. Remove Task.")
    print("3. View Tasks.")
    print("4. Exit")
    print()

    try:
        choice = int(input("Enter the Choice: "))
    except ValueError:
        print("Invalid input. Enter a valid number.")
        continue

    if choice == 1:
        add_task()
        
    elif choice == 2:
        delete_task()
    
    elif choice == 3:
        print(view_tasks())

    elif choice == 4:
        break

    else:
        print("Invalid Input")