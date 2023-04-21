import PySimpleGUI as sg

def mostrar_perfiles(lista):
    # Definir el diseño de la ventana
    layout = [[sg.Text("Usuarios")],
              [sg.Listbox(values=lista, size=(50, len(lista)), key="-LIST-")],
              [sg.Button("Cerrar")]]
    
    # Crear la ventana
    window = sg.Window("Mostrar lista", layout)
    while True:
        event,values = window.read()

        if event == "Cerrar" or event == sg.WINDOW_CLOSED:
            break
        
    window.close()

def agregar_perfil(lista):
    layout = [[sg.Text('Nuevo Perfil',font=('Helvetica',15)),sg.Button('Volver',pad=(150,50),size=(8,2),button_color=('grey'))],
          [sg.Text('Nick o alias',font=('Helvetica',10))],
          [sg.InputText()],
          [sg.Text('Nombre',font=('Helvetica',10))],
          [sg.InputText()],
          [sg.Text('Edad',font=('Helvetica',10))],
          [sg.Input()],
          [sg.Text('Genero autopercibido',font=('Helvetica',10))],
          [sg.Combo(['Masculino','Femenino'],default_value='Selecciona una opcion',key='Genero',size=(30,1))], #combo es una lista desplegable
          [sg.Button("",size=(2,1)),sg.Text("Otro")],
          [sg.Input("Complete el genero",key = 'Genero')],#arreglar
          [sg.Button('Guardar',pad=(250,50),size=(8,2),button_color=('sky blue'))]]
    window= sg.Window("Crear nuevo perfil",layout,margins=(100,100))
    while True:
        event,values = window.read()

        if event=="CANCELAR" or event== sg.WINDOW_CLOSED or event == 'Volver':
            break
        #if event =="Otro":
         #   genero = values[4]
        #else:
         #   genero = values['Genero']

        if event=='Guardar':
            alias = values[0]
            nombre=values[1]
            edad = values[2]
            genero = values['Genero']
            #print(f"El genero es {genero}")#para verificar
            lista.append((nombre,edad,alias,genero))
            #mostrarPerfil(alias,nombre,edad)
            break
    window.close()
    return lista
