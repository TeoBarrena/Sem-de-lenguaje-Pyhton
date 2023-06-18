import PySimpleGUI as sg

from imagenes_funciones.cargador_de_imagen import (
    cargador_de_imagen)

from imagenes_funciones.constantes_img import (
    RUTA_IMG_COLLAGE1,
    RUTA_IMG_COLLAGE2,
    RUTA_IMG_COLLAGE3,
    RUTA_IMG_COLLAGE4)


def seleccionar_collage():
    img_collage1 = cargador_de_imagen(RUTA_IMG_COLLAGE1, 300)
    img_collage2 = cargador_de_imagen(RUTA_IMG_COLLAGE2, 300)
    img_collage3 = cargador_de_imagen(RUTA_IMG_COLLAGE3, 300)
    img_collage4 = cargador_de_imagen(RUTA_IMG_COLLAGE4, 300)

    layout_generar_collage = [
        [
            sg.Button(
                image_data=img_collage1,
                button_color=(sg.theme_background_color(), sg.theme_background_color()),
                border_width=0,
                key='-COLLAGE1-',
                image_size=(300, 300),
                pad=(10, 10),
                expand_x=True
            ),
            sg.Button(
                image_data=img_collage2,
                button_color=(sg.theme_background_color(), sg.theme_background_color()),
                border_width=0,
                key='-COLLAGE2-',
                image_size=(300, 300),
                pad=(10, 10),
                expand_x=True
            ),
            sg.Button(
                image_data=img_collage3,
                button_color=(sg.theme_background_color(), sg.theme_background_color()),
                border_width=0,
                key='-COLLAGE3-',
                image_size=(300, 300),
                pad=(10, 10),
                expand_x=True
            ),
            sg.Button(
                image_data=img_collage4,
                button_color=(sg.theme_background_color(), sg.theme_background_color()),
                border_width=0,
                key='-COLLAGE4-',
                image_size=(300, 300),
                pad=(10, 10),
                expand_x=True
            )
        ]
    ]

    ventana = sg.Window('Generador de collage', layout_generar_collage)

    while True:
        evento, valores = ventana.read()

        if evento == sg.WIN_CLOSED:
            break

        if evento == '-COLLAGE1-':
            return "Collage1"

        if evento == '-COLLAGE2-':
            return "Collage2"

        if evento == '-COLLAGE3-':
            return "Collage3"

        if evento == '-COLLAGE4-':
            return "Collage4"

    ventana.close()
