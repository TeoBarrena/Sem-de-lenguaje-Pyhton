import PySimpleGUI as sg
import addPerfil as add

lista_perfiles=[]
sg.ChangeLookAndFeel('LightGrey4')

layout = [[sg.Text('UNLPImage',size=(30,30),justification='c',font=("Helvetica",15))],
          [sg.Button('Agregar perfil')],
          [sg.Button('Mostrar datos')],
          [sg.Button('Cerrar')]]

window = sg.Window("",layout,margins=(100,100))
while True:
    event,values = window.read()

    if event == ('Cerrar') or event == sg.WIN_CLOSED:
        break
    if event == 'Agregar perfil':
        add.agregar_perfil(lista_perfiles)
    if event == 'Mostrar datos':
        add.mostrarPerfil(lista_perfiles)
window.close()
