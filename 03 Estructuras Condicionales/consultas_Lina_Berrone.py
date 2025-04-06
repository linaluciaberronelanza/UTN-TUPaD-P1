#EJERCICIOS CLASE CONSULTA
# 04/04
numeroA = int(input("Ingrese un numero entero"))
numeroB = int(input("Ingrese un numero entero"))
numeroC = int(input("Ingrese un numero entero"))

if (numeroA % 2 == 0) and (numeroB %2 == 0) and (numeroC % 2 == 0):
    print("Todos los numeros son pares")
elif (numeroA % 2 == 0) or (numeroB %2 == 0) or (numeroC % 2 == 0):
    print("Algunos numeros son pares")
else:
    print("Ninguno de los numeros son pares") 