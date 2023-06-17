import json
import csv
import os


def buscar_csv (alias_buscar):   
    nombres_imagenes = []
    with open('imagenes.csv', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for fila in lector_csv:
            nombre_imagen = fila[0].split("\\")[-1]  # Obtener el nombre de la imagen del primer elemento de la fila
            alias = fila[-1]  # Obtener el alias del último elemento de la fila
            
            if alias == alias_buscar:
                nombres_imagenes.append(nombre_imagen)
    return nombres_imagenes



def obtener(alias):
    nombres_imagenes = buscar_csv(alias)

    if nombres_imagenes:
        with open('directorios.json') as file:
            data = json.load(file)
            for item in data:
                if item['Alias'] == alias:
                    ruta_imagenes = item['R_Imagenes']
                    ruta_collage = item['R_Collage']
                    break

        imagenes = []
        for nombre_imagen in nombres_imagenes:
            ruta_imagen = os.path.join(ruta_imagenes, nombre_imagen)
            imagenes.append(ruta_imagen)
        return imagenes, ruta_collage

    return [], None

