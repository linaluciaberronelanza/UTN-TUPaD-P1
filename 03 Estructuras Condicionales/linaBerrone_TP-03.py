import statistics, random

# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 

edadUsuario = int(input("Ingrese su edad: "))
if edadUsuario >= 18:
    print("Es mayor de edad") 
else:
    print("Es menor de edad")           

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”. 

notaUsuario = int(input("Ingrese la nota como numero entero: "))
if notaUsuario >= 6:
    print("Aprobado") 
else:
    print("Desaprobado") 

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar. 

parNumero = int(input("Ingrese un numero par: "))
if parNumero % 2 == 0 :
    print("Ha ingresado un número par") 
else:
    print("Por favor, ingrese un número par") 

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.

edadPersona = int(input("Ingrese su edad como numero entero: "))
if (edadPersona >= 0) and (edadPersona < 12):
    print("La persona es un niño/a") 
elif (edadPersona >= 12) and (edadPersona < 18):
    print("La persona es un Adolescente") 
elif (edadPersona >= 18) and (edadPersona < 30):
    print("La persona es un Adulto/a joven")
elif (edadPersona >= 30): 
    print("La persona es un Adulto/a mayor")
else:
    pass

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string. 

contraseñaCuenta = input("Ingrese una contraseña entre 8 y 14 caracteres: ")
if (len(contraseñaCuenta) >= 8) and (len(contraseñaCuenta) <= 14) :
    print("Ha ingresado una contraseña correcta") 
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres") 


# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el siguiente:
""" #  from statistics import mode, median, mean 
# mi_lista = [1,2,5,5,3] 
# mean(mi_lista)  """
# En la documentación oficial se puede encontrar más información sobre este paquete: https://docs.python.org/es/3.8/library/statistics.html. La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio: 
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda. 
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda. 
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma: 
""" # import random numeros_aleatorios = [random.randint(1, 100) for i in range(50)] """
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria.

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
moda = statistics.mode(numeros_aleatorios)

if (media > mediana) and (mediana > moda):
    print("El sesgo es positivo")
elif (media < mediana) and (mediana < moda):
    print("El sesgo es negativo")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("No se puede determinar un sesgo claro")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

palabraUsuario = input("Ingrese una palabra: ")
ultimaLetra = palabraUsuario[-1]

if (ultimaLetra == "a" or ultimaLetra == "e" or ultimaLetra == "i" or ultimaLetra == "o" or ultimaLetra == "u"
    or ultimaLetra == "A" or ultimaLetra == "E" or ultimaLetra == "I" or ultimaLetra == "O" or ultimaLetra == "U"):
    print(palabraUsuario + "!")
else:
    print(palabraUsuario)


# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombreIngresado = input("Ingrese su nombre: ")
opcion = input("Ingrese 1 , 2 o 3: ")
if opcion == "1":
    print(nombreIngresado.upper())
elif opcion == "2":
    print (nombreIngresado.lower())
elif opcion == "3":
    print(nombreIngresado.title())
else:
    print("Ingrese una opcion valida")

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes 
# categorías según la escala de Richter e imprima el resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitudTerremoto = float(input("Ingrese la magnitud del terremoto segun escala Ritcher (entre 1 y 7) "))
if magnitudTerremoto < 3:
    print("Muy leve (imperceptible)")
elif (magnitudTerremoto >= 3) and (magnitudTerremoto < 4):
    print ("Leve (ligeramente perceptible)")
elif (magnitudTerremoto >= 4) and (magnitudTerremoto < 5):
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif (magnitudTerremoto >= 5) and (magnitudTerremoto < 6):
    print("Fuerte (puede causar daños en estructuras débiles)")
elif (magnitudTerremoto >= 6) and (magnitudTerremoto < 7):
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitudTerremoto >= 7:
    print("Extremo (puede causar graves daños a gran escala)")
else:
    print("Ingrese una opcion valida")


# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año Periodo del año
#                                            Estación en el hemisferio norte Estación en el hemisferio sur
# Desde el 21 de diciembre hasta el 20 de                    Invierno                    Verano
# marzo (incluidos)
# 
# Desde el 21 de marzo hasta el 20 de junio                  Primavera                    Otoño
# (incluidos)
# 
# Desde el 21 de junio hasta el 20 de                          Verano                    Invierno
# septiembre (incluidos)
#
# Desde el 21 de septiembre hasta el 20 de                     Otoño                     Primavera
# diciembre (incluidos)

# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano. 3



hemisferio = input("Ingrese en el hemisferio que se encuentra 'N' para Norte y 'S' para Sur")
mesDelAño = input("Ingrese el mes del año")
diaDelMes = int(input("Ingrese el dia con numeros"))

