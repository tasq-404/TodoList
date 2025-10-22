while True:
    user_action = input("Type add, show, edit, complete, delete or exit: ")
    user_action = user_action.strip().lower()

    match user_action:
        case "add":
            todo = input("Enter a task: ") + "\n"
            
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

            with open("todos.txt", "w") as file:
                file.writelines(todos)
            
        case "show":
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            
            for i, item in enumerate(todos): # enumerate function
                    item = item.strip("\n")
                    print(i + 1,". ",item,sep="")

        case "edit":
            try:
                number = int(input("Enter a number: "))
                number -= 1
                new_todo = input("Enter a new task: ")
                todos[number] = new_todo
            except IndexError:
                print("Invalid number — no such task exists.")
            except ValueError:
                print("Please enter a valid number.")
            
        case "complete":
            number = int(input("Enter the number of the task to complete: "))
            todos.pop(number - 1)

        case "delete:":
            number = int(input("Enter the number of the task to delete: "))
            todos.pop(number - 1)

        case "exit":
            break
        case _:
            print("Invalid input, try again.")

print("Bye!")