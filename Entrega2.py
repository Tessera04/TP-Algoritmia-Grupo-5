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

    herramientas = {
        "1":{"activa"       :True,
              "nombre"      :"Taladro Bosch",
              "costo_diario":4500.0,
              "stock"       :5
            },
            
        "2": {"activa"      :True,
              "nombre"      :"Amoladora angular DeWalt",
              "costo_diario":4200.0,
              "stock"       :3
            },

        "3": {"activa": True,
            "nombre": "Sierra circular Makita",
            "costo_diario": 5200.0,
            "stock": 4},

        "4": {"activa": True,
            "nombre": "Lijadora Black+Decker",
            "costo_diario": 3100.0,
            "stock": 6},

        "5": {"activa": True,
            "nombre": "Cortadora de césped eléctrica Gamma",
            "costo_diario": 5700.0,
            "stock": 2},

        "6": {"activa": True,
            "nombre": "Martillo demoledor Stanley",
            "costo_diario": 6300.0,
            "stock": 3},

        "7": {"activa": True,
            "nombre": "Soldadora inverter Lusqtoff",
            "costo_diario": 6900.0,
            "stock": 2},

        "8": {"activa": True,
            "nombre": "Compresor de aire",
            "costo_diario": 7500.0,
            "stock": 1},

        "9": {"activa": True,
            "nombre": "Pistola de calor Skil",
            "costo_diario": 2800.0,
            "stock": 5},

        "10": {"activa": True,
            "nombre": "Atornillador inalámbrico Bosch",
            "costo_diario": 3600.0,
            "stock": 4},
    }

    alquileres = {
        "1": {
            "id_herramienta": "3",  # Sierra circular Makita 5007N
            "id_cliente": "38992233",  # TOMÁS EZEQUIEL GARCÍA
            "fecha_inicio": "2025-10-02",
            "fecha_fin": "2025-10-05",
            "dias_alquiler": 3,
            "total": 5200.0 * 3,  # 15600.0
            "activo": True
        },
        "2": {
            "id_herramienta": "6",  # Martillo demoledor Stanley STHM5KH
            "id_cliente": "30566123",  # ANDREA BEATRIZ LÓPEZ
            "fecha_inicio": "2025-10-04",
            "fecha_fin": "2025-10-08",
            "dias_alquiler": 4,
            "total": 6300.0 * 4,  # 25200.0
            "activo": True
        },
        "3": {
            "id_herramienta": "1",  # Taladro percutor Bosch GSB 13 RE
            "id_cliente": "41765012",  # SOFÍA ALEJANDRA MONTIEL
            "fecha_inicio": "2025-10-05",
            "fecha_fin": "2025-10-09",
            "dias_alquiler": 4,
            "total": 4500.0 * 4,  # 18000.0
            "activo": True
        },
        "4": {
            "id_herramienta": "10",  # Atornillador inalámbrico Bosch IXO V
            "id_cliente": "29644109",  # CARLA ANDREA VILLALBA
            "fecha_inicio": "2025-10-07",
            "fecha_fin": "2025-10-10",
            "dias_alquiler": 3,
            "total": 3600.0 * 3,  # 10800.0
            "activo": True
        },
        "5": {
            "id_herramienta": "4",  # Lijadora orbital Black+Decker KA300
            "id_cliente": "27784566",  # MARÍA LUJÁN PAREDES
            "fecha_inicio": "2025-10-09",
            "fecha_fin": "2025-10-11",
            "dias_alquiler": 2,
            "total": 3100.0 * 2,  # 6200.0
            "activo": True
        },
        "6": {
            "id_herramienta": "7",  # Soldadora inverter Lusqtoff Iron 250
            "id_cliente": "27811984",  # MARTÍN ESTEBAN FERRARI
            "fecha_inicio": "2025-10-10",
            "fecha_fin": "2025-10-15",
            "dias_alquiler": 5,
            "total": 6900.0 * 5,  # 34500.0
            "activo": True
        },
        "7": {
            "id_herramienta": "9",  # Pistola de calor Skil 8003 AA
            "id_cliente": "42331005",  # ROCÍO BELÉN SALGADO
            "fecha_inicio": "2025-10-12",
            "fecha_fin": "2025-10-14",
            "dias_alquiler": 2,
            "total": 2800.0 * 2,  # 5600.0
            "activo": True
        },
        "8": {
            "id_herramienta": "2",  # Amoladora angular DeWalt DWE4010
            "id_cliente": "41022987",  # ANA CELESTE CÁCERES
            "fecha_inicio": "2025-10-13",
            "fecha_fin": "2025-10-17",
            "dias_alquiler": 4,
            "total": 4200.0 * 4,  # 16800.0
            "activo": True
        },
        "9": {
            "id_herramienta": "8",  # Compresor de aire 50L Einhell TE-AC 270/50/10
            "id_cliente": "38900011",  # LUCÍA VANESA TORRES
            "fecha_inicio": "2025-10-16",
            "fecha_fin": "2025-10-20",
            "dias_alquiler": 4,
            "total": 7500.0 * 4,  # 30000.0
            "activo": True
        },
        "10": {
            "id_herramienta": "5",  # Cortadora de césped Gamma G2832AR
            "id_cliente": "34591277",  # JORGE LUIS RIVERO
            "fecha_inicio": "2025-10-18",
            "fecha_fin": "2025-10-21",
            "dias_alquiler": 3,
            "total": 5700.0 * 3,  # 17100.0
            "activo": True
        }
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
                    alquileres = registrarAlquiler(alquileres, clientes, herramientas)
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú alquileres
                    alquileres = modificarAlquiler(alquileres)

                elif opcionSubmenu == "3":   # Opción 3 del submenú alquileres
                    alquileres = eliminarAlquiler(alquileres)

                elif opcionSubmenu == "4":   # Opción 4 del submenú alquileres
                    alquileres = listarAlquileres(alquileres, clientes, herramientas)

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
                    informes = informeVentasYRecaudacionMensual(alquileres,clientes,herramientas)

                elif opcionSubmenu == "2":   # Opción 2 del submenú informes
                    informes = informeVentasPorProductoCantidades(alquileres, herramientas)

                elif opcionSubmenu == "3":   # Opción 3 del submenú  informes
                    informes = informeVentasPorProductoPrecios(alquileres, herramientas)

                elif opcionSubmenu == "4":   # Opción 4 del submenú informes
                    informes = informeHerramientasInactivas(herramientas, alquileres)

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")

        if opcionSubmenu != "0": # Pausa entre opciones. No la realiza si se vuelve de un submenú
            input("\nPresione ENTER para volver al menú.")
            print("\n\n")


# Punto de entrada al programa
main()