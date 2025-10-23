while True:
    user_action = input("Type add, show, edit, complete, delete or exit: ")
    user_action = user_action.strip().lower()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        with open("todos.txt", "r") as file:
            todos = file.readlines()
        todos.append(todo)
        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        with open("todos.txt", "r") as file:
            todos = file.readlines()
        if len(todos) == 0:
            print("No tasks in your list.")
        else:
            for i, item in enumerate(todos):
                print(f"{i + 1}. {item.strip()}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            new_todo = input("Enter the new task: ") + "\n"
            todos[number - 1] = new_todo
            with open("todos.txt", "w") as file:
                file.writelines(todos)
            print("Task updated.")
        except (IndexError, ValueError):
            print("Invalid task number.")

    elif user_action.startswith("complete"):
        try:
            number = int(user_action.split()[1])
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            todos.pop(number - 1)
            with open("todos.txt", "w") as file:
                file.writelines(todos)
            print("Task completed.")
        except (IndexError, ValueError):
            print("Invalid task number.")

    elif user_action.startswith("delete"):
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        # Check for delete all
        if user_action == "delete all":
            confirm = input("Are you sure you want to delete ALL tasks? (yes/no): ").lower()
            if confirm == "yes":
                todos.clear()
                with open("todos.txt", "w") as file:
                    file.writelines(todos)
                print("All tasks deleted.")
            else:
                print("Delete all cancelled.")
        else:
            # Normal delete
            try:
                number = int(user_action.split()[1])
                removed_task = todos.pop(number - 1).strip()
                with open("todos.txt", "w") as file:
                    file.writelines(todos)
                print(f"Task '{removed_task}' deleted.")
            except (IndexError, ValueError):
                print("Invalid task number.")

    elif user_action.startswith("exit"):
        break

    else:
        print("Invalid command. Try again.")

print("Bye!")
