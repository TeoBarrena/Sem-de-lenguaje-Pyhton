import PySimpleGUI as sg
import os
import json
ruta_imagen = os.path.join(os.getcwd(),"Fotos","usuario.png")

def agregar_perfil(lista_fotos):
    if os.path.exists('perfiles.txt'):
        archivo = open("perfiles.txt",'a')
    else:
        archivo = open ("perfiles.txt",'w')
    layout = [[sg.Text('Nuevo Perfil',font=('Helvetica',15)),sg.Button("< Volver", button_color=('black', 'white'),border_width=0,pad=(250,10))],
          [sg.Text('Nick o alias',font=('Helvetica',10))],
          [sg.InputText()],
          [sg.Text('Nombre',font=('Helvetica',10))],
          [sg.InputText()],
          [sg.Image(ruta_imagen,pad=(350,10),key='-AVATAR_IMAGE-',size=(150,100))],
          [sg.Text('Edad',font=('Helvetica',10)),sg.Button("Seleccionar avatar",pad=(350,10),key='-AVATAR-')],
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
        if event == '-AVATAR-':
            archivo_avatar = sg.popup_get_file('Seleccionar avatar', no_window=True)
            window['-AVATAR_IMAGE-'].update(filename=archivo_avatar, size=(150, 150))
        if event=='Guardar':
            alias = values[0]
            nombre=values[1]
            edad = values[2]
            foto = archivo_avatar
            lista_fotos.append(foto)#corregir no anda bien
            if values['Genero'] == "Selecciona una opcion": #si values['Genero] es igual a "selecciona una opcion" significa que no se eligio ni M ni F entonces busca en la posicion del boton "Otro"
                genero = values['OtroGenero']
            else: # si es distinto significa que eligio M o F entonces asigna
                genero = values['Genero']
            datos = {"Nombre": nombre,"Edad": edad,"Alias":alias,"Genero":genero,"Foto":foto}
            json.dump(datos,archivo,indent= 2)
            archivo.close()   
            sg.popup('Perfil creado con éxito')         
            break
    window.close()
    return lista_fotos


