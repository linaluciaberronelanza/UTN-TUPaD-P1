import random

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for cont in range(-1, 100):
    print(cont+1)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

num = int(input("Ingrese un numero entero"))
contA = 0

while num > 0:
    num //= 10
    contA += 1

print(contA) 

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

valor1 = int(input("Ingrese el primer número: "))
valor2 = int(input("Ingrese el segundo número: "))

if valor1 < valor2:
    menor = valor1
    mayor = valor2
else:
    menor = valor2
    mayor = valor1

sumatoria = 0


for a in range(menor + 1, mayor):
    sumatoria += a

print("La suma de los valores entre", menor, "y", mayor, "es:", sumatoria)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

suma = 0
numero = int(input("Ingrese un número entero (0 para salir): "))

while numero != 0:
    suma += numero
    numero = int(input("Ingrese otro número (0 para salir): "))

print("La suma de los valores es:", suma)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

numero_aleatorio = random.randint(0, 9)

contadorB = 0
numeroIngresado = int('-inf')  


while numeroIngresado != numero_aleatorio:
    numeroIngresado = int(input("Adivine el número entre 0 y 9: "))
    contadorB += 1
    if numeroIngresado != numero_aleatorio:
        print("Incorrecto, intenta de nuevo.")

print ("Has acertado el numero en la vuelta", contadorB)

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for u in range (100, -1, -2):
    print (u)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

valorUsuario = int(input("Ingrese un valor mayor a 0: "))

if valorUsuario > 0:
    sumatoria = 0
    for i in range(0, valorUsuario + 1):
        sumatoria += i
    print("La suma de los valores entre 0 y", valorUsuario, "es:", sumatoria)
else:
    print("Ingrese un valor válido mayor a 0.")

    # 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

par = 0
impar = 0
positivo = 0
negativo = 0

for b in range (0, 100):
    numeroIngresado = int(input("Ingrese un numero"))
    if numeroIngresado % 2 == 0: 
        par += 1
    elif numeroIngresado % 2 != 0:
        impar += 1
    
    if numeroIngresado >= 0:
        positivo += 1
    elif numeroIngresado < 0:
        negativo += 1

print("La cantidad de numeros pares es: ", par, "la de impares es: ", impar, "la de negativos es: ", negativo, "y la de positivos es: ", positivo)

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

sumaA = 0 

for c in range(100):
    numeroAB = int(input("Ingrese un número: "))
    sumaA += numeroAB

media = sumaA / 100
print("La media es:", media)

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero123 = int(input("Ingrese un número: "))
numeroInvertido = 0

while numero123 != 0:
    digito = numero123 % 10             
    numeroInvertido = numeroInvertido * 10 + digito 
    numero123 = numero123 // 10      

print("El número invertido es:", numeroInvertido)