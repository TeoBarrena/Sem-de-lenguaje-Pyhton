import PySimpleGUI as sg
import os
from PIL import Image
from PIL import ImageTk
from UnlpImage.rutas import IMPORT_DEFAULT
from UnlpImage.rutas import COLLAGE_DEFAULT
import UnlpImage.Funcionalidades.armado_collage_funcionalidades as ac

def layout(plantilla):

    extension_imagenes = [("Todos los archivos (*.*)", "*.*"), ("PNG (*.png)", "*.png"), ("JPG (*.jpg)", "*.jpg")]

    columna_1 = [
        [sg.Text('Generar Collage')],
        [sg.FileBrowse(button_text=f"IMAGEN {i}", key=f"-BUSCAR-IMAGEN-{i}-", size=(15, 1),enable_events=True, change_submits=True,
                        file_types=extension_imagenes, initial_folder= IMPORT_DEFAULT, metadata= info) for i, info in enumerate(plantilla["informacion"])]
    ]

    columna_2 = [
        [sg.Image(key="-IMAGEN-")]
    ]

    columna_3 = [
            [sg.Text("Ingresar titulo: "), sg.Input(key="-TITULO-"), sg.Button("Agregar", key="-AGREGAR-TITULO-")],
            [sg.Button("Guardar", key="-BOTON-GUARDAR-"), sg.Button('Volver', key ="-BOTON-VOLVER-")]
        ]

    general = [
                [sg.Column(columna_1,justification="center",pad=((0,0),(20,0)))],
                [sg.Column(columna_2,pad=(200, 40))],
                [sg.Column(columna_3,justification="center",pad=((0,0),(0,20)))]
            ]

    return [
        [sg.Column(layout=general, justification='center')],

    ]


def run(perfil, plantilla):
    window = sg.Window('Armado collage', layout(plantilla), resizable=True, finalize=True)


    collage = Image.new("RGB", (600, 600))   #Creo el collage
    window["-IMAGEN-"].update(data=ImageTk.PhotoImage(collage))
    nombres = [None] * int(plantilla["imagenes"])
    

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == '-BOTON-VOLVER-':
            break

        elif event.startswith("-BUSCAR-IMAGEN-"):
            info = window[event].metadata
            imagen_ruta = values[event]
            if ac.validar_imagen(imagen_ruta):
                nombres[int(info["codigo"])] = ac.obtener_nombre_imagen(imagen_ruta)
                collage = ac.pegar_imagen_en_collage(imagen_ruta, collage, info)
                try:
                    collage_copia = ac.agregar_titulo_al_collage(titulo, collage.copy())
                    window["-IMAGEN-"].update(data=ImageTk.PhotoImage(collage_copia))
                except:
                    window["-IMAGEN-"].update(data=ImageTk.PhotoImage(collage))
            else:
                sg.popup("La imagen seleccionada es invalida porque no se encuentra etiquetada.")

        elif event == "-AGREGAR-TITULO-":
            if (window["-TITULO-"].get() != ""):
                titulo = window["-TITULO-"].get()
                collage_copia = ac.agregar_titulo_al_collage(titulo, collage.copy())
                window["-IMAGEN-"].update(data=ImageTk.PhotoImage(collage_copia))
                window["-TITULO-"].update("")
            else:
                sg.popup("No se especifico un titulo.")

        elif event == "-BOTON-GUARDAR-":
            try:
                if (not None in nombres):
                    collage_copia.save(os.path.join(COLLAGE_DEFAULT, f"{titulo}.png"), "PNG")
                    ac.actualizar_log(perfil, nombres, titulo)
                else:
                    sg.popup("No se agregaron la cantidad de imagenes suficientes para completar el collage.")
            except:
                sg.popup("No se agrego un titulo a la imagen.")

    window.close()