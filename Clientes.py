"""
-----------------------------------------------------------------------------------------------
Título: Trabajo Práctico Grupo 5 - Sistema de Gestión de Alquiler de Herramientas
Fecha: 22/10/2025
Autor: Vicente Courtinade, Marcos Gimenez, Matias Gonzalez, Lautaro Ruisoto, Santiago Salas.

Descripción: Módulo de Clientes del sistema de gestión de alquiler de herramientas. 
Proporciona funciones CRUD para registrar, modificar, eliminar y listar clientes.

Pendientes:
-----------------------------------------------------------------------------------------------
"""
#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
from Archivos import *

#----------------------------------------------------------------------------------------------
# FUNCIONES Clientes
#----------------------------------------------------------------------------------------------
def registrarCliente():
    """
    Registra un nuevo cliente solicitando datos personales y permitiendole ingresar 1 o mas telefonos.

    Parametros:


    Returns:
    dict: El diccionario 'clientes' actualizado con la nueva entrada.
    """
    try:
        clientes = cargarArchivoJSON("./JSON/clientes.json")

        print("=== Registrar nuevo cliente ===")
        # Lógica para registrar un nuevo id de cliente
        if len(clientes) == 0:
            nuevo_id = "1"
        else:
            nuevo_id = str(int(max(clientes.keys())) + 1)

        #Solicitar datos del cliente
        nombre = str(input("Ingrese el nombre del cliente: ")).strip()
        domicilio = str(input("Ingrese el domicilio del cliente: ")).strip()
        email = str(input("Ingrese un email valido: ")).strip()

        # Cargar uno o más teléfonos
        telefonos = {}
        contador = 1
        while True:
            telefono = input(f"Ingrese el teléfono {contador}: ").strip()
            if telefono == "":
                print("El teléfono no puede estar vacío.")
                continue
            telefonos[f"telefono{contador}"] = telefono

            otroTelefono = input("¿Desea agregar otro teléfono? (s/n): ").strip()
            if otroTelefono != "s":
                break
            contador += 1

        #Agregar el nuevo cliente al diccionario
        clientes[nuevo_id] = {
            "activo": True,
            "nombre": nombre,
            "domicilio": domicilio,
            "email": email,
            "telefonos": telefonos,
        }

        guardarArchivoJSON("./JSON/clientes.json", clientes)

        #Mensaje de confirmacion al usuario
        print("Cliente registrado con éxito.")

        return clientes
    except(TypeError) as detalle:
        print("No se encontraron registros: ", detalle)

def modificarCliente():
    """
    Permite actualizar los datos básicos (nombre y domicilio) de un cliente existente.
    Solicita el ID del cliente y permite ingresar nuevos valores. Si el usuario deja un campo en blanco, se conserva el valor actual.
    
    Parametros:

    Returns:
        dict: El diccionario de clientes con los datos actualizados

    """
    clientes = cargarArchivoJSON("./JSON/clientes.json")

    print("=== Modificar cliente ===")

    if len(clientes) == 0:
        print("No hay clientes registrados.")
        return clientes

    listarClientes()

    id_cliente = input("Ingrese el ID del cliente a modificar: ").strip()

    if id_cliente not in clientes:
        print("ID de cliente no encontrado.")
        return clientes

    print("Deje en blanco para mantener el valor actual.")
    nuevo_nombre = input(f"Nuevo nombre ({clientes[id_cliente]['nombre']}): ").strip()
    nuevo_domicilio = input(f"Nuevo domicilio ({clientes[id_cliente]['domicilio']}): ").strip()

    if nuevo_nombre != "":
        clientes[id_cliente]['nombre'] = nuevo_nombre
    if nuevo_domicilio != "":
        clientes[id_cliente]['domicilio'] = nuevo_domicilio

    guardarArchivoJSON("./JSON/clientes.json", clientes)

    print("Cliente modificado con éxito.")
    return clientes

def eliminarCliente():
    """
    Realiza una baja lógica de un cliente cambiando su estado a inactivo.
    Solicita el ID del cliente y, si existe en el registro, cambia el valor de la clave 'activo' a False.

    Parametros:
        clientes (dict)

    Returns:
        dict: El diccionario actualizado tras la baja lógica.
    """

    clientes = cargarArchivoJSON("./JSON/clientes.json")

    print("=== Eliminar cliente ===")

    if len(clientes) == 0:
        print("No hay clientes registrados.")
        return clientes
    
    listarClientes()

    id_cliente = str(int(input("Ingrese el ID del cliente a eliminar: ")))

    if id_cliente not in clientes:
        print("ID de cliente no encontrado.")
        return clientes
    
    clientes[id_cliente]["activo"] = False

    guardarArchivoJSON("./JSON/clientes.json", clientes)

    print("Cliente eliminado con éxito.")
    return clientes

def listarClientes():
    """
    Enlista los clientes activos con sus respectivos datos

    Returns:
        dict: Devuelve el diccionario de clientes
    """

    try:
        clientes = cargarArchivoJSON("./JSON/clientes.json")

        print("=== Lista de Clientes ===")

        if len(clientes) == 0:
            print("No hay clientes registrados.")
            return
        
        print(f"{'ID':<5} {'Nombre':<30} {'Domicilio':<30} {'Telefono':<15}")
        print('*' * 100)

        for id_cliente, datos in clientes.items():
            if datos["activo"] == True:
                print(f"{id_cliente:<5} {datos['nombre']:<30} {datos['domicilio']:<30} {datos['telefonos']['telefono1']:<15}")

        return
    
    except(TypeError) as detalle:
        print("No se encontraron registros: ", detalle)


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    ...


# Punto de entrada al programa
main()
