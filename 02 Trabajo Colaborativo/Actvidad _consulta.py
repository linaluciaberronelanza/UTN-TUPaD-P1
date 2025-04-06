""" Un automóvil debe realizar un viaje en el que prevé hacer tres paradas en estaciones de servicio para cargar combustible.
Se desea un programa que solicite al usuario la cantidad de litros cargados y el importe del litro de combustible de cada parada y muestre:
A) El importe a pagar en cada estación de servicio.
B) El importe a pagar total en el viaje y la cantidad de litros cargados. """

importeNafta = float(input("Ingrese el valor del litro de nafta: "))

litrosCargados1 = float(input("Ingrese cuántos litros cargó en la primera estación: "))
importeTotal1 = importeNafta * litrosCargados1
print(f"El total de litros cargados en la primera estación es: {litrosCargados1} y el importe es {importeTotal1}")

litrosCargados2 = float(input("Ingrese cuántos litros cargó en la segunda estación: "))
importeTotal2 = importeNafta * litrosCargados2
print(f"El total de litros cargados en la segunda estación es: {litrosCargados2} y el importe es {importeTotal2}")

litrosCargados3 = float(input("Ingrese cuántos litros cargó en la tercera estación: "))  # Corrección aquí
importeTotal3 = importeNafta * litrosCargados3

importeTotalFinal = importeTotal1 + importeTotal2 + importeTotal3

print(f"El total de litros cargados en la tercera estación es: {litrosCargados3} y el importe es {importeTotal3}.")
print(f"El importe total de todas las estaciones es: {importeTotalFinal}")