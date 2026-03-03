
todo_list = []

def show_list(todos):
    if len(todos) == 0:
        print("No todos to show.")
    else:
        for i,item in enumerate(todos):
            item = item.strip('\n')
            print(f"{i+1}-{item}")

def get_todos(filepath='todos.txt'):
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos,filepath='todos.txt'):
    with open(filepath, 'w') as file:
        file.writelines(todos)   

while True:
    #Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete, clean or exit:").strip()
    
    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        
        todo_list = get_todos()
        todo_list.append(todo)

        write_todos(todo_list)   

    elif user_action.startswith("show") or user_action.startswith("display"):
        todo_list = get_todos()

        show_list(todo_list)

    elif user_action.startswith("edit"):
        try:
            todo_list = get_todos()
            show_list(todo_list)

            change_num = int(input("Choice a number to edit:")) -1

            if change_num < len(todo_list):
                new_todo = input("Enter a new todo:")
                todo_list[change_num] = new_todo + '\n'

            write_todos(todo_list)  
            show_list(todo_list)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("clean"):
        todo_list.clear()
        write_todos(todo_list)  

    elif user_action.startswith("complete") or user_action.startswith("c"):
        todo_list = get_todos()
        
        while True:
            show_list(todo_list)

            try:   
                delete_num = int(input("Choose a number to remove:"))
                

                removed_todo = todo_list[delete_num - 1].strip('\n')
                print(f"{removed_todo} was removed from the list.")
                todo_list.pop(delete_num - 1)
                write_todos(todo_list)  

                
                order = input("Choose continue or end:")
                if order.lower() == "end":
                    break
            except IndexError:
                print("There is no item with that number.")
            # except ValueError:
            #     print("Your command is not valid.")

    elif user_action.startswith("exit"):
        break

    #_ = whatever value that is not matched with the above cases
    else:
        print("hey, you entered an unknown command")

print("Bye!")


