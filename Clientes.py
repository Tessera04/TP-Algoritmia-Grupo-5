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
from Validaciones import *

#----------------------------------------------------------------------------------------------
# FUNCIONES Clientes
#----------------------------------------------------------------------------------------------


def registrarCliente():
    """
    Registra un nuevo cliente solicitando datos personales y permitiendole ingresar 1 o mas telefonos.

    Archivos:
        ./JSON/Clientes.json
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
        nombre = validarTexto("Ingrese el nombre del cliente : ", "El nombre del cliente no puede estar vacio.")
        domicilio = validarTexto("Ingrese el domicilio del cliente : ", "El domicilio del cliente no puede estar vacio.")
        email = validarTexto("Ingrese el email del cliente : ", "El email del cliente no puede estar vacio.")

        while validarEmail(email) == False:
            print("Email invalido, intente nuevamente: ")
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
    except TypeError as detalle:
        print("ERROR!: Error de tipo inesperado en los datos cargados.", detalle)
    except Exception as e:
        print("ERROR!: Error inesperado al guardar el archivo: ", e)

def modificarCliente():
    """
    Permite actualizar los datos básicos (nombre y domicilio) de un cliente existente.
    Solicita el ID del cliente y permite ingresar nuevos valores. Si el usuario deja un campo en blanco, se conserva el valor actual.
    
    Archivos:
        ./JSON/clientes.json
    """
    try:
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

        cliente = clientes[id_cliente]
        telefonos = cliente.get("telefonos", {})

        print("\n Deje en blanco para mantener el valor actual. \n")

        nuevo_nombre = input(f"Nuevo nombre ({cliente['nombre']}): ").strip()
        nuevo_domicilio = input(f"Nuevo domicilio ({cliente['domicilio']}): ").strip()

        nuevo_email = input(f"Ingrese el nuevo email ({cliente['email']}): ").strip()
        while validarEmail(nuevo_email) == False:
            print("Email invalido, intente nuevamente: ")
            nuevo_email = str(input("Ingrese un email valido: ")).strip()

        print("\n --- Modificar Telefonos --- \n")

        tel1actual = telefonos.get("telefono1", "")
        telefono1 = input(f"Telefono 1 ({tel1actual}): ").strip()
        if telefono1 != "":
            while not validarTelefono(telefono1):
                print("Telefono invalido. Formato esperado: 11-1234-5678 o similar.")
                telefono1 = input("Telefono 1: ").strip()
        
        tel2actual = telefonos.get("telefono2", "")
        telefono2 = input(f"Telefono 2 ({tel2actual}): ").strip()
        if telefono2 != "":
            while not validarTelefono(telefono2):
                print("Telefono invalido. Formato esperado: 11-1234-5678 o similar.")
                telefono2 = input("Telefono 2: ").strip()

        if nuevo_nombre != "":
            cliente['nombre'] = nuevo_nombre
        if nuevo_domicilio != "":
            cliente['domicilio'] = nuevo_domicilio
        if nuevo_email != "":
            cliente["email"] = nuevo_email

        if telefono1 != "":
            cliente["telefonos"]["telefono1"] = telefono1
        if telefono2 != "":
            cliente["telefonos"]["telefono2"] = telefono2

        cliente["telefonos"] = telefonos

        guardarArchivoJSON("./JSON/clientes.json", clientes)

        print("Cliente modificado con éxito.")

    except TypeError as detalle:
        print("ERROR!: Error de tipo inesperado en los datos cargados.", detalle)
    except Exception as e:
        print("ERROR!: Error inesperado al guardar el archivo: ", e)

def eliminarCliente():
    """
    Realiza una baja lógica de un cliente cambiando su estado a inactivo.
    Solicita el ID del cliente y, si existe en el registro, cambia el valor de la clave 'activo' a False.

    Archivos:
        ./JSON/clientes.json
    """
    try:
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
    except Exception as e:
        print("ERROR!: Error inesperado al guardar el archivo: ", e)

def listarClientes():
    """
    Enlista los clientes activos con sus respectivos datos.

    Archivos:
        ./JSON/clientes.json
    """

    try:
        clientes = cargarArchivoJSON("./JSON/clientes.json")

        print("=== Lista de Clientes ===")

        if len(clientes) == 0:
            print("No hay clientes registrados.")
            return
        
        print(f"{'ID':<15} {'Nombre':<30} {'Domicilio':<30} {'Telefonos':<45} {'Email':<15}")
        print('*' * 135)

        for id_cliente, datos in clientes.items():
            if datos["activo"] == True:
                diccionarioTelefonos = datos.get('telefonos', {})
                stringTelefonos = " / ".join(diccionarioTelefonos.values())

                print(f"{id_cliente:<15} {datos['nombre']:<30} {datos['domicilio']:<30} {stringTelefonos:<45} {datos['email']:<30}")

        return
    
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
