import math

# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

def imprimir_hola_mundo(mensaje):
    print(mensaje)

hola_mundo = imprimir_hola_mundo("Hola mundo!")

# 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

def saludar_usuario(nombre, saludo = "Hola"):
    print (f"{saludo} {nombre}")

saludar = saludar_usuario("Marcos")

# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia} ")

presentacion = informacion_personal("Lina", "Berrone", 33, "Rosario")

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_ circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    area = (math.pi * radio) ** 2
    print(f"El area del circulo es {area}")

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    print(f"El perimetro del circulo es {perimetro}")


def validar_numero_positivo(mensaje, min = 0):
    n = int(input(f"{mensaje}: "))
    while n < min :
        n = int(input(f"ERROR. {mensaje}: "))
    return n


radio = validar_numero_positivo("Ingrese un numero positivo")
area_del_circulo = calcular_area_circulo(radio)
perimetro_del_circulo = calcular_perimetro_circulo(radio)


# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.


def palabra_plural_o_singular(palabra, cantidad):
    if cantidad > 1:
        palabra += "s"
    else:
        palabra = palabra
    return palabra
    
def segundos_a_horas(mensaje):
    segundos = int(input(f"{mensaje}: "))
    horas = segundos // 3600
    minutos = segundos // 60

    palabra_hora = palabra_plural_o_singular("hora", horas)
    palabra_minuto = palabra_plural_o_singular ("minuto", minutos)

    if segundos < 60:
        print(f"Los {segundos} segundos no llegan a ser ni un minuto, ingrese un numero mas alto a convertir")
    else:
        print(f"{segundos} segundos son {horas} {palabra_hora} y {minutos} {palabra_minuto}.")

conversor = segundos_a_horas("Ingrese una cantidad de segundos")

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range (1,11):
        print (f"{numero} x {i} = {i * numero}")

numero = validar_numero_positivo("Ingrese un numero positivo")
multiplicar = tabla_multiplicar(numero)


# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    division = a / b
    multiplicacion = a * b
    print (f"El resultado de las operaciones con {a} y {b} es : suma = {suma}, resta = {resta}, multiplicacion = {multiplicacion} y division = {division}")

def pedir_dos_datos(mensaje1, mensaje2):
    a = float(input(f"{mensaje1}"))
    b = float(input(f"{mensaje2}"))
    return a, b

a, b = pedir_dos_datos("Ingrese el primer numero", "Ingrese el segundo numero")
tupla = operaciones_basicas(a, b)


# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    peso = int(peso)
    imc = peso / (altura ** 2)
    print(f"Su indice de masa corporal (IMC) es {imc}")

a, b = pedir_dos_datos("Ingrese su peso en kg", "Ingrese su altura en metros")
IMC = calcular_imc(a, b)

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_fahrenheit(celsius):
    farenheit = (9/5) * celsius + 32
    print(f"Los {celsius} grados Celsius equivalen a {farenheit} grados Farenheit")

def pedir_dato(mensaje):
    dato = int(input(mensaje))
    return dato


gradosCelsius = pedir_dato("Ingrese los grados Celsius")
conversor_de_Celsius_a_Farenheit = celsius_a_fahrenheit(gradosCelsius)

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

def pedir_tres_datos(mensaje1, mensaje2, mensaje3):
    a = float(input(f"{mensaje1}"))
    b = float(input(f"{mensaje2}"))
    c = float(input(f"{mensaje3}"))
    return a, b, c

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    print(f"El promedio de {a}, {b}, {c} da como resultado {promedio}")

a, b, c = pedir_tres_datos("Ingrese el primer numero ", "Ingrese el segundo numero ", "Ingrese el tercer numero ")
promedio = calcular_promedio(a, b, c)
