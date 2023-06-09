import pandas as pd
import csv

data_set = pd.read_csv('perfiles.csv',encoding='utf-8')
print (data_set)#imprime el contenido del archivo csv
print(type(data_set))
print(data_set.columns)#imprime el encabezado
print(data_set.index)#imprime cuantos lineas hay
print(data_set.shape)#imprime cuantas filas y columnas hay
print(data_set.info())#Podemos usar **info()** para obtener un resumen que indica si las columnas contienen valores nulos,  
                      #**qué tipo de dato**  pandas le asignó, etc.
print(data_set["Nick"])#imprime toda la columna de nicks


#UNA FORMA PARA GENERAR EL GRAFICO DE RUEDA DE CANT USUARIOS POR GENERO:
data_set_json = pd.read_json('perfiles.json')#carga el json 
print("-"*30)
print(data_set_json)#imprime json
print("Cantidad generos")
print(data_set_json["Genero"].value_counts())#imprime los valores de cada genero
#LAS COLUMNAS SON DE TIPO SERIES

#forma de definir otros indices
top_3 = pd.Series(
       [27.27, 16.35, 9.52],
       index=["Python", "Java", "JavaScript" ]
       )
top_3

#Para crear un DataFrame:
datos = {
        'tenista': ['Novak Djokovic', 'Rafael Nadal', 'Roger Federer', 'Ivan Lendl', 'Pete Sampras', 'John McEnroe', 'Bjorn Borg'],
        'pais': ['Serbia', 'España', 'Suiza', 'República Checa','Estados Unidos', 'Estados Unidos', 'Suecia'],
        'gran_slam': [22, 22, 20, 8, 14, 7, 11],
        'master_1000': [38, 36, 28, 22, 11, 19, 15],
        'otros': [6, 1, 6, 5, 5, 3, 2]
         }
labels_filas = ["H01", "H02", "H03", "H04", "H05", "H06", "H07"]

df = pd.DataFrame(data=datos, index=labels_filas)#si haces pd.DataFrame(data=datos) los indices se generan automaticamente

tenistas = df["tenista"]
tenistas #imprime todos los tenistas y su indice

