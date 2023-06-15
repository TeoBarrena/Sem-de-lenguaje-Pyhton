import csv
import json
import datetime
import time
#agregar al archivo CSV. Valores y texto sirven para Generar Meme y Generar Collage.
def cargar_csv(alias,accion,valores = ',', texto = ','):
    timestamp = int(datetime.datetime.now().timestamp())
    with open ('perfiles.csv','a',newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow([timestamp,alias,accion,valores,texto]) 

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