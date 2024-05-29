import functions as func
import time

now = time.strftime('%b %d, %Y %H:%M:%S')
print('It is', now)

while True:
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = func.get_todos()

        todos.append(todo + '\n')

        func.write_todos(todos)
    elif user_action.startswith('show'):
        todos = func.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f'{index+1}-{item}'
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])

            number = number - 1

            todos = func.get_todos()

            new_todo = input('Enter new todo: ')
            old_todo = todos[number]
            todos[number] = new_todo + '\n'
            func.write_todos(todos)
            print(f'The ToDo "{old_todo.strip("\n")}" was replaced by "{new_todo}"')
        except ValueError:
            print('Your command is invalid. Put a number of todo')
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            index = number - 1
            todos = func.get_todos()
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            func.write_todos(todos)
            message = f'ToDo {todo_to_remove} was removed from the list'
            print(message)
        except IndexError:
            print('There si no item with this number')
    elif user_action.startswith('exit'):
        break
    else:
        print('Command is not valid')
print('Bye!')
