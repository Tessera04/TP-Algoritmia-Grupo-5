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
from Validaciones import *

#----------------------------------------------------------------------------------------------
# FUNCIONES Herramientas
#----------------------------------------------------------------------------------------------
def registrarHerramienta():
    """
    Registra una nueva herramienta en el inventario solicitando datos por consola.

    La función calcula automáticamente el siguiente ID disponible basándose
    en las claves existentes del diccionario. Luego, solicita al usuario
    ingresar el nombre, costo diario y stock de la herramienta.

    Archivos:
        herramientas.json (dict)
    """
    try:
        herramientas = cargarArchivoJSON("./JSON/herramientas.json")

        print("=== Registrar nueva herramienta ===")
        #Logica para registrar una nueva herramienta
        if len(herramientas) == 0:
            nuevo_id = "1"
        else:
            nuevo_id = str(int(max(herramientas.keys())) + 1)

        #Solicitar datos
        #Solicitar Nombre
        nombre = validarTexto("Ingrese el nombre de la herramienta: ", "El nombre de la herramienta no puede estar vacio.")
        
        #Solicitar costo_diario
        costo_diario = float(validarNegativos("Ingrese el costo diario de alquiler ($): ", "El valor del costo diario no puede ser 0 o menos."))

        #Solicitar stock
        stock = validarNegativos("Ingrese el stock disponible: ", "El stock disponible no puede ser 0 o menos.")

        #Solicitar potencia
        potencia = validarTextoNA("Ingrese la potencia de la herramienta: ", "El valor no puede estar vacio, queda como N/A")

        #Solicitar voltaje
        voltaje = validarTextoNA("Ingrese el voltaje de la herramienta: ", "El valor no puede estar vacio, queda como N/A")

        #Solicitar peso
        peso = validarTextoNA("Ingrese el peso de la herramienta: ", "El valor no puede estar vacio, queda como N/A")

        #Solicitar velocidad
        velocidad = validarTextoNA("Ingrese la velocidad de la herramienta: ", "El valor no puede estar vacio, queda como N/A")

        #Validaciones


        #Agregar al diccionario
        herramientas[nuevo_id] = {
            "activa": True,
            "nombre": nombre,
            "costo_diario": costo_diario,
            "stock": stock,
            "especificaciones": {
                "potencia": potencia,
                "voltaje": voltaje,
                "peso": peso,
                "velocidad": velocidad
            }
        }

        guardarArchivoJSON("./JSON/herramientas.json", herramientas)

        print("Herramienta registrada con éxito.")
    except(TypeError) as detalle:
        print("No se encontraron registros: ", detalle)
    except Exception as e:
        print("ERROR!: Error inesperado al guardar el archivo: ", e)

def modificarHerramienta():
    """
    Permite al usuario modificar los atributos de una herramienta seleccionada.
    Si el diccionario de herramientas esta vacio, la funcion termina anticipadamente.
    Pide el id de la herramienta a modificar y luego solicita datos como el nuevo nombre, nuevo costo, nuevo stock, permitiendo dejar en blanco para dejar el valor actual.

    Archivos:
        herramientas.json (dict)

    """
    try:
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
        
        h = herramientas[id_herramienta]
        
        print("\n Deje en blanco para mantener el valor actual. \n")

        nueva_nombre = input(f"Nuevo nombre ({h['nombre']}): ").strip()

        nuevo_costo = input(f"Nuevo costo diario ({h['costo_diario']}): ").strip()
        if nuevo_costo != "":
            try:
                nuevo_costo = float(nuevo_costo)
            except ValueError:
                print("Costo invalido. No se modifico.")
                nuevo_costo = ""

        nuevo_stock = input(f"Nuevo stock ({h['stock']}): ").strip()
        if nuevo_stock != "":
            try:
                nuevo_stock = int(nuevo_stock)
            except ValueError:
                print("Stock invalido. No se modifico.")
                nuevo_stock = ""
        
        espec = h['especificaciones']

        nueva_potencia = input(f"Nuevo potencia ({espec['potencia']}): ").strip()
        nuevo_voltaje = input(f"Nuevo voltaje ({espec['voltaje']}): ").strip()
        nuevo_peso = input(f"Nuevo peso ({espec['peso']}): ").strip()
        nuevo_velocidad = input(f"Nuevo velocidad ({espec['velocidad']}): ").strip()

        if nueva_nombre != "":
            h['nombre'] = nueva_nombre
        if nuevo_costo != "":
            h['costo_diario'] = float(nuevo_costo)
        if nuevo_stock != "":
            h['stock'] = int(nuevo_stock)
        if nueva_potencia != "":
            espec['potencia'] = str(nueva_potencia)        
        if nuevo_voltaje != "":
            espec['voltaje'] = str(nuevo_voltaje)
        if nuevo_peso != "":
            espec['peso'] = str(nuevo_peso)
        if nuevo_velocidad != "":
            espec['velocidad'] = str(nuevo_velocidad)

        guardarArchivoJSON("./JSON/herramientas.json", herramientas)
        
        print("Herramienta modificada con éxito.")

    except(TypeError) as detalle:
        print("No se encontraron registros: ", detalle)
    except Exception as e:
        print("ERROR!: Error inesperado al guardar el archivo: ", e)

def eliminarHerramienta():
    """
    Realiza una baja lógica de una herramienta cambiando su estado a inactivo

    Archivos:
        herramientas.json (dict)
    
    """
    try:
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

    except(TypeError) as detalle:
        print("No se encontraron registros: ", detalle)
    except Exception as e:
        print("ERROR!: Error inesperado al guardar el archivo: ", e)


def listarHerramientas():
    """
    Muestra un listado de todas las herramientas que se encuentran activas

    Archivos:
        herramientas.json (dict)

    Returns:
        None: Esta función solo imprime datos en pantalla y no retorna ningún valor.
    """
    try:
        herramientas = cargarArchivoJSON("./JSON/herramientas.json")

        print("=== Lista de Herramientas ===")

        if len(herramientas) == 0:
            print("No hay herramientas registradas.")
            return
        
        print(f"{'ID':<5} {'Nombre':<50} {'Costo Diario ($)':<30} {'Stock':<20} {'Potencia':<20} {'Voltaje':<20} {'Peso':<20} {'Velocidad':<20}")
        print('-' * 200)

        for id_herramienta, datos in herramientas.items():
            if datos["activa"] == True:
                print(f"{id_herramienta:<5} {datos['nombre']:<50} {datos['costo_diario']:<30} {datos['stock']:<20} {datos['especificaciones']['potencia']:<20} {datos['especificaciones']['voltaje']:<20} {datos['especificaciones']['peso']:<20} {datos['especificaciones']['velocidad']:<20}")
        
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
