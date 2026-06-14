# TPI - Gestion de Datos de Paises - Programación 1
# Grupo 205
# Integrantes:
#       Gustavo Ramon Parodi
#       Matheo Santiago Cardozo

import csv
import os

# Definición de funciones
def cargar_paises():
    lista = []

    # Retorno temprano en caso de que el archivo no se encuentre
    if not os.path.exists("paises.csv"):
        print("No se encontro el archivo paises.csv")
        return lista

    with open("paises.csv", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            if fila["nombre"].strip() == "" or fila["poblacion"].strip() == "" or fila["superficie"].strip() == "" or fila["continente"].strip() == "":
                print("Se ignoro una fila con datos incompletos")
                continue

            try:
                pais = {
                    "nombre": fila["nombre"].strip(),
                    "poblacion": int(fila["poblacion"].strip()),
                    "superficie": int(fila["superficie"].strip()),
                    "continente": fila["continente"].strip()
                }
                lista.append(pais)
            except ValueError as e:
                print(f"Se ignoro una fila con formato incorrecto: {e}")
    
    return lista


def guardar_paises(lista):
    try:
        with open("paises.csv", "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie", "continente"])
            escritor.writeheader()
            escritor.writerows(lista)
        print("Cambios guardados correctamente.")
    except:
        print("Error: {e}")


def mostrar_pais(pais):
    print("  Nombre     :", pais["nombre"])
    print("  Poblacion  :", pais["poblacion"])
    print("  Superficie :", pais["superficie"], "km2")
    print("  Continente :", pais["continente"])
    print("  -----------------------------------")


def mostrar_lista(lista):
    if not lista:
        print("No se encontraron paises con esos criterios.")
    else:
        print("\nSe encontraron", len(lista), "pais/es:\n")
        for p in lista:
            mostrar_pais(p)


def agregar_pais(lista):
    print("\n--- AGREGAR PAIS ---")

    nombre = input("Nombre del pais: ").strip().capitalize()
    if not nombre:
        print("El nombre no puede estar vacio.")
        return

    for p in lista:
        if p["nombre"].lower() == nombre.lower():
            print("Ya existe un pais con ese nombre.")
            return

    poblacion = input("Poblacion: ").strip()
    if not poblacion:
        print("La poblacion no puede estar vacia.")
        return
    if not poblacion.isdigit():
        print("La poblacion tiene que ser un numero entero mayor a cero.")
        return
    if int(poblacion) == 0:
        print("La poblacion tiene que ser mayor a cero.")
        return

    superficie = input("Superficie en km2: ").strip()
    if not poblacion:
        print("La superficie no puede estar vacia.")
        return
    if not superficie.isdigit():
        print("La superficie tiene que ser un numero entero mayor a cero.")
        return
    if int(superficie) == 0:
        print("La superficie tiene que ser mayor a cero.")
        return

    continente = input("Continente: ").strip()
    if not continente:
        print("El continente no puede estar vacio.")
        return

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": int(poblacion),
        "superficie": int(superficie),
        "continente": continente
    }
    lista.append(nuevo_pais)
    guardar_paises(lista)
    print("Pais ", nombre, " agregado correctamente.")


def actualizar_pais(lista):
    print("\n--- ACTUALIZAR PAIS ---")

    nombre = input("Nombre del pais a actualizar: ").strip()
    if not nombre:
        print("El nombre no puede estar vacio.")
        return

    for p in lista:
        if p["nombre"].lower() == nombre.lower():
            print("Pais encontrado: ", p["nombre"])

            nueva_poblacion = input("Nueva poblacion (actual: " + str(p["poblacion"]) + "): ").strip()
            if not nueva_poblacion or not nueva_poblacion.isdigit() or int(nueva_poblacion) <= 0:
                print("Valor de poblacion invalido.")
                return

            nueva_superficie = input("Nueva superficie (actual: " + str(p["superficie"]) + " km2): ").strip()
            if not nueva_superficie or not nueva_superficie.isdigit() or int(nueva_superficie) <= 0:
                print("Valor de superficie invalido.")
                return

            p["poblacion"] = int(nueva_poblacion)
            p["superficie"] = int(nueva_superficie)
            guardar_paises(lista)
            print("Pais actualizado correctamente.")
            return

    print("No se encontro ningun pais llamado", nombre)


def buscar_pais(lista):
    print("\n--- BUSCAR PAIS ---")

    termino = input("Ingresa el nombre o parte del nombre: ").strip()
    if not termino:
        print("Ingresa al menos un caracter para buscar.")
        return

    resultados = []
    for p in lista:
        if termino.lower() in p["nombre"].lower():
            resultados.append(p)

    mostrar_lista(resultados)


def filtrar_por_continente(lista):
    print("\n--- FILTRAR POR CONTINENTE ---")

    continente = input("Ingresa el continente: ").strip()
    if not continente:
        print("El continente no puede estar vacio.")
        return

    resultados = []
    for p in lista:
        if p["continente"].lower() == continente.lower():
            resultados.append(p)

    mostrar_lista(resultados)


