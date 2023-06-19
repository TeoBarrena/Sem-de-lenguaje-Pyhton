import PySimpleGUI as sg
from PIL import Image 
from PIL import ImageDraw
from PIL import ImageFont
from layouts import generar_collage
import pandas as pd
import os
import re
import configuracion as modulo_configuracion
import cargar_csv_json 
import utilidades.constantes as constante
import utilidades.abrir_fotos as abrir
import tempfile
import etiquetas as etiquetar
sg.theme ('LightGrey4')

# Función para agregar el título a la imagen
def agregar_titulo(imagen, titulo):
    width, height = imagen.size
    barra_height = 50

    # Crear una nueva imagen con una barra debajo de la imagen original
    nueva_imagen = Image.new('RGB', (width, height + barra_height), (255, 255, 255))
    nueva_imagen.paste(imagen, (0, 0))

    # Agregar el título a la barra
    draw = ImageDraw.Draw(nueva_imagen)
    ruta_fuente = os.path.join(constante.ROOT_PATH,'tipografias','arial.ttf')
    font = ImageFont.truetype(ruta_fuente, 20)
    text_width, text_height = draw.textsize(titulo, font=font)
    text_x = int((width - text_width) / 2)
    text_y = height + int((barra_height - text_height) / 2)
    draw.text((text_x, text_y), titulo, font=font, fill=(0, 0, 0))

    return nueva_imagen


def buscar_csv():
    ruta_csv = os.path.join(constante.ROOT_PATH, 'archivos', 'perfiles.csv') 
    data_csv = pd.read_csv(ruta_csv)
    operaciones = ['Nueva imagen clasificada', 'Modificacion de imagen clasificada']
    fotos = data_csv[data_csv['Operacion'].isin(operaciones)]
    fotos = fotos["Valores"].unique()
    return fotos

