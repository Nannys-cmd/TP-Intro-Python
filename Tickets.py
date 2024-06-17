import sys
import os
import random

# Nombre del archivo donde se guardarán los tickets
archivo_tickets = "tickets.txt"

# Diccionario para almacenar los tickets
tickets = {}

def cargar_tickets():
    if os.path.isfile(archivo_tickets):
        with open(archivo_tickets, "r") as f:
            for linea in f:
                linea = linea.strip()
                if linea:
                    numero_ticket, nombre, sector, asunto, problema = linea.split('|')
                    tickets[int(numero_ticket)] = {
                        "nombre": nombre,
                        "sector": sector,
                        "asunto": asunto,
                        "problema": problema
                    }

def guardar_tickets():
    with open(archivo_tickets, "w") as f:
        for numero_ticket, datos in tickets.items():
            linea = f"{numero_ticket}|{datos['nombre']}|{datos['sector']}|{datos['asunto']}|{datos['problema']}\n"
            f.write(linea)

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def menu_principal():
    cargar_tickets()
    while True:
        limpiar_pantalla()
        print("Menú Principal:")
        print("1. Alta ticket")
        print("2. Leer ticket")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            alta_ticket()
        elif opcion == "2":
            leer_ticket()
        elif opcion == "3":
            if salir():
                print("Gracias por usar el sistema de tickets.")
                sys.exit()
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

def alta_ticket():
    nombre = input("Nombre: ")
    sector = input("Sector: ")
    asunto = input("Asunto: ")
    problema = input("Problema: ")

    numero_ticket = random.randint(1000, 9999)
    tickets[numero_ticket] = {
        "nombre": nombre,
        "sector": sector,
        "asunto": asunto,
        "problema": problema
    }
    guardar_tickets()

    print("\nTicket creado con éxito.")
    print(f"Número de Ticket: {numero_ticket}")
    print(f"Nombre: {nombre}")
    print(f"Sector: {sector}")
    print(f"Asunto: {asunto}")
    print(f"Problema: {problema}")
    print("Por favor, recuerde el número de ticket para futuras consultas.\n")
    
    while True:
        otra_vez = input("¿Desea crear otro ticket? (s/n): ")
        if otra_vez.lower() == 's':
            alta_ticket()
            break
        elif otra_vez.lower() == 'n':
            break
        else:
            print("Respuesta no válida. Por favor, responda 's' o 'n'.")

def leer_ticket():
    numero_ticket = int(input("Ingrese el número de ticket: "))
    ticket = tickets.get(numero_ticket)

    if ticket:
        print(f"\nTicket Número: {numero_ticket}")
        print(f"Nombre: {ticket['nombre']}")
        print(f"Sector: {ticket['sector']}")
        print(f"Asunto: {ticket['asunto']}")
        print(f"Problema: {ticket['problema']}\n")
    else:
        print("\nTicket no encontrado.\n")

    while True:
        otra_vez = input("¿Desea leer otro ticket? (s/n): ")
        if otra_vez.lower() == 's':
            leer_ticket()
            break
        elif otra_vez.lower() == 'n':
            break
        else:
            print("Respuesta no válida. Por favor, responda 's' o 'n'.")

def salir():
    confirmacion = input("¿Está seguro que desea salir? (s/n): ")
    return confirmacion.lower() == 's'

# Ejecutar el menú principal
menu_principal()
