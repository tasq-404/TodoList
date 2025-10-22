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
                
                with open("todos.txt", "r") as file:
                    todos = file.readlines()

                print("Current Tasks:")
                for i, item in enumerate(todos):
                    item = item.strip("\n")
                    print(i + 1,". ",item,sep="")

                new_todo = input("Enter the new task: ")
                todos[number] = new_todo + "\n"

                print("Task updated. New Tasks:")
                for i, item in enumerate(todos):
                    item = item.strip("\n")
                    print(i + 1,". ",item,sep="")


            except IndexError:
                print("Invalid number — no such task exists.")
            except ValueError:
                print("Please enter a valid number.")
            
        case "complete":
            number = int(input("Enter the number of the task to complete: "))
            
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todos.pop(number - 1)
            print("Task completed. Updated Tasks:")
            for i, item in enumerate(todos):
                item = item.strip("\n")
                print(i + 1,". ",item,sep="")

            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case "delete":
            print("Current Tasks:")
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            
            for i, item in enumerate(todos):
                item = item.strip("\n")
                print(i + 1,". ",item,sep="")

            number = int(input("Enter the number of the task to delete: "))
            
            todos.pop(number - 1)

            print("Task deleted. Updated Tasks:")
            for i, item in enumerate(todos):
                item = item.strip("\n")
                print(i + 1,". ",item,sep="")

            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case "exit":
            break
        case _:
            print("Invalid input, try again.")

print("Bye!")