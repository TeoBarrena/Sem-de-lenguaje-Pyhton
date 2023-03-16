from random import choice, randrange
from datetime import datetime
# Operadores posibles
operators = ["+", "-", "*", "//"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
cantCorrectas = 0 #defino variable para las correctas
cantIncorrectas = 0 #defino variable para las incorrectas
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
for i in range(0, times):
    # Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)

    # Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    # Le pedimos al usuario el resultado
    result = input("resultado: ")
    if operator == "+":
        res = number_1 + number_2
    elif operator == "-":
        res = number_1 + number_2
    elif operator == "*":
        res = number_1 * number_2
    else:
        res = number_1 // number_2
    if int(result) == res: #aca se convierte a entero el valor de result que esta como string
        print("Correcto!")
        cantCorrectas +=1 
    else:
        print("Incorrecto")
        cantIncorrectas +=1
# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")
print(f"\n Tuviste {cantCorrectas} respuestas correctas")
print(f"\n Tuviste {cantIncorrectas} respuestas incorrectas")
