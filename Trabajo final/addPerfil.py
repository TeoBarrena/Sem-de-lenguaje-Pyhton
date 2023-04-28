import PySimpleGUI as sg
import os,io
import json
from PIL import Image, ImageDraw

def agregar_perfil():
    ruta_imagen = os.path.join(os.getcwd(),"Fotos","usuario.png")
    if os.path.exists('perfiles.txt'):
        archivo = open('perfiles.txt','r')
        contenido_archivo = archivo.read()
        archivo.close()
        archivo = open("perfiles.txt",'a')
        ok = True
    else:
        archivo = open ("perfiles.txt",'w')
        ok = False
    layout = [[sg.Text('Nuevo Perfil',font=('Helvetica',15)),sg.Button("< Volver", button_color=('black', 'white'),border_width=0,pad=(250,10))],
          [sg.Text('Nick o alias',font=('Helvetica',10))],
          [sg.InputText()],
          [sg.Text('Nombre',font=('Helvetica',10))],
          [sg.InputText()],
          [sg.Text('Edad',font=('Helvetica',10))],
          [sg.Input()],
          [sg.Text('Genero autopercibido',font=('Helvetica',10))],
          [sg.Combo(['Masculino','Femenino','Otro'],default_value='Selecciona una opcion',key='Genero',size=(30,1))], #combo es una lista desplegable
          [sg.Image(ruta_imagen,key='-AVATAR_IMAGE-',size=(150,100))],
          [sg.Button("Seleccionar avatar",key='-AVATAR-')],
          [sg.Button('Guardar',pad=(400,10),size=(8,2),button_color=('sky blue'))]]
    window= sg.Window("Crear nuevo perfil",layout,margins=(100,100))
    while True:
        event,values = window.read()

        #cambio de imagen de usuario
        if event == '-AVATAR-':
            ruta_imagen = sg.popup_get_file('Seleccionar avatar', no_window=True, file_types=(('Imagenes', '*.png *.jpg *.jpeg *.gif *.bmp *.tiff'),))
            if ruta_imagen:
                try:
                    with open(ruta_imagen, 'rb') as file:
                        img_bytes = file.read()
                        image = Image.open(io.BytesIO(img_bytes))
                        image.thumbnail((150, 150))
                        bio = io.BytesIO()
                        image.save(bio, format='PNG')
                        window['-AVATAR_IMAGE-'].update(data=bio.getvalue())
                except Exception as e:
                    sg.popup_error(f'Error al cargar la imagen: {e}')
        #cerrado
        if event=="CANCELAR" or event== sg.WINDOW_CLOSED or event == "< Volver":
            break
        #guardado del perfil
        if event=='Guardar':
            #verificacion campos completos
            if any(len(values[key]) == 0 for key in values) or values['Genero'] == 'Selecciona una opcion':
                sg.popup('Por favor complete todos los campos.')
                continue
            alias = values[0]
            nombre=values[1]
            #verificacion edad sea un entero
            while True:
                try:
                    edad = int(values[2])
                    break
                except ValueError:
                    sg.popup('Por favor ingrese un número entero válido para la edad.')
                    event, values = window.read()#se declara de vuelta para que lea el nuevo valor de edad ingresado
                    continue
            foto = ruta_imagen
            #como guardar el genero
            if values['Genero'] == 'Otro':
                genero = sg.popup_get_text("Complete manualmente su genero")
            else:
                genero = values['Genero']
            #guardado de datos
            datos = {"Nombre": nombre,"Edad": edad,"Alias":alias,"Genero":genero,"Foto":foto}
            #verificar alias unico
            if ok: #si no hacia esto se rompia cuando el archivo estaba recien creado sin contenido, porque contenido archivo no habia sido asignado
                if alias in contenido_archivo:
                    while True:
                        nuevo_alias = sg.popup_get_text("Ese alias ya existe, ingrese otro")
                        if nuevo_alias is None or nuevo_alias == '':
                            break
                        elif nuevo_alias not in contenido_archivo:
                            datos['Alias'] = nuevo_alias
                            break
            #agregar al archivo JSON            
            json.dump(datos,archivo,indent= 2)
            archivo.close()   
            sg.popup('Perfil creado con éxito')         
            break
    window.close()



