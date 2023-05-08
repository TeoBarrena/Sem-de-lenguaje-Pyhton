import PySimpleGUI as sg
import io,io
import json
from PIL import Image,ImageDraw

def editar_perfil(alias):
    cambio_foto = False
    #cargar contenido del archivo en variable
    with open('perfiles.json') as archivo:
        contenido_archivo = json.load(archivo)

    #buscar el usuario con determinado alias
    for elem in contenido_archivo:
        if(elem["Alias"] == alias):
            usuario = elem
            foto = usuario["Foto"]
            #para que cargue bien la foto
            with open(usuario["Foto"], 'rb') as file:
                        img_bytes = file.read()
                        image = Image.open(io.BytesIO(img_bytes))
                        image.thumbnail((150, 150))
                        bio = io.BytesIO()
                        image.save(bio, format='PNG')
                        usuario["Foto"] = bio.getvalue()

    #layout
    layout = [[sg.Text('Editar perfil',font=('Helvetica',15)),sg.Button("< Volver", button_color=('black', 'white'),border_width=0,pad=(250,10))],
              [sg.Text('Nick o alias',font=('Helvetica',10))],
              [sg.Text(usuario["Alias"],font=('Helvetica',15))],
              [sg.Text('Nombre',font=('Helvetica',10))],
              [sg.InputText(usuario["Nombre"])],
              [sg.Text('Edad',font=('Helvetica',10))],
              [sg.Input(usuario["Edad"])],
              [sg.Text('Genero autopercibido',font=('Helvetica',10))],
              [sg.Combo(['Masculino','Femenino','Otro'],default_value=usuario["Genero"],key='Genero',size=(30,1))], #combo es una lista desplegable
              [sg.Image(usuario["Foto"],key='-AVATAR_IMAGE-',size=(150,100))],
              [sg.Button("Seleccionar avatar",key='-AVATAR-')],
              [sg.Button('Guardar',pad=(400,10),size=(8,2),button_color=('sky blue'))]
             ]        
    #creacion ventana
    window = sg.Window("Editar perfil",layout,margins=(100,100))
    #ejecucion ventana
    while True:
        event,values = window.read()
        #cerrado
        if event == sg.WINDOW_CLOSED or event == "< Volver":
            break
        
        #eleccion de imagen
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
                        cambio_foto = True #asi no da error 
                except Exception as e:
                    sg.popup_error(f'Error al cargar la imagen: {e}')

        #guardado
        if event == 'Guardar':
            
            nombre = values[0]
            print(nombre)
            #verificacion edad sea un entero
            while True:
                try:
                    edad = int(values[1])
                    break
                except ValueError:
                    sg.popup('Por favor ingrese un número entero válido para la edad.')
                    event, values = window.read()#se declara de vuelta para que lea el nuevo valor de edad ingresado
                    continue

            #como guardar el genero
            if values['Genero'] == 'Otro':
                genero = sg.popup_get_text("Complete manualmente su genero")
            else:
                genero = values['Genero']
            
            #verificacion para saber si hay que modificar la variable foto
            if cambio_foto:
                foto = ruta_imagen

            #nuevos datos
            datos_modificados = {"Nombre":nombre,"Edad":edad,"Alias":usuario["Alias"],"Genero":genero,"Foto":foto}

            #sobreescritura del JSON con nuevos datos si hubo, sino esta igual
            with open('perfiles.json','w') as archivo:
                for elem in contenido_archivo:
                    if elem["Alias"] == alias:
                        elem.update(datos_modificados)
                json.dump(contenido_archivo,archivo,indent=2)

            sg.Popup("Perfil editado con exito")
            break
    window.close()

