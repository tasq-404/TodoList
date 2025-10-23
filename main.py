# Main program loop that keeps running until user types 'exit'
while True:
    user_action = input("Type add, show, edit, complete, delete or exit: ")
    user_action = user_action.strip().lower()  # Normalize spacing and case

    # ------------------- ADD TASK -------------------
    if user_action.startswith("add"):
        # Extract task text after 'add ' and add newline for file formatting
        todo = user_action[4:] + "\n"

        # Read existing tasks from file
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        # Append new task to list
        todos.append(todo)

        # Write updated task list back to file
        with open("todos.txt", "w") as file:
            file.writelines(todos)

    # ------------------- SHOW TASKS -------------------
    elif user_action.startswith("show"):
        # Read all tasks from file
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        # If no tasks, show message
        if len(todos) == 0:
            print("No tasks in your list.")
        else:
            # Display all tasks with numbering
            for i, item in enumerate(todos):
                print(f"{i + 1}. {item.strip()}")

    # ------------------- EDIT TASK -------------------
    elif user_action.startswith("edit"):
        try:
            # Convert argument to integer index
            number = int(user_action[5:])

            # Load task list
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            # Ask user for updated task
            new_todo = input("Enter the new task: ") + "\n"

            # Replace target task
            todos[number - 1] = new_todo

            # Save updated list
            with open("todos.txt", "w") as file:
                file.writelines(todos)

            print("Task updated.")

        except (IndexError, ValueError):
            # Catch invalid index or non-numeric input
            print("Invalid task number.")

    # ------------------- COMPLETE TASK -------------------
    elif user_action.startswith("complete"):
        try:
            # Extract task number argument
            number = int(user_action.split()[1])

            # Read current tasks
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            # Remove completed task
            todos.pop(number - 1)

            # Save updated tasks
            with open("todos.txt", "w") as file:
                file.writelines(todos)

            print("Task completed.")

        except (IndexError, ValueError):
            print("Invalid task number.")

    # ------------------- DELETE TASK(S) -------------------
    elif user_action.startswith("delete"):
        # Load current tasks
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        # -- Delete all tasks --
        if user_action == "delete all":
            confirm = input("Are you sure you want to delete ALL tasks? (yes/no): ").lower()
            if confirm == "yes":
                todos.clear()  # Remove all tasks
                with open("todos.txt", "w") as file:
                    file.writelines(todos)
                print("All tasks deleted.")
            else:
                print("Delete all cancelled.")

        # -- Delete single task --
        else:
            try:
                number = int(user_action.split()[1])
                removed_task = todos.pop(number - 1).strip()

                # Write updated task list
                with open("todos.txt", "w") as file:
                    file.writelines(todos)

                print(f"Task '{removed_task}' deleted.")
            except (IndexError, ValueError):
                print("Invalid task number.")

    # ------------------- EXIT PROGRAM -------------------
    elif user_action.startswith("exit"):
        break  # End the loop and exit program

    # ------------------- INVALID COMMAND -------------------
    else:
        print("Invalid command. Try again.")

print("Bye!")  # Final message after exiting loop
