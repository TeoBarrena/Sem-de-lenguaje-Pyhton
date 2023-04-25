import PySimpleGUI as sg
import os
import json

def agregar_perfil():
    if os.path.exists('perfiles.txt'):
        archivo = open("perfiles.txt",'a')
    else:
        archivo = open ("perfiles.txt",'w')
    layout = [[sg.Text('Nuevo Perfil',font=('Helvetica',15)),sg.Button("< Volver", button_color=('black', 'white'),border_width=0,pad=(250,10))],
          [sg.Text('Nick o alias',font=('Helvetica',10))],
          [sg.InputText()],
          [sg.Text('Nombre',font=('Helvetica',10))],
          [sg.InputText()],
          [sg.Text('Edad',font=('Helvetica',10))],
          [sg.Input()],
          [sg.Text('Genero autopercibido',font=('Helvetica',10))],
          [sg.Combo(['Masculino','Femenino'],default_value='Selecciona una opcion',key='Genero',size=(30,1))], #combo es una lista desplegable
          [sg.Button("",size=(2,1)),sg.Text("Otro")],
          [sg.Input("Complete el genero",key = 'OtroGenero')],#arreglar
          [sg.Button('Guardar',pad=(400,10),size=(8,2),button_color=('sky blue'))]]
    window= sg.Window("Crear nuevo perfil",layout,margins=(100,100))
    while True:
        event,values = window.read()

        if event=="CANCELAR" or event== sg.WINDOW_CLOSED or event == "< Volver":
            break
        if event=='Guardar':
            alias = values[0]
            nombre=values[1]
            edad = values[2]
            if values['Genero'] == "Selecciona una opcion": #si values['Genero] es igual a "selecciona una opcion" significa que no se eligio ni M ni F entonces busca en la posicion del boton "Otro"
                genero = values['OtroGenero']
            else: # si es distinto significa que eligio M o F entonces asigna
                genero = values['Genero']
            datos = {"Nombre": nombre,"Edad": edad,"Alias":alias,"Genero":genero}
            json.dump(datos,archivo)
            archivo.close()            
            break
    window.close()


