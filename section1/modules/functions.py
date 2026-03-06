def show_list(todos):
    if len(todos) == 0:
        print("No todos to show.")
    else:
        for i,item in enumerate(todos):
            item = item.strip('\n')
            print(f"{i+1}-{item}")

def get_todos(filepath='todos.txt'):
    """ Read a text file and return the list of to-do items."""
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos,filepath='todos.txt'):
    """ Write the to-do item list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos)  

if __name__ == "__main__":
    print("Hello! from function.py")
    print(get_todos())