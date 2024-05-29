import FreeSimpleGUI as sg

sg.theme('LightBlue2')

text_feet = sg.Text('Enter feet:')
input_feet = sg.Input(key='feet')

text_inches = sg.Text('Enter inches:')
input_inches = sg.Input(key='inches')

convert = sg.Button('Convert')
result = sg.Text(key='output')

exit_button = sg.Button('Exit')

layout = [[text_feet, input_feet],
          [text_inches, input_inches],
          [convert, exit_button, result]]

window = sg.Window('Convertor', layout=layout)

while True:
    event, values = window.read()
    match event:
        case 'Convert':
            try:
                feet = float(values['feet'])
                inches = float(values['inches'])
                meters = 0.3048 * feet + 0.0254 * inches
                meters = round(meters, 3)
                window['output'].update(value=f'The result is: {meters}m')
                print(feet)
            except ValueError:
                sg.popup('Please enter the numbers!')
        case sg.WIN_CLOSED:
            break
        case 'Exit':
            break

