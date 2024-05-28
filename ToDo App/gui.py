import functions as func
import FreeSimpleGUI as sg
import time

sg.theme('DarkTeal6')

clock = sg.Text('', key='clock')
label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip='Enter todo', key='todo')

add_button = sg.Button(key='Add',
                       image_source='add.png',
                       image_size=(95,25),
                       tooltip=' Add a new ToDo ',
                       mouseover_colors='LightBlue2')

list_box = sg.Listbox(values=func.get_todos(), key='todos',
                      enable_events=True, size=(45, 10))
edit_button = sg.Button(key='Edit',
                        image_source='edit.png',
                        image_size=(95,25),
                        tooltip=' Edit ToDo ',
                        mouseover_colors='LightBlue2')

complete_button = sg.Button(key='Complete',
                            image_source='complete.png',
                            image_size=(95,25),
                            tooltip=' Complete ToDo ',
                            mouseover_colors='LightBlue2')
exit_button = sg.Button('Exit')

left_column_content = [[clock],
                       [label],
                       [input_box],
                       [list_box],
                       [exit_button]]
right_column_content = [[add_button],
                        [edit_button],
                        [complete_button]]
left_column = sg.Column(left_column_content)
right_column = sg.Column(right_column_content)

window = sg.Window('My To-Do App',
                   layout=[[left_column, right_column]],
                   font=('Helvetica', 15))

while True:
    event, values = window.read(timeout=200)
    if event == sg.WIN_CLOSED:
        break
    window['clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
    match event:
        case 'Add':
            if values['todo'] == '':
                sg.popup('The text is empty. Please write a todo.', font=("Helvetica", 15))
            else:
                todos = func.get_todos()
                new_todo = values['todo'] + '\n'
                todos.append(new_todo)
                func.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
        case 'Edit':
            try:
                todos = func.get_todos()
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                func.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup('Please select an item first.', font=("Helvetica", 15))
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = func.get_todos()
                todos.remove(todo_to_complete)
                func.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup('Please select an item first.', font=("Helvetica", 15))
        case 'Exit':
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0].strip('\n'))
        case sg.WIN_CLOSED:
            break