def filtrar_por_poblacion(lista):
    print("\n--- FILTRAR POR RANGO DE POBLACION ---")

    minimo = input("Poblacion minima: ").strip()
    maximo = input("Poblacion maxima: ").strip()

    if not minimo.isdigit() or not maximo.isdigit():
        print("Los valores tienen que ser numeros enteros mayores a cero.")
        return

    minimo = int(minimo)
    maximo = int(maximo)

    if minimo > maximo:
        print("El minimo no puede ser mayor que el maximo.")
        return

    resultados = []
    for p in lista:
        if minimo <= p["poblacion"] <= maximo:
            resultados.append(p)

    mostrar_lista(resultados)


def filtrar_por_superficie(lista):
    print("\n--- FILTRAR POR RANGO DE SUPERFICIE ---")

    minimo = input("Superficie minima (km2): ").strip()
    maximo = input("Superficie maxima (km2): ").strip()

    if not minimo.isdigit() or not maximo.isdigit():
        print("Los valores tienen que ser numeros enteros mayores a cero.")
        return

    minimo = int(minimo)
    maximo = int(maximo)

    if minimo > maximo:
        print("El minimo no puede ser mayor que el maximo.")
        return

    resultados = []
    for p in lista:
        if minimo <= p["superficie"] <= maximo:
            resultados.append(p)

    mostrar_lista(resultados)


def menu_filtros(lista):
    print("\n--- FILTROS ---")
    print("1. Por continente")
    print("2. Por rango de poblacion")
    print("3. Por rango de superficie")
    print("0. Volver")

    opcion = input("Opcion: ").strip()

    if opcion == "1":
        filtrar_por_continente(lista)
    elif opcion == "2":
        filtrar_por_poblacion(lista)
    elif opcion == "3":
        filtrar_por_superficie(lista)
    elif opcion == "0":
        return
    else:
        print("Opcion invalida.")


def ordenar_paises(lista):
    print("\n--- ORDENAR PAISES ---")
    print("1. Por nombre")
    print("2. Por poblacion")
    print("3. Por superficie")
    print("0. Volver")

    opcion = input("Opcion: ").strip()

    if opcion == "0":
        return

    if opcion not in ["1", "2", "3"]:
        print("Opcion invalida.")
        return

    descendente = False
    if opcion == "2" or opcion == "3":
        orden = input("Orden: (A)scendente o (D)escendente? ").strip().upper()
        if orden == "D":
            descendente = True

    if opcion == "1":
        ordenados = sorted(lista, key=lambda p: p["nombre"].lower())
    elif opcion == "2":
        ordenados = sorted(lista, key=lambda p: p["poblacion"], reverse=descendente)
    elif opcion == "3":
        ordenados = sorted(lista, key=lambda p: p["superficie"], reverse=descendente)

    mostrar_lista(ordenados)


def mostrar_estadisticas(lista):
    print("\n--- ESTADISTICAS ---")

    if not lista:
        print("No hay paises cargados.")
        return

    mayor_pob = lista[0]
    menor_pob = lista[0]
    for p in lista:
        if p["poblacion"] > mayor_pob["poblacion"]:
            mayor_pob = p
        if p["poblacion"] < menor_pob["poblacion"]:
            menor_pob = p

    total_poblacion = 0
    total_superficie = 0
    for p in lista:
        total_poblacion = total_poblacion + p["poblacion"]
        total_superficie = total_superficie + p["superficie"]

    promedio_poblacion = total_poblacion // len(lista)
    promedio_superficie = total_superficie // len(lista)

    continentes = {}
    for p in lista:
        cont = p["continente"]
        if cont in continentes:
            continentes[cont] = continentes[cont] + 1
        else:
            continentes[cont] = 1

    print("\n  Pais con mayor poblacion :", mayor_pob["nombre"], "(", mayor_pob["poblacion"], ")")
    print("  Pais con menor poblacion :", menor_pob["nombre"], "(", menor_pob["poblacion"], ")")
    print("  Promedio de poblacion    :", promedio_poblacion)
    print("  Promedio de superficie   :", promedio_superficie, "km2")
    print("\n  Paises por continente:")
    for cont in continentes:
        print("   ", cont, ":", continentes[cont])


def mostrar_menu():
    print("\n========================================")
    print("      GESTION DE DATOS DE PAISES")
    print("========================================")
    print("1. Agregar un pais")
    print("2. Actualizar un pais")
    print("3. Buscar un pais por nombre")
    print("4. Filtrar paises")
    print("5. Ordenar paises")
    print("6. Ver estadisticas")
    print("0. Salir")
    print("========================================")


print("Cargando datos...")
paises = cargar_paises()
print("Se cargaron", len(paises), "paises.")

while True:
    mostrar_menu()
    opcion = input("Elegi una opcion: ").strip()

    if opcion == "1":
        agregar_pais(paises)
    elif opcion == "2":
        actualizar_pais(paises)
    elif opcion == "3":
        buscar_pais(paises)
    elif opcion == "4":
        menu_filtros(paises)
    elif opcion == "5":
        ordenar_paises(paises)
    elif opcion == "6":
        mostrar_estadisticas(paises)
    elif opcion == "0":
        print("Hasta luego!")
        break
    else:
        print("Opcion invalida. Ingresa un numero del menu.")