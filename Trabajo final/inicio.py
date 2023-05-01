import PySimpleGUI as sg
import os, io
import crear_perfil as perfil
from PIL import Image, ImageDraw
import json
sg.ChangeLookAndFeel('LightGrey4')


if os.path.exists('perfiles.json'):
    with open('perfiles.json','r') as archivo:
        datos = json.load(archivo)
        lista_fotos = list(map(lambda elem : elem["Foto"],datos))
        for foto in lista_fotos:
            print(f"Ruta imagen {foto}")
else:
    with open('perfiles.json','w') as archivo:
        lista_fotos=[]

ruta_imagen = os.path.join(os.getcwd(),"Fotos","usuario.png")

#si el archivo existe y tiene perfiles cargados entra en el if y carga las fotos de los usuarios
if(len(lista_fotos) > 0):
    i = 0
    #esto lo hago para que no tire error con algunas fotos, para que acepte cualquier tipo de foto
    for foto in lista_fotos:
        with open(foto, 'rb') as file:
            img_bytes = file.read()
            image = Image.open(io.BytesIO(img_bytes))
            image.thumbnail((150, 150))
            bio = io.BytesIO()
            image.save(bio, format='PNG')
            lista_fotos[i] = bio.getvalue()
            i+=1
    imagenes = [sg.Image(foto) for foto in lista_fotos]
#sino pone la predeterminada
else:
    imagenes = [sg.Image(ruta_imagen)]

layout = [[sg.Text('UNLP-Image', size=(50, 2), font=('Times New Roman', 50), text_color='Black', justification=("c"))],
        [*imagenes],
        [sg.Button("Agregar perfil",key='agregar_perfil')],
        [sg.Button('Cerrar',size=(20, 2), button_color=('white', 'grey'), font=('Helvetica', 12))]]

#crea la ventana
window = sg.Window('Inicio', layout, element_justification='c', size=(1080,720))

while True:
    event,values = window.read()
    #cerrado
    if event == ('Cerrar') or event == sg.WIN_CLOSED:
        break
    
    if event ==('agregar_perfil'):
        window.hide()
        perfil.agregar_perfil()
        window.UnHide()

        #abris el archivo JSON para cargar las nuevas fotos
        with open('perfiles.json', 'r') as archivo:
            datos = json.load(archivo)
            lista_fotos = [elem["Foto"] for elem in datos]

        #se puede dar que pones agregar perfil y volves atras sin cargar nada entonces se toma ese caso tambien por las dudas
        if(len(lista_fotos) > 0):
            i = 0
            #esto lo hago para que no tire error con algunas fotos, para que acepte cualquier tipo de foto
            for foto in lista_fotos:
                with open(foto, 'rb') as file:
                    img_bytes = file.read()
                    image = Image.open(io.BytesIO(img_bytes))
                    image.thumbnail((150, 150))
                    bio = io.BytesIO()
                    image.save(bio, format='PNG')
                    lista_fotos[i] = bio.getvalue()
                    i+=1
            imagenes = [sg.Image(foto) for foto in lista_fotos]
        else:
            imagenes = [sg.Image(ruta_imagen)]
        #se crea un nuevo layout actualizado
        layout = [[sg.Text('UNLP-Image', size=(50, 2), font=('Times New Roman', 50), text_color='Black', justification=("c"))],
                [*imagenes],
                [sg.Button("Agregar perfil",key='agregar_perfil')],
                [sg.Button('Cerrar',size=(20, 2), button_color=('white', 'grey'), font=('Helvetica', 12))]]
        #cerras ventana vieja
        window.close()
        #creas ventana nueva actualizada
        window = sg.Window('Inicio', layout, element_justification='c', size=(1080, 720))

window.close()