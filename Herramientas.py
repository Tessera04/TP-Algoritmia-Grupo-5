"""
-----------------------------------------------------------------------------------------------
Título: Trabajo Práctico Grupo 5 - Sistema de Gestión de Alquiler de Herramientas
Fecha: 22/10/2025
Autor: Vicente Courtinade, Marcos Gimenez, Matias Gonzalez, Lautaro Ruisoto, Santiago Salas.

Descripción: Módulo de Herramientas del sistema de gestión de alquiler de herramientas. 
Proporciona funciones CRUD para registrar, modificar, eliminar y listar herramientas disponibles para alquiler.

Pendientes:
-----------------------------------------------------------------------------------------------
"""
#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
from Archivos import *

#----------------------------------------------------------------------------------------------
# FUNCIONES Herramientas
#----------------------------------------------------------------------------------------------
def registrarHerramienta():
    """
    Registra una nueva herramienta en el inventario solicitando datos por consola.

    La función calcula automáticamente el siguiente ID disponible basándose
    en las claves existentes del diccionario. Luego, solicita al usuario
    ingresar el nombre, costo diario y stock de la herramienta.

    Parametros:
        herramientas (dict)

    Returns:
        dict: El diccionario 'herramientas' actualizado con el nuevo registro
    
    
    """

    herramientas = cargarArchivoJSON("./JSON/herramientas.json")

    print("=== Registrar nueva herramienta ===")
    #Logica para registrar una nueva herramienta
    if len(herramientas) == 0:
        nuevo_id = "1"
    else:
        nuevo_id = str(int(max(herramientas.keys())) + 1)

    #Solicitar datos
    nombre = input("Ingrese el nombre de la herramienta: ").strip()
    costo_diario = float(input("Ingrese el costo diario de alquiler ($): "))
    stock = int(input("Ingrese el stock disponible: "))

    #Agregar al diccionario
    herramientas[nuevo_id] = {
        "nombre": nombre,
        "costo_diario": costo_diario,
        "stock": stock,
        "activa": True
    }

    guardarArchivoJSON("./JSON/herramientas.json", herramientas)

    print("Herramienta registrada con éxito.")
    return herramientas

def modificarHerramienta():
    """
    Permite al usuario modificar los atributos de una herramienta seleccionada.
    Si el diccionario de herramientas esta vacio, la funcion termina anticipadamente.
    Pide el id de la herramienta a modificar y luego solicita datos como el nuevo nombre, nuevo costo, nuevo stock, permitiendo dejar en blanco para dejar el valor actual.

    parametros:
        herramientas (dic)
    returns:
        El diccionario actualizado con las modificaciones realizadas, o el mismo diccionario si no hubo cambios o el ID no era válido

    """

    herramientas = cargarArchivoJSON("./JSON/herramientas.json")

    print("=== Modificar herramienta ===")

    if len(herramientas) == 0:
        print("No hay herramientas registradas.")
        return herramientas
    
    listarHerramientas()

    id_herramienta = input("Ingrese el ID de la herramienta a modificar: ").strip()

    if id_herramienta not in herramientas:
        print("ID de herramienta no encontrado.")
        return herramientas
    
    print("Deje en blanco para mantener el valor actual.")
    nueva_nombre = input(f"Nuevo nombre ({herramientas[id_herramienta]['nombre']}): ").strip()
    nuevo_costo = input(f"Nuevo costo diario ({herramientas[id_herramienta]['costo_diario']}): ").strip()
    nuevo_stock = input(f"Nuevo stock ({herramientas[id_herramienta]['stock']}): ").strip()

    if nueva_nombre != "":
        herramientas[id_herramienta]['nombre'] = nueva_nombre
    if nuevo_costo != "":
        herramientas[id_herramienta]['costo_diario'] = float(nuevo_costo)
    if nuevo_stock != "":
        herramientas[id_herramienta]['stock'] = int(nuevo_stock)

    guardarArchivoJSON("./JSON/herramientas.json", herramientas)
    
    print("Herramienta modificada con éxito.")
    return herramientas

def eliminarHerramienta():
    """
    Realiza una baja lógica de una herramienta cambiando su estado a inactivo

    Parametros:
        herramientas (dict)
    
    return:
    El diccionario actualizado con el estado de la herramienta modificado.
    """

    herramientas = cargarArchivoJSON("./JSON/herramientas.json")

    print("=== Eliminar herramienta ===")
    
    if len(herramientas) == 0:
        print("No hay herramientas registradas.")
        return herramientas

    listarHerramientas()

    id_herramienta = input("Ingrese el ID de la herramienta a eliminar: ").strip()

    if id_herramienta not in herramientas:
        print("ID de herramienta no encontrado.")
        return herramientas
    
    herramientas[id_herramienta]["activa"] = False

    guardarArchivoJSON("./JSON/herramientas.json", herramientas)

    print("Herramienta eliminada con éxito.")
    return herramientas


def listarHerramientas():
    """
    Muestra un listado de todas las herramientas que se encuentran activas

    Parametros:
    herramientas (dict)

    Returns:
    None: Esta función solo imprime datos en pantalla y no retorna ningún valor.
    """
    try:
        herramientas = cargarArchivoJSON("./JSON/herramientas.json")

        print("=== Lista de Herramientas ===")

        if len(herramientas) == 0:
            print("No hay herramientas registradas.")
            return
        
        print(f"{'ID':<5} {'Nombre':<50} {'Costo Diario ($)':<30} {'Stock':<20}")
        print('-' * 120)

        for id_herramienta, datos in herramientas.items():
            if datos["activa"] == True:
                print(f"{id_herramienta:<5} {datos['nombre']:<50} {datos['costo_diario']:<30} "
                    f"{datos['stock']:<20}")
        
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
