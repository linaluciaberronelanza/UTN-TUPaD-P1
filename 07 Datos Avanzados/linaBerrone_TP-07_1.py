# 1) Dado el diccionario precios_frutas precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)
# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800 
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)
# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios. 
lista1 = list(precios_frutas.keys())
print(lista1)
# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe. Ejemplo:

guia = {}
for i in range(5):
    nombre = input("Ingresa un nombre: ")
    telefono = input("Ingresa un número de teléfono asociado a ese nombre: ")
    guia[nombre] = telefono

consulta = input("¿Qué nombre deseas buscar?: ")
if consulta in guia:
    print(f"El número de {consulta} es: {guia[consulta]}")
else:
    print("Ese contacto no existe.")
    
# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra. Ejemplo: 
# Solicitar al usuario una frase
frase = input("Escribí una frase: ")

palabras = frase.lower().split()
palabras_unicas = set(palabras)
conteo_palabras = {}

for palabra in palabras:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1

print("Palabras únicas:", palabras_unicas)
print("Cantidad de apariciones de cada palabra:", conteo_palabras)

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno. Ejemplo: 
# Crear un diccionario para guardar alumnos y sus notas
alumnos = {}

for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno: ")
    notas_ingresadas = input(f"Ingresá 3 notas para el alumno, separadas por espacio: ")
    notas_lista = [int(n) for n in notas_ingresadas.split()]
    
    alumnos[nombre] = tuple(notas_lista)
    promedio = sum(notas_lista) / len(notas_lista)
    print(f"{nombre}: promedio = {promedio}")
        
# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}

lista1 = list(parcial1)
lista2 = list(parcial2)

for numero in lista1:
    if numero in lista2:
        print(f"Los alumnos que aprobaron ambos son {numero}")

for numero in lista1:
    if numero not in lista2:
        print(f"Los alumnos que aprobaron solo el segundo parcial son {numero}")
for numero in lista2:
    if numero not in lista1:
        print(f"Los alumnos que aprobaron solo el primer parcial son {numero}")

todos = []
for numero in lista1:
    if numero not in todos:
        todos.append(numero)
for numero in lista2:
    if numero not in todos:
        todos.append(numero)
print(f"Aprobaron al menos un parcial:{todos}")

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe. 
def gestionar_stock():
    stock = {"pan": 20,"leche": 15,"arroz": 10}

    producto = input("Ingresá el nombre del producto que querés consultar: ").lower()

    if producto in stock:
        print(f"Stock actual de {producto}: {stock[producto]}")
        agregar = input("¿Querés agregar unidades? (s/n): ").lower()
        if agregar == 's':
            cantidad = int(input("¿Cuántas unidades querés agregar?: "))
            stock[producto] += cantidad
            print(f"Nuevo stock de {producto}: {stock[producto]}")
    else:
        print(f"{producto} no está en el sistema.")
        nuevo = input("¿Querés agregarlo? (s/n): ").lower()
        if nuevo == 's':
            cantidad = int(input("¿Cuántas unidades tiene?: "))
            stock[producto] = cantidad
            print(f"{producto} agregado con {cantidad} unidades.")

gestionar_stock()

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. Ejemplo:
# Permití consultar qué actividad hay en cierto día y hora. 
agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("martes", "15:30"): "Clase de inglés",
    ("viernes", "08:00"): "Entrenamiento"
}

dia = input("Ingresá el día: ").lower()
hora = input("Ingresá la hora (ej: 10:00): ")

clave = (dia, hora)

if clave in agenda:
    print(f"Actividad programada: {agenda[clave]}")
else:
    print("No hay actividad programada en ese día y hora.")

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores. Ejemplo:
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}

capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

print("Diccionario invertido (capital -> país):")
for capital, pais in capitales_paises.items():
    print(f"{capital}: {pais}")