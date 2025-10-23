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
# FUNCIONES Herramientas
#----------------------------------------------------------------------------------------------
def registrarHerramienta(herramientas):
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

    print("Herramienta registrada con éxito.")
    return herramientas

def modificarHerramienta(herramientas):
    print("=== Modificar herramienta ===")

    if len(herramientas) == 0:
        print("No hay herramientas registradas.")
        return herramientas
    
    listarHerramientas(herramientas)

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
    
    print("Herramienta modificada con éxito.")
    return herramientas

def eliminarHerramienta(herramientas):
    print("=== Eliminar herramienta ===")
    
    if len(herramientas) == 0:
        print("No hay herramientas registradas.")
        return herramientas

    listarHerramientas(herramientas)

    id_herramienta = input("Ingrese el ID de la herramienta a eliminar: ").strip()

    if id_herramienta not in herramientas:
        print("ID de herramienta no encontrado.")
        return herramientas
    
    herramientas[id_herramienta]["activa"] = False
    print("Herramienta eliminada con éxito.")
    return herramientas


def listarHerramientas(herramientas):
    print("=== Lista de Herramientas ===")

    if len(herramientas) == 0:
        print("No hay herramientas registradas.")
        return
    
    print(f"{'ID':<5} {'Nombre':<25} {'Costo Diario ($)':<20} {'Stock':<10} {'Activa':<10}")
    print('-' * 80)
    for id_herramienta, datos in herramientas.items():
        estado = "Sí" if datos["activa"] else "No"
        print(f"{id_herramienta:<5} {datos['nombre']:<25} {datos['costo_diario']:<20.2f} "
              f"{datos['stock']:<10} {estado:<10}")
    return

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    ...


# Punto de entrada al programa
main()
