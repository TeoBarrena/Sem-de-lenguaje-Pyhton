import os
import io
from PIL import Image
import PySimpleGUI as sg 

def imagen(perfil):
        with open(perfil, 'rb') as file:
            img_bytes = file.read()
            image = Image.open(io.BytesIO(img_bytes))
            image.thumbnail((150, 150))
            bio = io.BytesIO()
            image.save(bio, format='PNG')
            perfil = bio.getvalue()
        return perfil


def layout(perfil):
    boton_volver = [[sg.Button("< Volver", size=(20, 2), button_color=('black', 'skyblue'), font=('Helvetica', 12),key='volver')]]
    boton_guardar = [[sg.Button('Guardar', size=(20, 2), button_color=('black', 'skyblue'), font=('Helvetica', 12))]]
    columna= [sg.Column(boton_volver, element_justification='left', expand_x=True),
              sg.Column(boton_guardar, element_justification='rigth', expand_x=True)]
    
    #layout
    layout = [[sg.Text('Editar perfil', size=(20, 1), font=('Times New Roman', 75), text_color='Black', justification=("c"))],
          [sg.Text('Nick o alias', size=(20, 1), font=('Times New Roman', 25), text_color='Black', justification=("c"))],
          [sg.Text(f'-{perfil["Alias"]}-',size=(20, 1), font=('Helvetica', 15), text_color='Black', justification=("c"))],
          [sg.Text('Nombre',size=(20, 1), font=('Times New Roman', 25), text_color='Black', justification=("c"))],
          [sg.InputText(perfil["Nombre"],background_color='skyblue', size=(50,1), font=('Helvetica', 10))],
          [sg.Text('Edad',size=(20, 1), font=('Times New Roman', 25), text_color='Black', justification=("c"))],
          [sg.Input(perfil["Edad"],background_color='skyblue', size=(50,1), font=('Helvetica', 10))],
          [sg.Text('Genero autopercibido',size=(20, 1), font=('Times New Roman', 25), text_color='Black', justification=("c"))],
          [sg.Combo(['Masculino','Femenino','Otro'],default_value=perfil["Genero"],key='Genero',size=(50,1),readonly=True,background_color='skyblue',font=('Helvetica', 10),button_arrow_color=('black'))], #combo es una lista desplegable
          [sg.Image(imagen(perfil['Foto']),key='-AVATAR_IMAGE-',size=(150,150))],
          [sg.Button("Seleccionar avatar",key='-AVATAR-',button_color=('black', 'skyblue'), font=('Helvetica', 12))],
          [columna]]
    return layout