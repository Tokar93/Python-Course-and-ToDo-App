def get_todos(filename='todos.txt'):
    """Read a text file and return the
    list of to-do items.
    """
    with open(filename, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filename='todos.txt'):
    with open(filename, 'w') as file:
        file.writelines(todos_arg)
