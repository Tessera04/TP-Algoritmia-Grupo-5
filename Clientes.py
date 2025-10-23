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
...

#----------------------------------------------------------------------------------------------
# FUNCIONES Clientes
#----------------------------------------------------------------------------------------------
def registrarCliente(clientes):
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
    ...
    return clientes

def eliminarCliente(clientes):
    print("=== Eliminar cliente ===")

    if len(clientes) == 0:
        print("No hay clientes registrados.")
        return clientes
    
    listarClientes(clientes)

    id_cliente = int(input("Ingrese el ID del cliente a eliminar: "))

    if id_cliente not in clientes:
        print("ID de cliente no encontrado.")
        return clientes
    
    clientes[id_cliente]["activo"] = False
    print("Cliente eliminado con éxito.")
    return clientes

def listarClientes(clientes):
    print("=== Lista de Clientes ===")

    if len(clientes) == 0:
        print("No hay clientes registrados.")
        return
    
    print(f"{'ID':<5} {'Nombre':<30} {'Domicilio':<30} {'Telefono':<15} {'Activo':<10}")
    print('*' * 100)
    for id_cliente, datos in clientes.items():
        estado = "Si" if datos["activo"] else "No"
        print(f"{id_cliente:<5} {datos['nombre']:<30} {datos['domicilio']:<30} {datos['telefonos']['telefono1']:<15} {estado}")
    return

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    ...


# Punto de entrada al programa
main()
