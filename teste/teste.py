import PySimpleGUI as sg

layout = [[sg.Text('My one-shot window.')],
          [[sg.Text('Digite seu nome: ')], [sg.InputText()]],
          [[sg.Text('Digite sua idade: ')], [sg.InputText()]],
          [sg.Submit(), sg.Cancel()]]

window = sg.Window('Window Title', layout)

event, values = window.read()
print(event)
print(values)
window.close()

text_input = values[0]
sg.popup('You entered', text_input)