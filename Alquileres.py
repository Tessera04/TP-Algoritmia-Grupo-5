"""
-----------------------------------------------------------------------------------------------
Título: Trabajo Práctico Grupo 5 - Sistema de Gestión de Alquiler de Herramientas
Fecha: 22/10/2025
Autor: Vicente Courtinade, Marcos Gimenez, Matias Gonzalez, Lautaro Ruisoto, Santiago Salas.

Descripción:

Pendientes:
-----------------------------------------------------------------------------------------------
"""
#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
from datetime import datetime

#----------------------------------------------------------------------------------------------
# FUNCIONES Alquileres
#----------------------------------------------------------------------------------------------
def registrarAlquiler(alquileres, clientes, herramientas):
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

    print("---------------------------")
    print("Alquiler registrado con éxito.")
    print("---------------------------")

    return alquileres

def modificarAlquiler(alquileres):
    ...
    return alquileres

def eliminarAlquiler(alquileres):
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
    print("---------------------------")
    print("El Alquiler fue elimiado correctamente!")
    print("---------------------------")
    return alquileres   

def listarAlquileres(alquileres, clientes, herramientas):
    print("=== Lista de Alquileres ===")

    if len(alquileres) == 0:
        print("No hay alquileres registrados.")
        return
    
    print(f"{'ID':<5} {'Herramienta ':<50} {'Cliente':<50} {'Fecha de Inicio':<25} {'Fecha de Fin':<25} {'Dias de alquiler':<15} {'Total':<10} {'Activo':<10}")
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

        if datos["activo"]:
            estado = "Sí"
        else:
            estado = "No"

        print(f"{id_alquiler:<5} {nombre_herramienta:<50} {nombre_cliente:<50} {datos['fecha_inicio']:<25} {datos['fecha_fin']:<25} {datos['dias_alquiler']:<15} {datos['total']:<10} {estado}")
    return

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    ...


# Punto de entrada al programa
main()
