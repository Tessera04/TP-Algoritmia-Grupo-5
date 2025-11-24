"""
-----------------------------------------------------------------------------------------------
Título: Trabajo Práctico Grupo 5 - Sistema de Gestión de Alquiler de Herramientas
Fecha: 22/10/2025
Autor: Vicente Courtinade, Marcos Gimenez, Matias Gonzalez, Lautaro Ruisoto, Santiago Salas.

Descripción: Módulo de Alquileres del sistema de gestión de alquiler de herramientas. 
Proporciona funciones CRUD para registrar, modificar, eliminar y listar alquileres de herramientas.

Pendientes:
-----------------------------------------------------------------------------------------------
"""
#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
from datetime import datetime
from Archivos import *

#----------------------------------------------------------------------------------------------
# FUNCIONES Alquileres
#----------------------------------------------------------------------------------------------
def registrarAlquiler():
    """
    Registrar un nuevo alquiler de herramientas

    Archivos:
        alquileres.json (dict)
        clientes.json (dict)
        herramientas.json (dict)
    """
    try:
        clientes = cargarArchivoJSON("./JSON/clientes.json")
        herramientas = cargarArchivoJSON("./JSON/herramientas.json")
        alquileres = cargarArchivoJSON("./JSON/alquileres.json")

        print("=== Registrar nuevo alquiler de herramientas ===")

        if len(alquileres) == 0:
            nuevo_id = "1"
        else:
            nuevo_id = str(int(max(alquileres.keys())) + 1)

        print("---------------------------")
        print("Clientes disponibles:")
        print("---------------------------")

        for id_cliente, datos in clientes.items():
            if datos["activo"]:
                print(f"{id_cliente} - {datos['nombre']}")
        
        print("---------------------------")
        idCliente = input("Ingrese el ID del cliente seleccionado: ").strip()
        print("---------------------------")

        if id_cliente not in clientes:
            print("---------------------------")
            print("Cliente no encontrado.")
            print("---------------------------")
            return alquileres
        
        print("---------------------------")
        print("Herramientas disponibles:")
        print("---------------------------")
        for id_herramienta, datos in herramientas.items():
            if datos["activa"]:
                print(f"{id_herramienta} - {datos['nombre']}")
        
        #Solicitar datos del cliente
        print("---------------------------")
        idHerramienta = input("Ingrese el ID de la herramienta seleccionada: ").strip()
        print("---------------------------")

        if id_herramienta not in herramientas:
            print("---------------------------")
            print("Herramienta no encontrada.")
            print("---------------------------")
            return alquileres
        
        fecha_inicio = input("Ingrese la fecha de inicio (AAAA-MM-DD): ").strip()
        fecha_fin = input("Ingrese la fecha de fin (AAAA-MM-DD): ").strip()

        f1 = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        f2 = datetime.strptime(fecha_fin, "%Y-%m-%d")
        dias_alquiler = (f2 - f1).days

        if dias_alquiler <= 0:
            print("La fecha de fin debe ser posterior a la de inicio.")
            return alquileres
        
        precio_dia = herramientas[id_herramienta]["costo_diario"]
        total = precio_dia * dias_alquiler

        alquileres[nuevo_id] = {
            "id_herramienta": idHerramienta,
            "id_cliente": idCliente,
            "fecha_inicio": fecha_inicio,
            "fecha_fin": fecha_fin,
            "dias_alquiler": dias_alquiler,
            "total": total,
            "activo": True
        }

        guardarArchivoJSON("./JSON/alquileres.json", alquileres)

        print("---------------------------")
        print("Alquiler registrado con éxito.")
        print("---------------------------")
    except(TypeError) as detalle:
        print("No se encontraron registros: ", detalle)
    except Exception as e:
        print("ERROR!: Error inesperado al guardar el archivo: ", e)

