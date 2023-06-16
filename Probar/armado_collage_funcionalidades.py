import PySimpleGUI as sg
import os
import json
import csv


from UnlpImage.rutas import ARCHIVO_PLANTILLAS
from UnlpImage.rutas import DATOS_IMAGENES
from UnlpImage.rutas import PLANTILLAS_COLLAGES
from UnlpImage.rutas import ARCHIVO_LOGS
from UnlpImage.Funcionalidades.chequeo_archivos import verificarLogsGuardar
from UnlpImage import rutas
from datetime import datetime

from PIL import Image
from PIL import ImageOps
from PIL import ImageDraw

def abrir_json_plantillas():
    with open(ARCHIVO_PLANTILLAS, 'r') as archivo:
      
        plantillas = json.load(archivo)
        for plantilla in plantillas:
            plantilla["direccion"] = os.path.join(PLANTILLAS_COLLAGES, plantilla["direccion"])
    
    return plantillas


def validar_imagen(imagen_ruta):
    valido = False
    imagen_ruta = rutas.convertir_para_guardar(imagen_ruta)
    try:
        with open(DATOS_IMAGENES, "r") as archivo:
            reader = csv.reader(archivo)
            for fila in reader:
                if fila[0] == imagen_ruta:
                    if fila[1] != "":
                        valido = True
                        break
        return valido
    except:
        sg.popup("Se produjo un error, intente de nuevo.")


def pegar_imagen_en_collage(imagen_ruta, collage, info):
    imagen = ImageOps.fit(Image.open(imagen_ruta), (info["resolucion_ancho"], info["resolucion_alto"]))
    collage.paste(imagen, (info["coordenada_x"], info["coordenada_y"]))
    return collage


def agregar_titulo_al_collage(titulo, collage):
    draw = ImageDraw.Draw(collage)
    draw.text((20, 580), titulo, )
    return collage


def obtener_nombre_imagen(imagen_ruta):
    nombre = str(imagen_ruta).split("/")
    nombre = nombre[len(nombre)-1]
    nombre = nombre.split(".")
    nombre = nombre[0]
    return nombre


def actualizar_log(perfil, nombres, titulo):
    fila = []  
    
    timestamp = datetime.timestamp(datetime.now())
    fecha_hora = datetime.fromtimestamp(timestamp)
    
    fila.append(fecha_hora)
    fila.append(perfil["alias"])
    fila.append("nuevo_collage")

    string_nombres = nombres[0]
    for i in range(len(nombres)-1):
        string_nombres += f";{nombres[i+1]}"

    fila.append(string_nombres)
    fila.append(titulo)

    try:
        with open(ARCHIVO_LOGS, 'a', encoding='UTF8', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(fila)
    except:
        verificarLogsGuardar()