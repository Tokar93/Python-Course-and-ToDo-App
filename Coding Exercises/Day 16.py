import FreeSimpleGUI as sg

text_feet = sg.Text('Enter feet:')
input_feet = sg.Input(key='feet')

text_inches = sg.Text('Enter inches:')
input_inches = sg.Input(key='inches')

convert = sg.Button('Convert')
result = sg.Text(key='output')

layout = [[text_feet, input_feet],
          [text_inches, input_inches],
          [convert, result]]

window = sg.Window('Convertor', layout=layout)

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Convert':
            feet = float(values['feet'])
            inches = float(values['inches'])
            meters = 0.3048 * feet + 0.0254 * inches
            window['output'].update(value=f'The result is: {meters}m')
            print(feet)

        case sg.WIN_CLOSED:
            break

window.read()
window.close()
