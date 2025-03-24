import math

# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")

# # 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

radio = float(input("Ingrese el radio de un círculo: "))
area = (math.pi * radio) ** 2
perimetro = 2 * math.pi * radio
print(f"El área del círculo es {area} y el perímetro es {perimetro}.")


# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos son {horas} horas.")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

numero = int(input("Ingrese un numero entero: "))
tabla1 = numero * 1
tabla2 = numero * 2
tabla3 = numero * 3
tabla4 = numero * 4
tabla5 = numero * 5
tabla6 = numero * 6 
tabla7 = numero * 7
tabla8 = numero * 8
tabla9 = numero * 9
tabla10 = numero * 10
print(numero, "x 1 = ", tabla1)
print(numero, "x 2 = ", tabla2)
print(numero, "x 3 = ", tabla3)
print(numero, "x 4 = ", tabla4)
print(numero, "x 5 = ", tabla5)
print(numero, "x 6 = ", tabla6)
print(numero, "x 7 = ", tabla7)
print(numero, "x 8 = ", tabla8)
print(numero, "x 9 = ", tabla9)
print(numero, "x 10 = ", tabla10)

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero1 = int(input("Ingrese el primer numero entero distinto a 0"))
numero2 = int(input("Ingrese el segundo numero entero distinto a 0"))
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
print (f"El resultado de la suma de {numero1} y {numero2} es: {suma}")
print (f"El resultado de la resta de {numero1} menos {numero2} es: {resta}")
print (f"El resultado de la multiplicacion de {numero1} por {numero2} es: {multiplicacion}")
print (f"El resultado de la division de {numero1} entre {numero2} es: {division}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo:
# 𝐼𝑀𝐶 =𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔/(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2

peso = int(input("Ingrese su peso en kg"))
altura = float(input("Ingrese su altura en metros"))
imc = peso / (altura ** 2)
print(f"Su indice de masa corporal (IMC) es {imc}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢s + 32

gradosCelsius = float(input("Ingrese la temperatura en grados celsius"))
gradosFarenheit = (9/5) * gradosCelsius + 32
print(f"Los {gradosCelsius} grados Celsius equivalen a {gradosFarenheit} grados Farenheit")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

num1 = float(input("Ingrese el primer numero"))
num2 = float(input("Ingrese el segundo numero"))
num3 = float(input("Ingrese el tercer numero"))
promedio = (num1 + num2 + num3)/3
print (f"el promedio entre {num1}, {num2} y {num3} es {promedio}")

