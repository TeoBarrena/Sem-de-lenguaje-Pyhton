import PySimpleGUI as sg
import crear_perfil as perfil

sg.ChangeLookAndFeel('LightGrey4')

layout = [[sg.Text('UNLPImage', size=(50, 2), justification='left', font=('Helvetica', 15))],
          [sg.Button('Agregar perfil', size=(20, 2), button_color=('white', 'grey'), font=('Helvetica', 12)),sg.Button('Cerrar', size=(20, 2), button_color=('white', 'grey'), font=('Helvetica', 12))]]

window = sg.Window('', layout, element_justification='c', margins=(150, 200))

while True:
    event,values = window.read()

    if event == ('Cerrar') or event == sg.WIN_CLOSED:
        break
    if event == 'Agregar perfil':
        perfil.agregar_perfil()
window.close()
