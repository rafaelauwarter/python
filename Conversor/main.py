from turtle import title
import PySimpleGUI as sg

layout = [
    [sg.Text('Texto', enable_events= True, key = '-txt_1-'),sg.Spin(['item 1', 'item 2'])],
    [sg.Button('Botão', key = '-btn_1-')],
    [sg.Input(key = '-INPUT_1-')],
    [sg.Text('Mais uma'), sg.Button('OK')],
    [sg.Button('Sair')]
]
window = sg.Window('Conversor', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED  or event == 'Sair':
        break

    if event == '-btn_1-':
        # print(values['-INPUT_1-'])
        # window['-txt_1-'].update(values['-INPUT_1-'])
        window['-txt_1-'].update(visible = False)

    if event == 'OK':
        print('Botão OK pressionado')

    if event == '-txt_1-':
        print('alguma coisa')
    
    # if event == 'Sair':
    #     break

window.close()