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
import re

#----------------------------------------------------------------------------------------------
# FUNCIONES Validaciones
#----------------------------------------------------------------------------------------------
def validarTexto(textoInput, textoOutput):
    """
    Valida que el texto cumpla las validaciones.

    Parametros:
        variable (str)
        textoInput (str)
        textoOutput (str)
    Returns:
        variable (str)
    """
    variable = ""
    while variable == "":
        variable = str(input(textoInput)).strip()
        if variable == "":
            print(textoOutput)
    return variable

def validarNegativos(textoInput, textoOutput):
    variable = -1
    while variable <= 0:
        try:
            variable = int(input(textoInput))
            if variable <= 0:
                print(textoOutput)
        except ValueError:
            print("Debe ingresar un numero valido!")
            variable = -1
    return variable

def validarTextoNA(textoInput, textoOutput):
    """
    Valida que el texto cumpla las validaciones.

    Parametros:
        variable (str)
        textoInput (str)
        textoOutput (str)
    Returns:
        variable (str)
    """
    variable = ""
    variable = str(input(textoInput)).strip()
    if variable == "":
        print(textoOutput)
        variable = "N/A"
    return variable

def validarTelefono(telefono):
    """
    Valida que el telefono cumpla el patron especificado.

    Parametros:
        telefono (str)
    Returns:
        Bool (True o False)
    """
    patron = r'^\d{2}-\d{4}-\d{4}$'
    if re.match(patron, telefono):
        return True
    else:
        return False

def validarEmail(email):
    """
    Valida que el email cumpla el patron especificado.

    Parametros:
        email (str)
    Returns:
        Bool (True o False)
    """
    patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(patron, email):
        return True
    else:
        return False

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    ...


# Punto de entrada al programa
main()