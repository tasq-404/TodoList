todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip().lower()

    match user_action:
        case "add":
            todo = input("Enter a task: ")
            todos.append(todo)
        case "show":
            for i, item in enumerate(todos): # enumerate function
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

        case "exit":
            break
        case _:
            print("Invalid input, try again.")

print("Bye!")