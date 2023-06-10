import PySimpleGUI as sg
import os, io
import crear_perfil as perfil
import menu_principal as menu
from PIL import Image
import json
import csv
sg.ChangeLookAndFeel('LightGrey4')

#Se crea esta función para poder abrir las fotos en formatos diferentes al png convirtiendolos en bytes.
def abrir_foto(ruta_foto):
    """
    Se abre la foto desde la ruta (que debe ser pasada por parametro) solo para lectura en formato binario, de esa manera obteniendo los bytes respectivos de la imagen y 
    utilizando el PIL se lee y se la reacomoda en un tamaño de 200x200, guardandandola y enviando a traves del return los bytes de la imagen.
"""
    try:
        with open(ruta_foto, 'rb') as file:
            img_bytes = file.read()
            image = Image.open(io.BytesIO(img_bytes))
            image.thumbnail((200, 200))
            bio = io.BytesIO()
            image.save(bio, format='PNG')
        return bio.getvalue()
    except FileNotFoundError:
        sg.popup ("Error: No se encontró la imagen en la ruta especificada")
    except Exception as e:
        sg.popup ("Error desconocido: ",str(e))
    return None    
posicion_en_lista = [0,0,0,0]
i = 0

def ini():
    #Inicializamos los botones con los primeros elementos de la lista y/o elementos vacios. SE USA AL MOMENTO DEL INICIO. SE CREO POR EL CASO EN QUE EL TAMAÑO DE LA LISTA SEA MENOR O IGUAL A 4
    def inicializar_botones():
        """
        Se inicializan los botones en vacio, y se cargan hasta 4 botones. 
        """
        global i
        #Se inicializan los botones en vacios.
        botones = [0,0,0,0]
        #Si hay elementos en la lista se cargan los botones.
        if (len(lista_imagenes) > i):
            botones[0] = sg.Button(image_data=abrir_foto(lista_imagenes[i]['Foto']), image_size=(150,150),border_width=0, key='boton0')
            posicion_en_lista[0] = i
            i+=1
            if (len(lista_imagenes) > i):
                botones[1] = sg.Button(image_data=abrir_foto(lista_imagenes[i]['Foto']), image_size=(150,150),border_width=0, key='boton1')
                posicion_en_lista[1] = i
                i+=1
                if (len(lista_imagenes) > i):
                    botones[2] = sg.Button(image_data=abrir_foto(lista_imagenes[i]['Foto']), image_size=(150,150),border_width=0, key='boton2')
                    posicion_en_lista[2] = i
                    i+=1
                    if (len(lista_imagenes) > i):
                        botones[3] = sg.Button(image_data=abrir_foto(lista_imagenes[i]['Foto']), image_size=(150,150),border_width=0, key='boton3')
                        posicion_en_lista[3] = i
                        i+=1
                    else:
                        botones[3] =sg.Button(image_size=(150,150),border_width=0, key='boton3', visible=False)
                        i = 0
                else:
                    botones[2] = sg.Button(image_size=(150,150),border_width=0, key='boton2', visible=False)
                    botones[3] = sg.Button(image_size=(150,150),border_width=0, key='boton3', visible=False)
                    i = 0
            else:
                botones[1] = sg.Button(image_size=(150,150),border_width=0, key='boton1', visible=False)
                botones[2] = sg.Button(image_size=(150,150),border_width=0, key='boton2', visible=False)
                botones[3] = sg.Button(image_size=(150,150),border_width=0, key='boton3', visible=False)
                i = 0 
        else:
            botones[0] = sg.Button(image_size=(150,150),border_width=0, key='boton0', visible=False)
            botones[1] = sg.Button(image_size=(150,150),border_width=0, key='boton1', visible=False)
            botones[2] = sg.Button(image_size=(150,150),border_width=0, key='boton2', visible=False)
            botones[3] = sg.Button(image_size=(150,150),border_width=0, key='boton3', visible=False)
        return botones



    #Verifica que no esta vacio el archivo y sino lo esta verifica cuantos elementos tiene, muestrando y actualizando los botones. SE UTILIZA CUANDO EL TAMAÑO DE LA LISTA ES MAYOR A 4
    def mostrar_lista():
        """"
        Se cargan los botones que siguen en la lista. En el caso de que haya menos de 4 elementos a mostrar se invisibilizan los que no estan en uso y se cargan los botones finales. 
        """
        global i
        #Se verifica que el iterador de la lista_imagenes no sea igual a su tamaño en cada posicion. En el caso que sea igual el iterador se inicializa en 0 y se deshabilitan los botones siguientes.  
        if (len(lista_imagenes) > i): 
            #Si se llego al final, para volver a ver los elementos de nuevo se habilitan.
            if (i < 4):  
                window['boton0'].update(visible=True)
                window['boton1'].update(visible=True)
                window['boton2'].update(visible=True)
                window['boton3'].update(visible=True)  
            window['boton0'].update(image_data=abrir_foto(lista_imagenes[i]['Foto']), image_size=(150,150))
            posicion_en_lista[0] = i
            i+=1
            window['num_pagina'].update(f'Pagina n° {(i // 4)+1}')
            if (len(lista_imagenes) > i):
                window['boton1'].update(image_data=abrir_foto(lista_imagenes[i]['Foto']), image_size=(150,150))
                posicion_en_lista[1] = i
                i+=1
                if (len(lista_imagenes) > i):
                    window['boton2'].update(image_data=abrir_foto(lista_imagenes[i]['Foto']), image_size=(150,150))
                    posicion_en_lista[2] = i
                    i+=1
                    if (len(lista_imagenes) > i):
                        window['boton3'].update(image_data=abrir_foto(lista_imagenes[i]['Foto']), image_size=(150,150))
                        posicion_en_lista[3] = i
                        i+=1
                        if (len(lista_imagenes) == i):  
                            i = 0                  
                    else:
                        window['boton3'].update(visible=False)
                        i = 0
                else:
                    window['boton2'].update(visible=False)
                    window['boton3'].update(visible=False)
                    i = 0
            else:
                window['boton1'].update(visible=False)
                window['boton2'].update(visible=False)
                window['boton3'].update(visible=False)
                i = 0 
        else:
            i = 0  

    if not (os.path.exists('perfiles.csv')):
        with open('perfiles.csv','w', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv)
            writer.writerow(['Timestamp','Nick','Operacion','Valores','Textos'])

    #Se verifica si el archivo existe, si es asi se lo abre en modo lectura. En el case de que el archivo no exista se lo abre en modo escritura y se crea la lista de imagenes vacia.
    if os.path.exists('perfiles.json'):
        with open('perfiles.json','r') as archivo:
            #Se verifica si el archivo esta vacio, si es asi se crea la lista de imagenes vacia. Si el archivo no esta vacio se carga lista_imagenes con los datos.
            if (os.stat('perfiles.json').st_size == 0):
                lista_imagenes=[]
            else:
                datos = json.load(archivo)
                lista_imagenes = list(map(lambda elem : elem,datos))
    else:
        with open('perfiles.json','w') as archivo:
            lista_imagenes=[]

    #Se crea boton_cerrar para utilizarlo como columna y asi posicionarlo en el costado derecho.
    boton_cerrar = [[sg.Button('Cerrar',size=(20, 2), button_color=('black', 'skyblue'), font=('Comis Sans MS', 12))]]

    #Se verifica que la lista_imagenes sea menor a 4. Si esto es verdadero se crea el texto con la pagina correcta y con el boton "Ver más" desactivado. En el caso de que sea mayor a 4 se habilita el boton "Ver más" y se crea el texto con la pagina correcta. 
    if (len(lista_imagenes) > 4):
        numero_pagina = [sg.Text(f'Pagina n° {(i // 4)+1}', key='num_pagina', text_color='Black',font=('Times New Roman', 15))]
        boton_ver_mas = [[sg.Button("Ver más",size=(20, 2), button_color=('black', 'skyblue'), font=('Helvetica', 12),key='ver_mas',disabled=False),
                sg.Button("Agregar perfil",size=(20, 2), button_color=('black', 'skyblue'), font=('Helvetica', 12),key='agregar_perfil')]]
    else:
        numero_pagina = [sg.Text(f'Pagina n° {(i // 4)+1}', key='num_pagina', text_color='Black',font=('Times New Roman', 15))]
        boton_ver_mas = [[sg.Button("Ver más",size=(20, 2), button_color=('black', 'skyblue'), font=('Helvetica', 12),key='ver_mas',disabled=True),
                sg.Button("Agregar perfil",size=(20, 2), button_color=('black', 'skyblue'), font=('Helvetica', 12),key='agregar_perfil')]]
        
    botones = inicializar_botones()

    ruta_fotos = os.path.join(os.getcwd(),"Fotos","fondo.png")

    layout = [[sg.Text('UNLP-Image', size=(50, 2), font=('Times New Roman', 75), text_color='Black', justification=("c"))],
            [numero_pagina],
            [botones],
            [boton_ver_mas],
            [sg.Button(image_data=abrir_foto(ruta_fotos),image_size=(150,150),border_width=0)],#se crea este boton para generar un espacio.
            [sg.Column(boton_cerrar, element_justification='rigth', expand_x=True)]]

    window = sg.Window('Inicio', layout, element_justification='c', size=(1366,768),resizable=True )

    while True:
        event,values = window.read()

        if event == ('Cerrar') or event == sg.WIN_CLOSED:
            break
        if event ==("agregar_perfil"):
            window.hide()
            per = perfil.agregar_perfil()
            #verifica si se uso el agregar perfil, porque puede entrar a crear perfil y no crear ningun perfil
            if (per != None):
                menu.me(per) #si se agrega un perfil va al menu
                #break
                
            window.UnHide()
        if event == ("ver_mas"):
            mostrar_lista()

        #Se verifica que boton se presionó Y se llama al menu enviando el perfil a traves de lista imagenes en la posicion dada por la lista posicion que guarda a que elemento apunta cada boton. sin importar los cambio, cuando retorna se sobreescribe.
        if (event == 'boton0'):
            window.hide()
            lista_imagenes[posicion_en_lista[0]] = menu.me(lista_imagenes[posicion_en_lista[0]])
            break
        elif (event == 'boton1'):
            window.hide()
            lista_imagenes[posicion_en_lista[1]] = menu.me(lista_imagenes[posicion_en_lista[1]])
            break
        elif (event == 'boton2'):
            window.hide()
            lista_imagenes[posicion_en_lista[2]] = menu.me(lista_imagenes[posicion_en_lista[2]])
            break
        elif (event == 'boton3'):
            window.hide()
            lista_imagenes[posicion_en_lista[3]] = menu.me(lista_imagenes[posicion_en_lista[3]])
            break
    window.close()