def modificarAlquiler():
    """
    Modificar los datos de un alquiler existente

    Archivos:
        alquileres.json (dict)
        clientes.json (dict)
        herramientas.json (dict)
    """
    try:
        clientes = cargarArchivoJSON("./JSON/clientes.json")
        herramientas = cargarArchivoJSON("./JSON/herramientas.json")
        alquileres = cargarArchivoJSON("./JSON/alquileres.json")

        print("=== Modificar alquiler ===")
    
        if len(alquileres) == 0:
            print("No hay alquileres registrados.")
            return alquileres
    
        print(f"{'ID':<5} {'Cliente':<20} {'Herramienta':<25} {'Activo':<10}")
        print("-" * 60)
    
        for id_alquiler, datos in alquileres.items():
            nombre_cliente = clientes.get(datos["id_cliente"], {}).get("nombre", "Desconocido")
            nombre_herramienta = herramientas.get(datos["id_herramienta"], {}).get("nombre", "Desconocida")
            estado = "Sí" if datos["activo"] else "No"
            print(f"{id_alquiler:<5} {nombre_cliente:<20} {nombre_herramienta:<25} {estado:<10}")
    
        print("-" * 60)
        id_alquiler = input("Ingrese el ID del alquiler que desea modificar: ").strip()
    
        if id_alquiler not in alquileres:
            print("ID no encontrado.")
            return alquileres
    
        alquiler = alquileres[id_alquiler]
    
        print("---------------------------")
        print("Datos actuales del alquiler:")
        print(f"Cliente: {alquiler['id_cliente']}")
        print(f"Herramienta: {alquiler['id_herramienta']}")
        print(f"Fecha inicio: {alquiler['fecha_inicio']}")
        print(f"Fecha fin: {alquiler['fecha_fin']}")
        print(f"Activo: {'Sí' if alquiler['activo'] else 'No'}")
        print("---------------------------")
    
        # --- Modificar cliente ---
        opcion = input("¿Desea cambiar el cliente? (s/n): ").strip().lower()
        while opcion not in ("s", "n"):
            opcion = input("Opción inválida. Ingrese 's' o 'n': ").strip().lower()
        if opcion == "s":
            print("Clientes disponibles:")
            for id_cliente, datos in clientes.items():
                if datos["activo"]:
                    print(f"{id_cliente} - {datos['nombre']}")
            nuevo_cliente = input("Ingrese el nuevo ID de cliente: ").strip()
            if nuevo_cliente in clientes and clientes[nuevo_cliente]["activo"]:
                alquiler["id_cliente"] = nuevo_cliente
            else:
                print("Cliente no válido, se mantiene el actual.")
    
        # --- Modificar herramienta ---
        opcion = input("¿Desea cambiar la herramienta? (s/n): ").strip().lower()
        while opcion not in ("s", "n"):
            opcion = input("Opción inválida. Ingrese 's' o 'n': ").strip().lower()
        if opcion == "s":
            print("Herramientas disponibles:")
            for id_herramienta, datos in herramientas.items():
                if datos["activa"]:
                    print(f"{id_herramienta} - {datos['nombre']}")
            nueva_herramienta = input("Ingrese el nuevo ID de herramienta: ").strip()
            if nueva_herramienta in herramientas and herramientas[nueva_herramienta]["activa"]:
                alquiler["id_herramienta"] = nueva_herramienta
            else:
                print("Herramienta no válida, se mantiene la actual.")
    
        # --- Modificar fechas ---
        opcion = input("¿Desea cambiar las fechas? (s/n): ").strip().lower()
        while opcion not in ("s", "n"):
            opcion = input("Opción inválida. Ingrese 's' o 'n': ").strip().lower()
        if opcion == "s":
            fecha_inicio = input("Ingrese nueva fecha de inicio (AAAA-MM-DD): ").strip()
            fecha_fin = input("Ingrese nueva fecha de fin (AAAA-MM-DD): ").strip()
    
            f1 = datetime.strptime(fecha_inicio, "%Y-%m-%d")
            f2 = datetime.strptime(fecha_fin, "%Y-%m-%d")
    
            dias_alquiler = (f2 - f1).days
            if dias_alquiler <= 0:
                print("La fecha de fin debe ser posterior a la de inicio. No se modificaron las fechas.")
            else:
                alquiler["fecha_inicio"] = fecha_inicio
                alquiler["fecha_fin"] = fecha_fin
                alquiler["dias_alquiler"] = dias_alquiler
                precio_dia = herramientas[alquiler["id_herramienta"]]["costo_diario"]
                alquiler["total"] = precio_dia * dias_alquiler
                print("Fechas y total actualizados correctamente.")
    
        # --- Cambiar estado activo ---
        opcion = input("¿Desea cambiar el estado del alquiler (activo/inactivo)? (s/n): ").strip().lower()
        while opcion not in ("s", "n"):
            opcion = input("Opción inválida. Ingrese 's' o 'n': ").strip().lower()
        if opcion == "s":
            nuevo_estado = input("Ingrese 's' para activo o 'n' para inactivo: ").strip().lower()
            while nuevo_estado not in ("s", "n"):
                nuevo_estado = input("Opción inválida. Ingrese 's' o 'n': ").strip().lower()
            alquiler["activo"] = nuevo_estado == "s"
        
        guardarArchivoJSON("./JSON/alquileres.json", alquileres)
    
        print("---------------------------")
        print("Alquiler modificado correctamente.")
        print("---------------------------")

    except(TypeError) as detalle:
        print("No se encontraron registros: ", detalle)
    except Exception as e:
        print("ERROR!: Error inesperado al guardar el archivo: ", e)

