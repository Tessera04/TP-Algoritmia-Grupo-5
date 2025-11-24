"""
-----------------------------------------------------------------------------------------------
Título: Trabajo Práctico Grupo 5 - Sistema de Gestión de Alquiler de Herramientas
Fecha: 22/10/2025
Autor: Vicente Courtinade, Marcos Gimenez, Matias Gonzalez, Lautaro Ruisoto, Santiago Salas.

Descripción: Módulo para manejo de persistencia de datos (lectura y escritura en archivos).

Pendientes:
-----------------------------------------------------------------------------------------------
"""
#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import json

#----------------------------------------------------------------------------------------------
# FUNCIONES Archivos
#----------------------------------------------------------------------------------------------
def cargarArchivoJSON(ruta):
    """
    Carga un archivo JSON y devuelve su contenido como dict.

    Parametros:
        ruta (str)
    Returns:
        datos(dict) | None
    """
    try:
        archivo = open(ruta, mode="r", encoding="utf-8")
        datos = json.load(archivo)
        archivo.close()
        return datos
    except (FileNotFoundError, OSError) as detalle:
        print(f"Error al abrir {ruta}: {detalle}")
        return None

def guardarArchivoJSON(ruta, datos):
    """
    Guarda datos en formato diccionario en un archivo JSON.

    Parametros:
        ruta (str)
        datos (dict)
    
    Returns:
        None
    """
    try:
        archivo = open(ruta, mode="w", encoding="utf-8")
        json.dump(datos, archivo, ensure_ascii=False, indent=4)
        archivo.close()
    except (FileNotFoundError, OSError) as detalle:
        print(f"Error al abrir {ruta}: {detalle}")
        return None

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    ...


# Punto de entrada al programa
main()
