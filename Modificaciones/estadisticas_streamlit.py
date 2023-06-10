import pandas as pd
import calendar
from matplotlib import pyplot as plt


def porcentajes_genero(data_set_json):
    generos = data_set_json["Genero"].value_counts().sort_values(ascending=False)
    print(generos.value_counts())#imprime los valores de cada genero
    #print(f"INDICES: {generos}")

    etiquetas = list(generos.index)
    #print(f"Etiquetas: {etiquetas}")
    data_dibujo = list(generos.values)
    #print(f"Data dibujo: {data_dibujo}")

    plt.pie(data_dibujo, labels=etiquetas, autopct='%1.1f%%',
            shadow=True, startangle=120, labeldistance= 1.1)
    plt.axis('equal') 
    plt.legend(etiquetas)

    plt.title("Uso por genero")
    #plt.show()

def dias_semana(data_set_csv):
    data_set_csv["Timestamp"] = pd.to_datetime(data_set_csv["Timestamp"], unit='s', origin='unix')
    data_set_csv['Timestamp'] = data_set_csv['Timestamp'].dt.tz_localize('UTC')  # Establecer la zona horaria como UTC
    data_set_csv['Día de la semana'] = data_set_csv['Timestamp'].dt.day_name()
    print(f"DIa: {data_set_csv['Timestamp'].dt.day_name()}")
    print(f"IMPRIMIENDOOO: {data_set_csv['Día de la semana']}")

    # Obtener el recuento de registros para cada día
    conteo_dias = data_set_csv['Día de la semana'].value_counts()

    # Obtener los nombres de los días en español
    dias_semana_es = list(calendar.day_name)

    # Crear la gráfica de barras
    conteo_dias = conteo_dias.reindex(index=dias_semana_es)  # Reordenar los datos según los nombres en español
    conteo_dias.plot(kind='bar')

    # Personalizar la gráfica
    plt.xlabel('Día de la semana')
    plt.ylabel('Cantidad')
    plt.title('Cantidad de operaciones por día de la semana')

def cantidad_operaciones(data):
    #operaciones = data["Operacion"]
    #print(operaciones) #imprime toda la columna de operaciones
    operaciones = data["Operacion"].value_counts().sort_values(ascending=False)#ordena segun cant. operaciones
    #print(operaciones)

    operaciones.plot(kind='bar')

    plt.xlabel('Operaciones')
    plt.ylabel('Cantidad')
    plt.title('Grafico de operaciones')
    #plt.show()

def cant_operaciones_usuarios(data):
    #groupby en la columna "Nick" del DataFrame data para agrupar los datos por usuario.
    #Luego, utilizamos el método size() para contar el número de filas correspondiente a cada grupo.
    operaciones_por_usuario = data.groupby("Nick").size()
    operaciones_por_usuario = operaciones_por_usuario.sort_values(ascending=False)#ordenar por cant. operaciones
    
    categorias = operaciones_por_usuario.index #tiene cargado los alias
    print(f"CATEGORIAS: {categorias}")
    operaciones = operaciones_por_usuario.values.T #tiene la cantidad de operaciones
    print(f"Operaciones: {operaciones}")

    fig, ax = plt.subplots()
    #for i in range(len(categorias)):
       # x = 1
        #ax.bar(categorias, operaciones, label=f'Operaciones')
        #x +=1
    ax.bar(categorias, operaciones, label=f'Operaciones')
    # Configurar el gráfico
    ax.set_xlabel('Nombres')
    ax.set_ylabel('Total de Operaciones')
    ax.set_title('Gráfico de Barras Apilado')
    ax.legend()
    
    

data_set_csv = pd.read_csv('perfiles.csv')#carga el csvv
data_set_json = pd.read_json('perfiles.json')#carga el json
if __name__ == "__main__":
    data_set_csv = pd.read_csv('perfiles.csv')#carga el csv
    data_set_json = pd.read_json('perfiles.json')#carga el json
    #porcentajes_genero(data_set_json)
    #dias_semana(data_set_csv)
    #cantidad_operaciones(data_set_csv)
    cant_operaciones_usuarios(data_set_csv)
    