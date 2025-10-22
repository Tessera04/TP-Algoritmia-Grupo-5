"""
-----------------------------------------------------------------------------------------------
Título: Trabajo Práctico Grupo 5 - Sistema de Gestión de Alquiler de Herramientas
Fecha: 22/10/2025
Autor: Vicente Courtinade, Marcos Gimenez, Matias Gonzalez, Lautaro Ruisoto, Santiago Salas.

Descripción: Sistema de gestión CRUD para una empresa de alquiler de herramientas que permite registrar,
modificar, eliminar y listar clientes, herramientas y alquileres. Además, genera informes sobre ventas
y herramientas inactivas.

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
from Clientes import *
from Herramientas import *
from Alquileres import *
from Informes import *

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    #-------------------------------------------------
    # Inicialización de variables
    #----------------------------------------------------------------------------------------------
    clientes = {
        "38111222":{"activo"   :False,
                    "nombre"   :"JUAN JOSÉ GALVÁN",
                    "domicilio":"ESTRADA 2048",
                    "email"    :"juangalvan@gmail.com",
                    "telefonos":{"telefono1":"11-4521-8956",
                                 "telefono2":"15-1526-4859",
                                 "telefono3":"11-7812-5689",
                                },
                   },
        "25888444":{"activo"   :True,
                    "nombre"   :"CLARA JULIETA FASIOLI",
                    "domicilio":"INDEPENDENCIA 322",
                    "email"    :"clarajf332@outlook.com",
                    "telefonos":{"telefono1":"11 5623 8945",
                                },
                   },
        "33299118":{"activo"   :True,
                    "nombre"   :"MARCOS EMILIANO VERA",
                    "domicilio":"LAPRIDA 1850",
                    "email"    :"marcosvera@yahoo.com",
                    "telefonos":{"telefono1":"11-4738-1122",
                                 "telefono2":"15-6132-0029",
                                },
                   },
        "41765012":{"activo"   :True,
                    "nombre"   :"SOFÍA ALEJANDRA MONTIEL",
                    "domicilio":"ALSINA 542",
                    "email"    :"sofia.montiel@hotmail.com",
                    "telefonos":{"telefono1":"11-3874-2255",
                                },
                   },
        "29177654":{"activo"   :True,
                    "nombre"   :"DIEGO MANUEL PERALTA",
                    "domicilio":"SALTA 980",
                    "email"    :"dperalta@gmail.com",
                    "telefonos":{"telefono1":"11-4962-7412",
                                 "telefono2":"15-5339-8821",
                                },
                   },
        "30987651":{"activo"   :True,
                    "nombre"   :"NATALIA SOLEDAD PÉREZ",
                    "domicilio":"PUEYRREDÓN 2110",
                    "email"    :"nataperez@live.com",
                    "telefonos":{"telefono1":"11-6859-3011",
                                },
                   },
        "42711895":{"activo"   :True,
                    "nombre"   :"GABRIEL IGNACIO ROMERO",
                    "domicilio":"PAZ 705",
                    "email"    :"gromero77@gmail.com",
                    "telefonos":{"telefono1":"11-5210-7744",
                                 "telefono2":"11-7874-9630",
                                },
                   },
        "36890221":{"activo"   :True,
                    "nombre"   :"VALERIA DENISE GIMÉNEZ",
                    "domicilio":"SARMIENTO 310",
                    "email"    :"valegimenez@gmail.com",
                    "telefonos":{"telefono1":"11-6668-2233",
                                 "telefono2":"15-5021-8890",
                                 "telefono3":"11-4390-5578",
                                },
                   },
        "41233789":{"activo"   :True,
                    "nombre"   :"LEANDRO FABRICIO MORALES",
                    "domicilio":"BELGRANO 1664",
                    "email"    :"lfmorales@outlook.com",
                    "telefonos":{"telefono1":"11-3777-2134",
                                },
                   },
        "30566123":{"activo"   :True,
                    "nombre"   :"ANDREA BEATRIZ LÓPEZ",
                    "domicilio":"SAN MARTÍN 882",
                    "email"    :"andrealopez@gmail.com",
                    "telefonos":{"telefono1":"11-5398-7452",
                                 "telefono2":"11-7981-5526",
                                },
                   },
        "38992233":{"activo"   :True,
                    "nombre"   :"TOMÁS EZEQUIEL GARCÍA",
                    "domicilio":"CATAMARCA 215",
                    "email"    :"tomasgarcia@gmail.com",
                    "telefonos":{"telefono1":"11-4441-6689",
                                },
                   },
        "27784566":{"activo"   :True,
                    "nombre"   :"MARÍA LUJÁN PAREDES",
                    "domicilio":"SAN JUAN 950",
                    "email"    :"mlpar83@yahoo.com",
                    "telefonos":{"telefono1":"11-3219-7710",
                                 "telefono2":"11-7985-6631",
                                },
                   },
        "41388290":{"activo"   :True,
                    "nombre"   :"NICOLÁS ADRIÁN GÓMEZ",
                    "domicilio":"YRIGOYEN 1299",
                    "email"    :"nicolasgomez@live.com",
                    "telefonos":{"telefono1":"11-4020-7411",
                                },
                   },
        "29644109":{"activo"   :True,
                    "nombre"   :"CARLA ANDREA VILLALBA",
                    "domicilio":"TUCUMÁN 777",
                    "email"    :"cvillalba@gmail.com",
                    "telefonos":{"telefono1":"11-6932-2250",
                                 "telefono2":"15-5001-7859",
                                },
                   },
        "34591277":{"activo"   :True,
                    "nombre"   :"JORGE LUIS RIVERO",
                    "domicilio":"MAIPÚ 1800",
                    "email"    :"jorgerivero@outlook.com",
                    "telefonos":{"telefono1":"11-3254-9977",
                                },
                   },
        "38900011":{"activo"   :True,
                    "nombre"   :"LUCÍA VANESA TORRES",
                    "domicilio":"MITRE 620",
                    "email"    :"lucia.torres@gmail.com",
                    "telefonos":{"telefono1":"11-4422-1358",
                                 "telefono2":"11-7935-6214",
                                 "telefono3":"11-6150-8877",
                                },
                   },
        "27811984":{"activo"   :True,
                    "nombre"   :"MARTÍN ESTEBAN FERRARI",
                    "domicilio":"MORENO 431",
                    "email"    :"mferrari@hotmail.com",
                    "telefonos":{"telefono1":"11-5668-2005",
                                },
                   },
        "42331005":{"activo"   :True,
                    "nombre"   :"ROCÍO BELÉN SALGADO",
                    "domicilio":"CORDOBA 1561",
                    "email"    :"rocio.salgado@gmail.com",
                    "telefonos":{"telefono1":"11-6311-2289",
                                 "telefono2":"11-7144-9621",
                                },
                   },
        "30771299":{"activo"   :True,
                    "nombre"   :"IGNACIO FEDERICO BIANCHI",
                    "domicilio":"SANTA FE 330",
                    "email"    :"ignabi@live.com",
                    "telefonos":{"telefono1":"11-4566-7745",
                                 "telefono2":"15-7793-1112",
                                },
                   },
        "41022987":{"activo"   :True,
                    "nombre"   :"ANA CELESTE CÁCERES",
                    "domicilio":"BELGRANO 999",
                    "email"    :"anacaceres@gmail.com",
                    "telefonos":{"telefono1":"11-5899-3344",
                                },
                   },
    }


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
            print("[1] Gestión de Clientes")
            print("[2] Gestión de Alquileres")
            print("[3] Gestión de Herramientas")
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

                if opcionSubmenu == "0": # Opción salir del submenú clientes
                    break # No sale del programa, sino que vuelve al menú anterior

                elif opcionSubmenu == "1":   # Opción 1 del submenú clientes
                    clientes = registrarCliente(clientes)

                elif opcionSubmenu == "2":   # Opción 2 del submenú clientes
                    clientes = modificarCliente(clientes)
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú     clientes
                    clientes = eliminarCliente(clientes)

                elif opcionSubmenu == "4":   # Opción 4 del submenú clientes
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

                if opcionSubmenu == "0": # Opción salir del submenú alquileres
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú alquileres
                    alquileres = registrarAlquiler(alquileres)
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú alquileres
                    alquileres = modificarAlquiler(alquileres)

                elif opcionSubmenu == "3":   # Opción 3 del submenú alquileres
                    alquileres = eliminarAlquiler(alquileres)

                elif opcionSubmenu == "4":   # Opción 4 del submenú alquileres
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

                if opcionSubmenu == "0": # Opción salir del submenú herramientas
                    break # No sale del programa, sino que vuelve al menú anterior

                elif opcionSubmenu == "1":   # Opción 1 del submenú herramientas
                    herramientas = registrarHerramienta(herramientas)

                elif opcionSubmenu == "2":   # Opción 2 del submenú herramientas
                    herramientas = modificarHerramienta(herramientas)

                elif opcionSubmenu == "3":   # Opción 3 del submenú herramientas
                    herramientas = eliminarHerramienta(herramientas)

                elif opcionSubmenu == "4":   # Opción 4 del submenú herramientas
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

                if opcionSubmenu == "0": # Opción salir del submenú informes
                    break # No sale del programa, sino que vuelve al menú anterior

                elif opcionSubmenu == "1":   # Opción 1 del submenú informes
                    informes = informeVentasYRecaudacionMensual(alquileres)

                elif opcionSubmenu == "2":   # Opción 2 del submenú informes
                    informes = informeVentasPorProductoCantidades(alquileres)

                elif opcionSubmenu == "3":   # Opción 3 del submenú  informes
                    informes = informeVentasPorProductoPrecios(alquileres)

                elif opcionSubmenu == "4":   # Opción 4 del submenú informes
                    informes = informeHerramientasInactivas(herramientas, alquileres)

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")

        if opcionSubmenu != "0": # Pausa entre opciones. No la realiza si se vuelve de un submenú
            input("\nPresione ENTER para volver al menú.")
            print("\n\n")


# Punto de entrada al programa
main()