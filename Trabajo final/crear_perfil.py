import PySimpleGUI as sg
import os
import io
import json
import cargar_csv_json as cargar
import layout_crear_perfil as lay
from PIL import Image

def agregar_perfil():
    """
    Se ejecuta una ventana con campos para llenar con informacion acerca del nuevo perfil que se creara y se carga
    este nuevo perfil en el perfiles.json, y tambien se actualiza la lista datos que contiene los perfiles cargados.
    """
    #imagen predeterminada
    ruta_imagen = os.path.join(os.getcwd(),"Fotos","usuario.png")
    
    if os.path.getsize('perfiles.json') > 0:
        with open('perfiles.json','r') as archivo:
            datos = json.load(archivo)
            ok = True
    else:    
        datos = []
        ok = False

    window= sg.Window("Crear nuevo perfil",lay.layout(), element_justification='c', size=(1366,768), resizable=True )
    
    while True:
        event,values = window.read()

        #cambio de imagen de usuario
        if event == '-AVATAR-':
            ruta_imagen = sg.popup_get_file('Seleccionar avatar', no_window=True, file_types=(('Imagenes', '*.png *.jpg *.jpeg *.gif *.bmp *.tiff'),))
            if not ruta_imagen:
                ruta_imagen = os.path.join(os.getcwd(),"Fotos","usuario.png")
            elif ruta_imagen:
                try:
                    #para que no de error de Image data cuando se pone una nueva foto
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
        if event=="CANCELAR" or event== sg.WINDOW_CLOSED or event == "volver":
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
                while genero is None or genero.strip() == '':
                    # Se ejecuta si el usuario presiona Cancelar o no ingresa ningún valor.
                    sg.popup('Debe ingresar un valor para su género')
                    genero = sg.popup_get_text("Complete manualmente su genero")
            else:
                genero = values['Genero']

            #guardado de datos
            usuario_nuevo = {"Nombre": nombre,"Edad": edad,"Alias":alias,"Genero":genero,"Foto":foto}

            #verificar alias unico
            #utilizar filter
            alias_existente = [d["Alias"] for d in datos] #agarra del primero hasta el anteultimo, el ultimo lo excluye
            if alias in alias_existente:
                while True:
                   nuevo_alias = sg.popup_get_text("Ese alias ya existe, ingrese otro")
                   if nuevo_alias is None or nuevo_alias == '': #en caso de apretar cancel se ejecuta el while de nuevo, para asegurar que elije algun alias que no se repite
                        continue
                   elif nuevo_alias == alias:
                       continue
                   elif nuevo_alias in alias_existente: #la segunda condicion se toma por si apretan el boton cancelar
                        continue #vuelve a entrar al while
                   else:
                        usuario_nuevo['Alias'] = nuevo_alias
                        break
                   
            cargar.cargar_json(usuario_nuevo,ok,datos)#llama al modulo para cargar json
            
            cargar.cargar_csv(usuario_nuevo["Alias"],"Creo perfil")#llama al modulo para cargar csv
            
            sg.popup('Perfil creado con exito')         
            break
    window.close()
    #verifica si el usuario no apreto volver y no cargo ningun dato.
    if(datos!=[]):
        return datos
