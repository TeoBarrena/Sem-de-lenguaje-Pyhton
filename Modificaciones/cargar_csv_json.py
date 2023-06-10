import csv
import json
import datetime
import time
#agregar al archivo CSV, no es para la funcion requerida por Generar Meme y Generar Collage
def cargar_csv(alias,accion):
    timestamp = int(datetime.datetime.now().timestamp())
    with open ('perfiles.csv','a',newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow([timestamp,alias,accion,',',',']) 

#agregar al archivo JSON
def cargar_json(usuario_nuevo,ok,datos):
    with open('perfiles.json','w') as archivo:
        datos.append(usuario_nuevo)
        if ok:
            json.dump(datos,archivo,indent= 2)
            archivo.write('\n') # se agrega un salto de línea para escribir la siguiente lista en la siguiente línea
        else:
            json.dump(datos,archivo,indent=2)
            archivo.write('\n')

#agregar al archivo CSV con la info de valores y texto para Generar Meme y Generar Collage
def cargar_csv_generar(alias,accion,valores,texto):
    timestamp = int(datetime.datetime.now().timestamp())
    with open('perfiles.csv','a',newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow([timestamp,alias,accion,valores,texto])
