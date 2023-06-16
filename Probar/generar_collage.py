from tkinter import image_names
import PySimpleGUI as sg
import os
import io
import json
import csv
#import Configuracion as configuracion
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import etiquetas as etiqueta
import layouts.layout_generar_collage as layout_collage
import utilidades.obtener_rutas as obtener_rutas
import utilidades.abrir_fotos as abrir_foto_collage
import cv2

sg.theme ('LightGrey4')

def superponer_fotos (foto,textbox,imagen,posicion):
    try:
        imagen_fondo = cv2.imread(foto)
        imagen_fondo_image=Image.fromarray(imagen_fondo)
        imagen_superpuesta = cv2.imread(imagen)
        imagen_superpuesta_image = Image.fromarray(imagen_superpuesta)
        pos_x_arriba = textbox[posicion]["top_left_x"]
        pos_y_arriba = textbox[posicion]["top_left_y"]
        pos_x_abajo = textbox[posicion]["bottom_right_x"]
        pos_y_abajo = textbox[posicion]["bottom_right_y"]
        coordenadas = (pos_x_arriba,pos_y_arriba,pos_x_abajo,pos_y_abajo)
        imagen_fondo_image.draw(imagen_superpuesta_image,(coordenadas))
        return imagen_fondo_image
    except Exception as e:
        sg.popup(f'Ocurrió un error en superponer_fotos: {str(e)}', title='Error')


def sacar_longitud (foto,textbox,imagen):
    longitud = len(textbox)
    imagen_superpuesta = imagen
    for i in range(0,longitud):
        imagen_superpuesta = superponer_fotos(foto,textbox,imagen_superpuesta,i)
        foto=imagen_superpuesta # Actualiza la imagen de fondo para la próxima iteración
    return foto
    
def window_generar_collage (alias,foto,textbox):
    
    imagenes, _ = obtener_rutas.obtener(alias)
    window = sg.Window('',layout_collage.layout_collage(foto,alias), element_justification='c', size=(1366,768), resizable=True )
    while True:
        event,values = window.read()

        if event == ("-VOLVER-") or event == sg.WIN_CLOSED:
            break
        
        if event == "-ARCHIVOS-":
            #Seleccionamos un archivo de la lista y lo mostramos.
            try:
                #Buscamos la información de la foto en el archivo de templates.
                for arc in imagenes:
                    if (arc['name'] == values["-ARCHIVOS-"][0]):
                        datos = arc
                #Mostramos en panalla el meme seleccionado.
                collage_seleccionado = abrir_foto_collage.abrir(os.path.join(os.getcwd(),"Fotos",datos["image"]))
                window["-IMAGE-"].update(data=collage_seleccionado)
            except:
                pass
        if event == "-ENTER-":
            descripcion = values['-TEXTO-']
            window["-TEXTO-"].update(descripcion)
        
        if event == "-AGREGAR-":
        
            try:
                """imagen_seleccionada = values["-ARCHIVOS-"][0]
                print(type(imagen_seleccionada))
                #imagen_seleccionada = Image.open(imagen_seleccionada)
                imagen_seleccionada = abrir_foto_collage.abrir(imagen_seleccionada)
                imagen_seleccionada_image = io.BytesIO(imagen_seleccionada)
                imagen_seleccionada = Image.open(imagen_seleccionada_image)
                print(type(imagen_seleccionada))
                # Agregar la imagen en las coordenadas especificadas
                imagen_base = Image.open(foto)
                # Crea un objeto BytesIO para leer los datos en formato de bytes
                foto_final = sacar_longitud(imagen_seleccionada,textbox,imagen_base)
                #Transformamos la imagen en bytes y la mostramos en pantalla.
                foto_final_actualizada = Image.open(foto_final)
                bio = io.BytesIO()
                foto_final_actualizada.save(bio, format="PNG")
                #imagen_resultante_data = foto_final 
                window["-IMAGE-"].update(data=foto_final_actualizada.getvalue(),size=(400,400),subsample=3)
                """
                imagen_seleccionada = values["-ARCHIVOS-"][0]
                print(type(imagen_seleccionada))
                imagen = cv2.imread(imagen_seleccionada)
                imagen_seleccionada_image = Image.fromarray(imagen)
                imagen_base = cv2.imread(foto)
                imagen_base_image = Image.fromarray(imagen_base)
                print(type(imagen_base_image))
                foto_final = sacar_longitud(imagen_seleccionada_image,textbox,imagen_base_image)
                foto_final = cv2.imread(foto_final)
                foto_final_image = Image.fromarray(foto_final)
                window["-IMAGE-"].update(data=foto_final_image.getvalue(),size=(400,400),subsample=3)
            except Exception as e:
                sg.popup(f'Ocurrió un error en el agregar: {str(e)}', title='Error')

        if event == "-ETIQUETAR-":
            window.Hide()
            etiqueta.eti(alias)
            window.UnHide()
        if event == ('-GUARDAR-') or event == sg.WIN_CLOSED: 
            
            break
        if event == ('-TEXTO-'):
            break
    window.close()
