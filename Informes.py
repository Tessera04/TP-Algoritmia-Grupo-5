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
# FUNCIONES Informes
#----------------------------------------------------------------------------------------------

def informeVentasYRecaudacionMensual(alquileres):
    print(f"{'Fecha/Hora':<30} {'Cliente':<50} {'Producto':<50} {'Cant.':<15} {'Unit.':<15} {'Total':<15}")
    print('-' * 200)
    return

def informeVentasPorProductoCantidades(alquileres):
    print("---------------------------")
    print("=== CANTIDADES TOTALES POR MES (UNIDADES ALQUILADAS) ===")
    print("---------------------------")
    print(f"{'Producto':<5} {'ENERO-24 ':<50} {'FEBRERO-25':<10}")
    print('-' * 200)
    return

def informeVentasPorProductoPrecios(alquileres, herramientas):

    # Solicitar rango de fechas al usuario
    anio_inicio = int(input("Ingrese el año de inicio (por ejemplo 2024): "))
    mes_inicio = int(input("Ingrese el mes de inicio (1-12): "))
    anio_fin = int(input("Ingrese el año de fin (por ejemplo 2024): "))
    mes_fin = int(input("Ingrese el mes de fin (1-12): "))

    fecha_inicio = datetime(anio_inicio, mes_inicio, 1)
    fecha_fin = datetime(anio_fin, mes_fin, 28)

    if fecha_fin < fecha_inicio:
        print("Error: la fecha final debe ser posterior a la fecha inicial.")
        return
    
    # Calcular cantidad de meses en el rango
    meses_diferencia = (anio_fin - anio_inicio) * 12 + (mes_fin - mes_inicio + 1)
    if meses_diferencia > 10:
        print("Error: el rango no puede superar los 10 meses.")
        return
    
    meses_abrev = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN",
                   "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]
    
    # Generar lista de meses a mostrar
    meses_mostrar = []
    fecha_actual = fecha_inicio
    while fecha_actual <= fecha_fin:
        etiqueta = f"{meses_abrev[fecha_actual.month - 1]}.{str(fecha_actual.year)[2:]}"
        meses_mostrar.append(etiqueta)
        nuevo_mes = fecha_actual.month + 1
        nuevo_anio = fecha_actual.year
        if nuevo_mes > 12:
            nuevo_mes = 1
            nuevo_anio += 1
        fecha_actual = datetime(nuevo_anio, nuevo_mes, 1)

        # Crear estructura base
    resumen = {}
    for id_h, datos_h in herramientas.items():
        resumen[datos_h["nombre"]] = {mes: 0 for mes in meses_mostrar}

    # Recorrer alquileres dentro del rango
    for datos in alquileres.values():
        id_h = datos["id_herramienta"]
        fecha_str = datos["fecha_inicio"]
        precio_diario = datos["total"] / datos["dias_alquiler"]
        dias = datos["dias_alquiler"]

        fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
        if fecha < fecha_inicio or fecha > fecha_fin:
            continue

        monto = precio_diario * dias
        etiqueta_mes = f"{meses_abrev[fecha.month - 1]}.{str(fecha.year)[2:]}"
        nombre_h = herramientas[id_h]["nombre"]

        if etiqueta_mes in resumen[nombre_h]:
            resumen[nombre_h][etiqueta_mes] += monto

    print("-" * 150)
    print("CANTIDADES TOTALES POR MES (PESOS)")
    print("-" * 150)
        
    # Encabezado
    print(f"{'Producto':<50}", end="")
    for mes in meses_mostrar:
        print(f"{mes:^10}", end="")
    print()
    print("-" * 150)

    # Filas
    for producto, valores in resumen.items():
        print(f"{producto:<50}", end="")
        for mes in meses_mostrar:
            print(f"{valores[mes]:>10.0f}", end="")
        print()
    print("-" * 150)

    return

def informeHerramientasInactivas(herramientas, alquileres):
    print(f"{'ID':<5} {'Herramienta ':<50} {'Estado':<10}")
    print('*' * 200)
    return

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    ...


# Punto de entrada al programa
main()
