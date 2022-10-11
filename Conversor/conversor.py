from turtle import title
import PySimpleGUI as sg

# Muda a cor da janela
sg.theme('Black')

# cria um layout de quantas linhas vao ter na tela
layout = [
    [sg.Input(key = '-INPUT-'),sg.Spin(['Km para Milhas', 'Kg para Gramas', 'Minutos para segundos'], key = '-SPN_1-')],
    [sg.Text('---', key = '-TXT_1-')],
    [sg.Button('Converter', key = '-BTN_CONVERT-'),sg.Button('Sair')]
]

# cria a janela com o nome e o layout ja desenvolvido
window = sg.Window('Conversor', layout)

while True:
    event, values = window.read()

    # verifica se o evento esta para fechar a janela
    if event == sg.WIN_CLOSED  or event == 'Sair':
        break

    
    if event == '-BTN_CONVERT-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values['-SPN_1-']:
                case 'Km para Milhas':
                    output = float(input_value) * 0.6241
                    output_string = f'{input_value} km são {output} milhas.'
                case 'Kg para Gramas':
                    output = float(input_value) * 100
                    output_string = f'{input_value} kg são {output} gramas.'
                case 'Minutos para segundos':
                    output = float(input_value) * 60
                    output_string = f'{input_value} minutos são {output} segundos.'

            window['-TXT_1-'].update(output_string)
        else:
            window['-TXT_1-'].update('Digite um valor valido!!')

window.close()