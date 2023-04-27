import PySimpleGUI as sg
import os, io
import crear_perfil as perfil
from PIL import Image, ImageDraw

lista_perfiles=[]
sg.ChangeLookAndFeel('LightGrey4')

def convert_to_bytes(file_or_bytes, resize=None):
   img = Image.open(file_or_bytes)
   with io.BytesIO() as bio:
      img.save(bio, format="PNG")
      del img
      return bio.getvalue()


#ruta_fotos1 = convert_to_bytes(os.path.join(os.getcwd(),"Fotos","meme2.png"))
#ruta_fotos2= convert_to_bytes(os.path.join(os.getcwd(),"Fotos","flecha2.png"))
#ruta_fotos3= convert_to_bytes(os.path.join(os.getcwd(),"Fotos","flecha.png"))
#ruta_fotos4= convert_to_bytes(os.path.join(os.getcwd(),"Fotos","usuario.png"))
#ruta_fotos5= convert_to_bytes(os.path.join(os.getcwd(),"Fotos","Gato2.jpg"))
#ruta_fotos12 = convert_to_bytes(os.path.join(os.getcwd(),"Fotos","gatopng.png"))
#ruta_fotos22= convert_to_bytes(os.path.join(os.getcwd(),"Fotos","gatopng2.png"))
#ruta_fotos32= convert_to_bytes(os.path.join(os.getcwd(),"Fotos","perro.jpg"))
#ruta_fotos42= convert_to_bytes(os.path.join(os.getcwd(),"Fotos","Gato1.jpg"))
#ruta_fotos52= convert_to_bytes(os.path.join(os.getcwd(),"Fotos","Gato2.jpg"))

#lista_fotos = [ruta_fotos1, ruta_fotos2, ruta_fotos3, ruta_fotos4]# ruta_fotos5, ruta_fotos12, ruta_fotos22, ruta_fotos32, ruta_fotos42, ruta_fotos52]
lista_fotos = []
def perfiles(lista_fotos):
    botonera = []
    for i in range(len(lista_fotos)):
        botonera.append(sg.Button(size=(20, 2), button_color=('black', 'white'), image_data=lista_fotos[int(i)], image_size=(100,100),image_subsample=5))
    botonera.append(sg.Button('+', size=(5, 2), button_color=('white', 'grey'), font=('Helvetica', 25),key='agregar_perfil'))
    return botonera

layout = [[sg.Text('UNLP-Image', size=(50, 2), font=('Times New Roman', 50), text_color='Black', justification=("c"))],
        [perfiles(lista_fotos)],
        [sg.Button('Cerrar',size=(20, 2), button_color=('white', 'grey'), font=('Helvetica', 12))]]


window = sg.Window('Inicio', layout, element_justification='c', size=(1080,720))

while True:
    event,values = window.read()

    if event == ('Cerrar') or event == sg.WIN_CLOSED:
        break
    if event ==('agregar_perfil'):
        lista_fotos = perfil.agregar_perfil(lista_fotos)
        layout[1]=perfiles(lista_fotos)#corregir no anda bien
        window.refresh()#corregir no anda bien
window.close()
