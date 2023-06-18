from imagenes_funciones.cargador_de_imagen import cargador_de_imagen
from generador_collage.seleccionador_collage import seleccionar_collage
from generador_collage.funciones_collage import (
    buscar_nombre_collage,
    generar_titulo,
    get_collage_done,
    verificar_imagenes_collage)
from imagenes_funciones.csv_manager import guardar_en_logs
import PySimpleGUI as sg
import os

def vista_collage(perfil_id, dir_collage):

    design = seleccionar_collage()

    designs = { 
        "Collage1": 2,
        "Collage2": 2,
        "Collage3": 4,
        "Collage4": 3
    }

    max_images = designs.get(design)

    images_inputs = []
    for i in range(max_images):
        images_inputs.append([sg.Text(f"Imagen {i+1}:"), sg.FilesBrowse(key=f"-IMAGEN{i+1}-", enable_events=True)])


    layout = [
        [sg.Text("Seleccione las imagenes etiquetadas:")],
        [images_inputs],
        [sg.Text("Ingrese el título del collage:"), sg.Input(key="-TITLE-")],
        [sg.Image(key="-IMAGE-", size=(500, 500))],
        [sg.Button("Guardar collage", key="-GUARDAR-"), sg.Button("Actualizar", key="-ACTUALIZAR-")]
    ]

    ventana = sg.Window("Generador de collage", layout)

    while True:
        evento, valores = ventana.read()

        if evento == sg.WINDOW_CLOSED:
            break

        if evento == "-GUARDAR-":
            try:
                collage.save(collage_path)
                guardar_en_logs(perfil_id, "Nuevo Collage", [os.path.basename(ruta) for ruta in images], title)
                sg.popup("Collage guardado correctamente.")
            except:
                sg.popup("Genera un collage antes de guardar.")

        if evento == "-ACTUALIZAR-":
            images = []
            for i in range(max_images):
                image_key = f"-IMAGEN{i+1}-"
                image_path = valores[image_key]
                if image_path:
                    images.append(image_path)
            if len(images) == max_images:
                if verificar_imagenes_collage(images):
                    title = valores["-TITLE-"]
                    collage = get_collage_done(images, design)
                    if title:
                        title_box, title_box_position = generar_titulo(valores["-TITLE-"])
                        collage.paste(title_box, title_box_position)
                    file_name = buscar_nombre_collage(dir_collage)
                    collage_path = os.path.join(dir_collage, file_name)
                    collage.save(collage_path)
                    img_bytes = cargador_de_imagen(collage_path, 500)
                    ventana["-IMAGE-"].update(data=img_bytes)
                    os.remove(collage_path)     
                else:
                    sg.popup("Al menos una de las imágenes no está etiquetada en 'etiquetas.csv'.")
            else:
                sg.popup(f"Seleccione {max_images} imagenes para completar el collage.")                   

    ventana.close()
