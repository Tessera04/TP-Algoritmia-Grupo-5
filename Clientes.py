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
import json

#----------------------------------------------------------------------------------------------
# FUNCIONES Clientes
#----------------------------------------------------------------------------------------------
def registrarCliente(clientes):
    """
    Registra un nuevo cliente solicitando datos personales y permitiendole ingresar 1 o mas telefonos.

    Parametros:
    clientes (dict)

    Returns:
    dict: El diccionario 'clientes' actualizado con la nueva entrada y sus teléfonos asociados.
    """
    print("=== Registrar nuevo cliente ===")
    # Lógica para registrar un nuevo id de cliente
    if len(clientes) == 0:
        nuevo_id = "1"
    else:
        nuevo_id = str(int(max(clientes.keys())) + 1)

    #Solicitar datos del cliente
    nombre = input("Ingrese el nombre del cliente: ").strip()
    domicilio = input("Ingrese el domicilio del cliente: ").strip()

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
        "nombre": nombre,
        "domicilio": domicilio,
        "telefonos": telefonos,
        "activo": True
    }
    #Mensaje de confirmacion al usuario
    print("Cliente registrado con éxito.")

    return clientes

def modificarCliente(clientes):
    """
    Permite actualizar los datos básicos (nombre y domicilio) de un cliente existente.
    Solicita el ID del cliente y permite ingresar nuevos valores. Si el usuario deja un campo en blanco, se conserva el valor actual.
    
    Parametros:
        clientes (dict):
    Returns:
        dict: El diccionario de clientes con los datos actualizados

    """
    print("=== Modificar cliente ===")

    if len(clientes) == 0:
        print("No hay clientes registrados.")
        return clientes

    listarClientes(clientes)

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

    print("Cliente modificado con éxito.")
    return clientes

def eliminarCliente(clientes):
    """
    Realiza una baja lógica de un cliente cambiando su estado a inactivo.
    Solicita el ID del cliente y, si existe en el registro, cambia el valor de la clave 'activo' a False.

    Parametros:
        clientes (dict)

    Returns:
        dict: El diccionario actualizado tras la baja lógica.
    """
    print("=== Eliminar cliente ===")

    if len(clientes) == 0:
        print("No hay clientes registrados.")
        return clientes
    
    listarClientes(clientes)

    id_cliente = str(int(input("Ingrese el ID del cliente a eliminar: ")))

    if id_cliente not in clientes:
        print("ID de cliente no encontrado.")
        return clientes
    
    clientes[id_cliente]["activo"] = False
    print("Cliente eliminado con éxito.")
    return clientes

def listarClientes():
    """
    Enlista los clientes activos con sus respectivos datos

    Returns:
        dict: Devuelve el diccionario de clientes
    """

    try:
        archivo = open("./JSON/clientes.json", mode="r", encoding="utf-8")
        clientes = json.load(archivo)

        print("=== Lista de Clientes ===")

        if len(clientes) == 0:
            print("No hay clientes registrados.")
            return
        
        print(f"{'ID':<5} {'Nombre':<30} {'Domicilio':<30} {'Telefono':<15}")
        print('*' * 100)

        for id_cliente, datos in clientes.items():
            if datos["activo"] == True:
                print(f"{id_cliente:<5} {datos['nombre']:<30} {datos['domicilio']:<30} {datos['telefonos']['telefono1']:<15}")

        archivo.close()
        return
    
    except(FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir el archivo: ", detalle)


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    ...


# Punto de entrada al programa
main()
