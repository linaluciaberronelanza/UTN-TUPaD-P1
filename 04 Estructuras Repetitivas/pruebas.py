for  i in range(3):
    for j in range(2):
            print( i, j)


palabraUnicode = input("Ingrese una palabra: ")
acumulador = 0

for b in range(len(palabraUnicode)):
    acumulador += ord(palabraUnicode[b])

print("La suma de los valores Unicode es:", acumulador)