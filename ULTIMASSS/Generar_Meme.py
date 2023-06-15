import PySimpleGUI as sg
import os,io
from PIL import Image
sg.theme ('LightGrey4')

ruta_foto = os.path.join(os.getcwd(),"Fotos","Fondo_Meme.png")

def meme():
    boton_volver = [[sg.Button("< Volver", size=(20, 2), button_color=('black', 'skyblue'), font=('Helvetica', 12),key='volver')]]
    boton_guardar = [[sg.Button('Guardar', size=(20, 2), button_color=('black', 'skyblue'), font=('Helvetica', 12))]]

    columna= [sg.Column(boton_volver, element_justification='left', expand_x=True),
            sg.Column(boton_guardar, element_justification='rigth', expand_x=True)]
        
        #layout
    layout = [[sg.Text('Generar Meme', size=(20, 1), font=('Times New Roman', 75), text_color='Black', justification=("c"))],
            [sg.Image(filename=ruta_foto,key='-VISUAL_IMAGE-',size=(400,400),subsample=3)],
            [sg.Button("Seleccionar imagen",key='-IMAGE-',button_color=('black', 'skyblue'), font=('Helvetica', 12),size=(15,2)),
            sg.Button("Insertar Texto",key='-TEXT-',button_color=('black', 'skyblue'), font=('Helvetica', 12),size=(15,2))],
            [columna]]

    window = sg.Window('',layout, element_justification='c', size=(1366,768), resizable=True )

    while True:
        event,values = window.read()

        if event == ('volver') or event == sg.WIN_CLOSED:
            break
        if event == '-IMAGE-':
            ruta_imagen = sg.popup_get_file('Seleccionar avatar', no_window=True, file_types=(('Imagenes', '*.png *.jpg *.jpeg *.gif *.bmp *.tiff'),))
            if ruta_imagen:
                try:
                    with open(ruta_imagen, 'rb') as file:
                        img_bytes = file.read()
                        image = Image.open(io.BytesIO(img_bytes))
                        image.thumbnail((400, 400))
                        bio = io.BytesIO()
                        image.save(bio, format='PNG')
                        window['-VISUAL_IMAGE-'].update(data=bio.getvalue())
                    window['-IMAGE-'].update("Cambiar Imagen")
                except Exception as e:
                    sg.popup_error(f'Error al cargar la imagen: {e}')
    window.close()