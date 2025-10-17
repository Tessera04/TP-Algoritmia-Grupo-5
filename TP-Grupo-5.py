"""
-----------------------------------------------------------------------------------------------
Título: Trabajo Práctico Grupo 5 - Sistema de Gestión de Alquiler de Herramientas
Fecha: 22/10/2025
Autor: Vicente Courtinade, Marcos Gimenez, Matias Gonzalez, Lautaro Ruisoto, Santiago Salas.

Descripción: Sistema de gestión para una empresa de alquiler de herramientas que permite registrar,
modificar, eliminar y listar clientes, herramientas y alquileres. Además, genera informes sobre ventas
y herramientas inactivas.

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
...


#----------------------------------------------------------------------------------------------
# FUNCIONES Clientes
#----------------------------------------------------------------------------------------------
def registrarCliente(clientes):
    ...
    return clientes

def modificarCliente(clientes):
    ...
    return clientes

def eliminarCliente(clientes):
    ...
    return clientes

def listarClientes(clientes):
    ...
    return

#----------------------------------------------------------------------------------------------
# FUNCIONES Herramientas
#----------------------------------------------------------------------------------------------
def registrarHerramienta(herramientas):
    ...
    return herramientas

def modificarHerramienta(herramientas):
    ...
    return herramientas

def eliminarHerramienta(herramientas):
    ...
    return herramientas

def listarHerramientas(herramientas):
    ...
    return

#----------------------------------------------------------------------------------------------
# FUNCIONES Alquileres
#----------------------------------------------------------------------------------------------
def registrarAlquiler(alquileres):
    ...
    return alquileres

def modificarAlquiler(alquileres):
    ...
    return alquileres

def eliminarAlquiler(alquileres):
    ...
    return alquileres   

def listarAlquileres(alquileres):
    ...
    return

#----------------------------------------------------------------------------------------------
# FUNCIONES Informes
#----------------------------------------------------------------------------------------------

def informeVentasYRecaudacionMensual(alquileres):
    ...
    return

def informeVentasPorProductoCantidades(alquileres):
    ...
    return

def informeVentasPorProductoPrecios(alquileres):
    ...
    return

def informeHerramientasInactivas(herramientas, alquileres):
    ...
    return

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    #-------------------------------------------------
    # Inicialización de variables
    #----------------------------------------------------------------------------------------------
    clientes = {...}


    #-------------------------------------------------
    # Bloque de menú
    #----------------------------------------------------------------------------------------------
    while True:
        while True:
            opciones = 5
            print()
            print("---------------------------")
            print("MENÚ PRINCIPAL")
            print("---------------------------")
            print("[1] Gestión de Herramientas")
            print("[2] Gestión de Alquileres")
            print("[3] Gestión de Clientes")
            print("[4] Informes")
            print("---------------------------")
            print("[0] Salir del programa")
            print("---------------------------")
            print()
            
            opcionSubmenu = ""
            opcionMenuPrincipal = input("Seleccione una opción: ")
            if opcionMenuPrincipal in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcionMenuPrincipal == "0": # Opción salir del programa
            exit() # También puede ser sys.exit() para lo cual hay que importar el módulo sys

        elif opcionMenuPrincipal == "1":   # Opción 1 del menú principal
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE CLIENTES")
                    print("---------------------------")
                    print("[1] Registrar clientes")
                    print("[2] Modificar clientes")
                    print("[3] Eliminar clientes")
                    print("[4] Listar clientes")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    clientes = registrarCliente(clientes)
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    clientes = modificarCliente(clientes)
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    clientes = eliminarCliente(clientes)

                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    clientes = listarClientes(clientes)

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")


        elif opcionMenuPrincipal == "2":   # Opción 2 del menú principal
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE ALQUILERES")
                    print("---------------------------")
                    print("[1] Registrar alquileres")
                    print("[2] Modificar alquileres")
                    print("[3] Eliminar alquileres")
                    print("[4] Listar alquileres")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    alquileres = registrarAlquiler(alquileres)
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    alquileres = modificarAlquiler(alquileres)

                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    alquileres = eliminarAlquiler(alquileres)

                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    alquileres = listarAlquileres(alquileres)

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")

        
        elif opcionMenuPrincipal == "3":   # Opción 3 del menú principal
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE HERRAMIENTAS")
                    print("---------------------------")
                    print("[1] Registrar herramientas")
                    print("[2] Modificar herramientas")
                    print("[3] Eliminar herramientas")
                    print("[4] Listar herramientas")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    herramientas = registrarHerramienta(herramientas)

                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    herramientas = modificarHerramienta(herramientas)

                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    herramientas = eliminarHerramienta(herramientas)

                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    herramientas = listarHerramientas(herramientas)

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")

        
        elif opcionMenuPrincipal == "4":   # Opción 4 del menú principal
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE INFORMES")
                    print("---------------------------")
                    print("[1] Ventas y total recaudado del mes")
                    print("[2] Resumen anual de Ventas por producto (cantidades)")
                    print("[3] Resumen anual de Ventas por producto (precios)")
                    print("[4] Herramientas inactivas o con bajos movimientos")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    informes = informeVentasYRecaudacionMensual(alquileres)
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    informes = informeVentasPorProductoCantidades(alquileres)

                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    informes = informeVentasPorProductoPrecios(alquileres)

                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    informes = informeHerramientasInactivas(herramientas, alquileres)

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")

        if opcionSubmenu != "0": # Pausa entre opciones. No la realiza si se vuelve de un submenú
            input("\nPresione ENTER para volver al menú.")
            print("\n\n")


# Punto de entrada al programa
main()