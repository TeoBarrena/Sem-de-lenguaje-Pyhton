import csv
from PIL import Image, ImageDraw, ImageFont
import os

collage_width = 800
collage_height = 600

def buscar_nombre_collage(dir_collage): #Busca el nombre del collage para guardarlo.
    file_name = "collage.png"
    contador = 1
    name, ext = os.path.splitext(file_name)
    while os.path.exists(os.path.join(dir_collage, file_name)):
        file_name = f"{name}({contador}){ext}"
        contador += 1
    return file_name

def generar_titulo(title): #Genera un rectangulo blanco con la palabra pasada por parametro.
        title_box_height = 50
        title_box_color = (255, 255, 255)
        title_box_position = (0, collage_height - title_box_height)
        title_box = Image.new("RGB", (collage_width // 2, title_box_height), title_box_color)
        font_size = 30
        font = ImageFont.truetype("arial.ttf", font_size)
        draw = ImageDraw.Draw(title_box)
        text_width, text_height = draw.textsize(title, font=font)
        text_position = ((collage_width // 2 - text_width) // 2, (title_box_height - text_height) // 2)
        draw.text(text_position, title, fill="black", font=font)
        return title_box, title_box_position

def get_collage_done(images, design): #Forma el collage con sus imagenes segun el collage elegido previamente.

    if design == "Collage1":
        image1 = Image.open(images[0])
        image1 = image1.resize((collage_width, collage_height // 2))

        image2 = Image.open(images[1])
        image2 = image2.resize((collage_width, collage_height // 2))

        collage = Image.new("RGB", (collage_width, collage_height), "white")
        collage.paste(image1, (0, 0))
        collage.paste(image2, (0, collage_height // 2))

    if design == "Collage2":
        image1 = Image.open(images[0])
        image1 = image1.resize((collage_width // 2, collage_height))

        image2 = Image.open(images[1])
        image2 = image2.resize((collage_width // 2, collage_height))

        collage = Image.new("RGB", (collage_width, collage_height), "white")
        collage.paste(image1, (0, 0))
        collage.paste(image2, (collage_width // 2, 0))

    if design == "Collage3":
        image1 = Image.open(images[0])
        image1 = image1.resize((collage_width // 2, collage_height // 2))

        image2 = Image.open(images[1])
        image2 = image2.resize((collage_width // 2, collage_height // 2))

        image3 = Image.open(images[2])
        image3 = image3.resize((collage_width // 2, collage_height // 2))

        image4 = Image.open(images[3])
        image4 = image4.resize((collage_width // 2, collage_height // 2))

        collage = Image.new("RGB", (collage_width, collage_height), "white")
        collage.paste(image1, (0, 0))
        collage.paste(image2, (collage_width // 2, 0))
        collage.paste(image3, (0, collage_height // 2))
        collage.paste(image4, (collage_width // 2, collage_height // 2))

    if design == "Collage4":
        image1 = Image.open(images[0])
        image1 = image1.resize((collage_width // 2, collage_height // 2))

        image2 = Image.open(images[1])
        image2 = image2.resize((collage_width // 2, collage_height // 2))

        image3 = Image.open(images[2])
        image3 = image3.resize((collage_width, collage_height // 2))

        collage = Image.new("RGB", (collage_width, collage_height), "white")
        collage.paste(image1, (0, 0))
        collage.paste(image2, (collage_width // 2, 0))
        collage.paste(image3, (0, collage_height // 2))

    return collage

def verificar_imagenes_collage(images): #Verifica que las imagenes pasadas por parametro se encuentren etiquetadas.
    etiquetas_file = "etiquetas.csv"

    if not os.path.isfile(etiquetas_file):
        raise FileNotFoundError(f"No se encontro el archivo '{etiquetas_file}'.")

    with open(etiquetas_file, "r") as file:
        reader = csv.reader(file)
        etiquetas = [os.path.basename(row[0]) for row in reader]

    for image_path in images:
        image_basename = os.path.basename(image_path)
        if image_basename not in etiquetas:
            return False

    return True
