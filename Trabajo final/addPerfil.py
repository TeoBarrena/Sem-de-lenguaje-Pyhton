import PySimpleGUI as sg

#def mostrarPerfil(lista):
 #   layout=[[sg.Text('Usuarios registrados:')],[sg.Button('Cerrar')][sg.Output(size=(30,3))]]
  #  ventana= sg.Window("",layout,margins=(100,100))
   # while True:
    #    event,values =ventana.read()
     #   for elem in lista:
      #      print(elem[0])
       # if event=='Cerrar' or event == sg.WINDOW_CLOSED :
       #     break
    #ventana.close()
    #sg.Popup(f"El usuario {alias}, tiene {edad} años y su nombre es: {nombre}")


def agregar_perfil(lista):
    layout = [[sg.Text('Nuevo Perfil')],
          [sg.Text('Nick o alias')],
          [sg.InputText()],
          [sg.Text('Nomber')],
          [sg.InputText()],
          [sg.Text('Edad')],
          [sg.Input()],
          [sg.Text('Genero autopercibido')],
          #votacion
          [sg.Button('ok')],
          [sg.Button('cancelar')]]
    window= sg.Window("Crear nuevo perfil",layout,margins=(100,100))
    while True:
        event,values = window.read()

        if event=="cancelar" or event== sg.WINDOW_CLOSED:
            break
        if event=='ok':
            alias = values[0]
            nombre=values[1]
            edad = values[2]
            lista.append((nombre,edad,alias))
            #mostrarPerfil(alias,nombre,edad)
    
        window.close()
    return lista