if (mesDelAño == "Enero") or (mesDelAño == "enero") or (mesDelAño == "ENERO") or (mesDelAño == "1"):
    print("Ingreso enero")
    mesDelAño = 1
elif (mesDelAño == "febrero") or (mesDelAño == "FEBRERO") or (mesDelAño == "Febrero") or (mesDelAño == "2"):
    print("Ingreso febrero")
    mesDelAño = 2
elif (mesDelAño == "marzo") or (mesDelAño == "MARZO") or (mesDelAño == "Marzo") or (mesDelAño == "3"):
    print("Ingreso marzo")
    mesDelAño = 3
elif (mesDelAño == "abril") or (mesDelAño == "ABRIL") or (mesDelAño == "Abril") or (mesDelAño == "4"):
    print("Ingreso abril")
    mesDelAño = 4
elif (mesDelAño == "Mayo") or (mesDelAño == "mayo") or (mesDelAño == "MAYO") or (mesDelAño == "5"):
    print("Ingreso mayo")
    mesDelAño = 5
elif (mesDelAño == "junio") or (mesDelAño == "JUNIO") or (mesDelAño == "Junio") or (mesDelAño == "6"):
    print("Ingreso junio")
    mesDelAño = 6
elif (mesDelAño == "julio") or (mesDelAño == "JULIO") or (mesDelAño == "Julio") or (mesDelAño == "7"):
    print("Ingreso julio")
    mesDelAño = 7
elif (mesDelAño == "agosto") or (mesDelAño == "AGOSTO") or (mesDelAño == "Agosto") or (mesDelAño == "8"):
    print("Ingreso agosto")
    mesDelAño = 8
elif (mesDelAño == "septiembre") or (mesDelAño == "SEPTIEMBRE") or (mesDelAño == "Septiembre") or (mesDelAño == "9"):
    print("Ingreso septiembre")
    mesDelAño = 9
elif (mesDelAño == "octubre") or (mesDelAño == "OCTUBRE") or (mesDelAño == "Octubre") or (mesDelAño == "10"):
    print("Ingreso octubre")
    mesDelAño = 10
elif (mesDelAño == "noviembre") or (mesDelAño == "NOVIEMBRE") or (mesDelAño == "Noviembre") or (mesDelAño == "11"):
    print("Ingreso noviembre")
    mesDelAño = 11
elif (mesDelAño == "diciembre") or (mesDelAño == "DICIEMBRE") or (mesDelAño == "Diciembre") or (mesDelAño == "12"):
    print("Ingreso diciembre")
    mesDelAño = 12
else:
    print("Ingrese un mes del año valido")

if (hemisferio == "N") or (hemisferio == "n"):
        print(f"Usted ha ingresado hemisferio Norte")
        if ((mesDelAño == 12) and (diaDelMes >= 21)) or (mesDelAño == 1 or mesDelAño == 2) or ((mesDelAño == 3) and (diaDelMes <= 20)):
            print("Esta en invierno")
        if ((mesDelAño == 3) and (diaDelMes >= 21)) or (mesDelAño == 4 or mesDelAño == 5) or ((mesDelAño == 6) and (diaDelMes <= 20)):
            print("Esta en primavera")
        if ((mesDelAño == 6) and (diaDelMes >= 21)) or (mesDelAño == 7 or mesDelAño == 8) or ((mesDelAño == 9) and (diaDelMes <= 20)):
            print("Esta en verano")
        if ((mesDelAño == 9) and (diaDelMes >= 21)) or (mesDelAño == 10 or mesDelAño == 11) or ((mesDelAño == 12) and (diaDelMes <= 20)):
            print("Esta en otoño")
        else:
            pass
elif (hemisferio == "S") or (hemisferio == "s"):
        print(f"Usted ha ingresado hemisferio Sur")
        if ((mesDelAño == 12) and (diaDelMes >= 21)) or (mesDelAño == 1 or mesDelAño == 2) or ((mesDelAño == 3) and (diaDelMes <= 20)):
            print("Esta en verano")
        if ((mesDelAño == 3) and (diaDelMes >= 21)) or (mesDelAño == 4 or mesDelAño == 5) or ((mesDelAño == 6) and (diaDelMes <= 20)):
            print("Esta en otoño")
        if ((mesDelAño == 6) and (diaDelMes >= 21)) or (mesDelAño == 7 or mesDelAño == 8) or ((mesDelAño == 9) and (diaDelMes <= 20)):
            print("Esta en invierno")
        if ((mesDelAño == 9) and (diaDelMes >= 21)) or (mesDelAño == 10 or mesDelAño == 11) or ((mesDelAño == 12) and (diaDelMes <= 20)):
            print("Esta en primavera")
        else:
            pass
else:
    print("Ingrese un hemisferio valido")