def eliminarAlquiler():
    """
    Dar de baja logicamente un alquiler

    Archivos:
        alquileres.json (dict)
    """
    try:  
        alquileres = cargarArchivoJSON("./JSON/alquileres.json")

        print("=== Eliminar alquiler ===")

        if len(alquileres) == 0:
            print("No hay alquileres registrados.")
            return alquileres
        
        for id_alquileres, datos in alquileres.items():
            print(f"{id_alquileres} - Cliente {datos['id_cliente']} | Herramienta {datos['id_herramienta']} | Activo: {'Sí' if datos['activo'] else 'No'}")

        print("---------------------------")
        id_alquileres = input("Ingrese el ID del alquiler seleccionado: ").strip()
        print("---------------------------")   

        if id_alquileres not in alquileres:
            print("ID no encontrado.")
            return alquileres
        
        alquileres[id_alquileres]["activo"] = False

        guardarArchivoJSON("./JSON/alquileres.json", alquileres)

        print("---------------------------")
        print("El Alquiler fue elimiado correctamente!")
        print("---------------------------")
    except(TypeError) as detalle:
        print("No se encontraron registros: ", detalle)
    except Exception as e:
        print("ERROR!: Error inesperado al guardar el archivo: ", e)

def listarAlquileres():
    """
    Mostrar en pantalla la lista completa de alquileres registrados

    Archivos:
        alquileres.json (dict)
        clientes.json (dict)
        herramientas.json (dict)

    Devuelve:
        None
    """
    try:
        clientes = cargarArchivoJSON("./JSON/clientes.json")
        herramientas = cargarArchivoJSON("./JSON/herramientas.json")
        alquileres = cargarArchivoJSON("./JSON/alquileres.json")

        print("=== Lista de Alquileres ===")

        if len(alquileres) == 0:
            print("No hay alquileres registrados.")
            return
        
        print(f"{'ID':<25} {'Herramienta ':<50} {'Cliente':<50} {'Fecha de Inicio':<25} {'Fecha de Fin':<25} {'Dias de alquiler':<15} {'Total':<10}")
        print('*' * 200)

        for id_alquiler, datos in alquileres.items():
            id_cliente = datos["id_cliente"]
            id_herramienta = datos["id_herramienta"]

            if id_cliente in clientes:
                nombre_cliente = clientes[id_cliente]["nombre"]
            else:
                nombre_cliente = "Nombre desconocido!"
            
            if id_herramienta in herramientas:
                nombre_herramienta = herramientas[id_herramienta]["nombre"]
            else:
                nombre_herramienta = "Herramienta desconocida!"

            if datos["activo"] == True:
                print(f"{id_alquiler:<25} {nombre_herramienta:<50} {nombre_cliente:<50} {datos['fecha_inicio']:<25} {datos['fecha_fin']:<25} {datos['dias_alquiler']:<15} {datos['total']:<10}")
    except(TypeError) as detalle:
        print("No se encontraron registros: ", detalle)
    except Exception as e:
        print("ERROR!: Error inesperado al guardar el archivo: ", e)

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    ...


# Punto de entrada al programa
main()