def window_generar_collage(alias,datos):
    fotos = buscar_csv()
    plantilla = datos["image"]
    textbox = datos["text_boxes"]
    espacios_ocupados = 0
    fotos_elegidas = []
    imagenes_seleccionadas = []
    window = sg.Window('',generar_collage.layout_collage(fotos,alias,plantilla), element_justification='c', size=(1366,768), resizable=True )
    while True:
        event, values = window.read()
        if event == ("-VOLVER-") or event == (sg.WINDOW_CLOSED):
            break
        coordenadas=[]
        cantidad_textboxes = len(textbox)
        
        if plantilla == "Plantilla_1.png":
            # Obtener la cantidad de imágenes y las rutas de las imágenes
            #cantidad_imagenes, rutas_imagenes = obtener_imagenes(plantilla_seleccionada)
            # Coordenadas de las imágenes en la plantilla
            for i in range(cantidad_textboxes):
                coordenadas.append((textbox[i]["top_left_x"], textbox[i]["top_left_y"]))
            #variables que se pasan para poder hacer el resize de la imagen
            x = 650
            y = 260
        elif plantilla == "Plantilla_2.png":
            #cantidad_imagenes, rutas_imagenes = obtener_imagenes(plantilla_seleccionada)
            for i in range(cantidad_textboxes):
                coordenadas.append((textbox[i]["top_left_x"], textbox[i]["top_left_y"]))
            x = 300
            y = 350
        elif plantilla == "Plantilla_3.png":
            #cantidad_imagenes, rutas_imagenes = obtener_imagenes(plantilla_seleccionada)
            coordenadas = [(53, 41), (53, 455)]
            x = 610
            y = 400
        elif plantilla == "Plantilla_4.png":
            #cantidad_imagenes, rutas_imagenes = obtener_imagenes(plantilla_seleccionada)
            for i in range(cantidad_textboxes):
                coordenadas.append((textbox[i]["top_left_x"],textbox[i]["top_left_y"]))
            x = 320
            y = 250
        #plantilla = pegar_imagenes(plantilla,cantidad_textboxes, coordenadas, x, y) 
        
        if event == '-AGREGAR-':
            if espacios_ocupados < len(textbox):

                if values["-ARCHIVOS-"]:
                    # Dentro del bucle o proceso
                    imagen_seleccionada = values["-ARCHIVOS-"][0]
                    fotos_elegidas.append(imagen_seleccionada)
                    ruta_imagen = os.path.join(constante.ROOT_PATH, 'fotos', imagen_seleccionada)
                    imagen = Image.open(ruta_imagen)
                    nueva_imagen = imagen.resize((x,y))

                    # Asegúrate de que `coordenadas` sea una lista que contiene las coordenadas de las posiciones libres en la plantilla

                    # Pega la imagen seleccionada en el siguiente espacio libre del collage
                    coordenadas_siguiente = coordenadas[espacios_ocupados]
                    imagenes_seleccionadas.append((nueva_imagen, coordenadas_siguiente))

                    # Incrementa el contador de espacios ocupados
                    espacios_ocupados += 1

                    ruta = os.path.join(constante.ROOT_PATH,'fotos',plantilla)
                    plantilla_modificada = Image.open(ruta)

                    # Crea una copia de la plantilla modificada
                    plantilla_modificada_copia = plantilla_modificada.copy()

                    # Itera sobre las imágenes seleccionadas y pégalas en el collage
                    for nueva_imagen, coordenadas in imagenes_seleccionadas:
                        plantilla_modificada_copia.paste(nueva_imagen, coordenadas)
                    # Guarda la plantilla modificada en un archivo temporal
                    temp_file = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
                    temp_file_path = temp_file.name
                    plantilla_modificada_copia.save(temp_file_path)
                    temp_file.close()
                    temp_file_path = abrir.abrir(temp_file_path,(400,400))
                    # Actualiza el collage en la ventana
                    window['-IMAGE-'].update(temp_file_path)
        if event == "-ENTER-":
            texto_ingresado_titulo = values['-TEXTO-']
            if texto_ingresado_titulo:
                window['-TITULO-'].update(texto_ingresado_titulo)

                # Obtener la imagen de la plantilla
                ruta = os.path.join(constante.ROOT_PATH,'fotos',plantilla)
                plantilla_modificada = Image.open(ruta)

                # Agregar el título a la imagen
                imagen_con_titulo = agregar_titulo(plantilla_modificada, texto_ingresado_titulo)

                # Guardar la imagen con el título en un archivo temporal
                temp_file = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
                temp_file_path = temp_file.name
                imagen_con_titulo.save(temp_file_path)
                temp_file.close()

                # Actualizar la imagen en la ventana
                window['-IMAGE-'].update(filename=temp_file_path)
            else:
                sg.popup("Ingrese un titulo.") 
        if event == "-ETIQUETAR-":
            window.hide()
            etiquetar.eti(alias)
            window.UnHide()
            fotos = buscar_csv()
            window["-ARCHIVOS-"].update(fotos)
        if event == "-GUARDAR-":
            if espacios_ocupados < len(textbox):
                sg.popup("Quedaron espacios vacios en el collage")
            else:
                repositorio_collage = ""
                ruta_directorios = os.path.join(constante.ROOT_PATH,"archivos","directorios.json")
                datos_json = cargar_csv_json.cargar_lista_json(ruta_directorios)
                for dato in datos_json:
                    if (dato["Alias"] == alias):
                        repositorio_collage = dato["R_Collage"]
                
                while True:
                    if (repositorio_collage == ""):
                        window.hide()
                        directorios = modulo_configuracion.conf(alias)
                        if (not directorios):
                            sg.popup("Se debe cargar el directorio donde se va a guardar el collage.")
                        else:
                            repositorio_collage = directorios["R_Collage"]
                            break
                        window.UnHide()
                    else:
                        break
                texto_ingresado = sg.popup_get_text('Ingrese el nombre de la foto:', 'Guardar foto')
                if texto_ingresado:
                        parametro = f'{texto_ingresado}.png'  # Agrega la extensión ".png" al nombre
                        imagen = plantilla_modificada_copia #Pasar la imagen modificada, el collage con todas las fotos correspondientes
                        imagen.save(os.path.join(repositorio_collage,parametro), format='PNG')
                        nombres_fotos = ";".join(fotos_elegidas)
                        cargar_csv_json.cargar_csv(alias, "nuevo_collage",nombres_fotos,texto_ingresado_titulo)
                        sg.popup("El collage se guardó con éxito.")
                window.close()
        
    window.close()