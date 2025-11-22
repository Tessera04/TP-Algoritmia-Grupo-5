"""
-----------------------------------------------------------------------------------------------
Título: Trabajo Práctico Grupo 5 - Sistema de Gestión de Alquiler de Herramientas
Fecha: 22/10/2025
Autor: Vicente Courtinade, Marcos Gimenez, Matias Gonzalez, Lautaro Ruisoto, Santiago Salas.

Descripción: Módulo de Informes del sistema de gestión de alquiler de herramientas. Proporciona funciones para generar informes detallados sobre ventas,
recaudación mensual, cantidades y precios por producto, y herramientas menos utilizadas.

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

def informeVentasYRecaudacionMensual(alquileres, clientes, herramientas):
    """
    Generar un informe con todas las ventas y la recaudacion del mes actual

    Parametros:
        alquileres (dict)
        clientes (dict)
        herramientas (dict)

    Devuelve:
        None
    """



    print("---------------------------")
    print("=== INFORME DE VENTAS Y RECAUDACION MENSUAL ===")
    print("---------------------------")

    # Obtener mes y año actual del sistema
    fecha_actual = datetime.now()
    mes_actual = fecha_actual.month
    anio_actual = fecha_actual.year

    print(f"OPERACIONES DEL MES {mes_actual}/{anio_actual}")
    print('-' * 150)
    print(f"{'Fecha/Hora':<20} {'Cliente':<40} {'Producto':<40} {'Cant.':<15} {'Unit.':<15} {'Total':<15}")
    print('-' * 150)

    total_mes = 0
    hay_datos = False
    
    for alquiler in alquileres:
        datos = alquileres[alquiler]
        fecha = datetime.strptime(datos["fecha_inicio"], "%Y-%m-%d")

        if fecha.year == anio_actual and fecha.month == mes_actual:
            hay_datos = True

            idCliente = datos["id_cliente"]
            idHerramienta = datos["id_herramienta"]

            if idCliente in clientes:
                nombre_cliente = clientes[idCliente]["nombre"]
            else:
                nombre_cliente = "Cliente Desconocido"

            if idHerramienta in herramientas:
                nombre_herramienta = herramientas[idHerramienta]["nombre"]
                precio_unitario = herramientas[idHerramienta]["costo_diario"]
            else:
                nombre_herramienta = "Herramienta Desconocida"
                precio_unitario = 0
            
            dias = datos["dias_alquiler"]
            total = datos["total"]
            total_mes += total

            print(f"{datos['fecha_inicio']:<20} {nombre_cliente:<40} {nombre_herramienta:<40} {dias:<15} {precio_unitario:<15.2f} {total:<15.2f}")
            
    if not hay_datos:
        print("No se registraron operaciones en este mes.")
    else:
        print('-' * 150)
        print(f"{'TOTAL RECAUDADO EN EL MES:':<130} {total_mes:<15.2f}")
        print('-' * 150)
    return

def informeVentasPorProductoCantidades(alquileres, herramientas):
    """
    Generar un informe de cantidades alquiladas por producto dentro de un rango de meses

    Parametros:
        alquileres (dict)
        herramientas (dict)

    Devuelve:
        None
    """


    print("---------------------------")
    print("=== CANTIDADES TOTALES POR MES ===")
    print("---------------------------")
    print("Rango máximo: 10 meses.")

    # Solicitar rango de fechas al usuario
    anio_inicio = int(input("Ingrese el año de inicio (por ejemplo 2025): "))
    mes_inicio = int(input("Ingrese el mes de inicio (1-12): "))
    anio_fin = int(input("Ingrese el año de fin (por ejemplo 2025): "))
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
        resumen[datos_h["nombre"]] = {}
        for mes in meses_mostrar:
            resumen[datos_h["nombre"]][mes] = 0

    # Recorrer alquileres dentro del rango
    for id_a in alquileres:
        datos = alquileres[id_a]
        id_h = datos["id_herramienta"]
        fecha_str = datos["fecha_inicio"]
        dias = datos["dias_alquiler"]

        fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
        if fecha < fecha_inicio or fecha > fecha_fin:
            continue

        etiqueta_mes = f"{meses_abrev[fecha.month - 1]}.{str(fecha.year)[2:]}"
        nombre_h = herramientas[id_h]["nombre"]

        if etiqueta_mes in resumen[nombre_h]:
            resumen[nombre_h][etiqueta_mes] += dias

    # Mostrar tabla
    print("-" * 150)
    print("CANTIDADES TOTALES POR MES")
    print("-" * 150)

    # Encabezado
    print(f"{'Producto':<50}", end="")
    for mes in meses_mostrar:
        print(f"{mes:^10}", end="")
    print()
    print("-" * 150)

    # Filas
    for producto in resumen:
        print(f"{producto:<50}", end="")
        for mes in meses_mostrar:
            print(f"{resumen[producto][mes]:>10.0f}", end="")
        print()
    print("-" * 150)

    return

def informeVentasPorProductoPrecios(alquileres, herramientas):
    """
    Generar un informe del total recaudado por producto dentro de un rango de meses

    Parametros:
        alquileres (dict)
        herramientas (dict)

    Devuelve:
        None
    """
        


    print("---------------------------")
    print("=== PRECIOS TOTALES POR MES (PESOS) ===")
    print("---------------------------")
    print("Rango maximo: 10 meses.")

    # Solicitar rango de fechas al usuario
    anio_inicio = int(input("Ingrese el año de inicio (por ejemplo 2025): "))
    mes_inicio = int(input("Ingrese el mes de inicio (1-12): "))
    anio_fin = int(input("Ingrese el año de fin (por ejemplo 2025): "))
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
    """
    Generar un informe de las herramientas menos utilizadas durante el mes actual

    Parametros:
        herramientas (dict)
        alquileres (dict)

    Devuelve:
        None
    """
        


    print("---------------------------")
    print("=== INFORME DE HERRAMIENTAS MENOS UTILIZADAS (MES ACTUAL) ===")
    print("---------------------------")

    hoy = datetime.now()
    mes_actual = hoy.month
    anio_actual = hoy.year

    # Crear resumen base
    resumen = {}
    for idHerramientas, datos_h in herramientas.items():
        resumen[idHerramientas] = {
            "nombre": datos_h["nombre"],
            "cantidad": 0,
            "total": 0.0
        }

    # Contar alquileres del mes actual
    for datos in alquileres.values():
        fecha = datetime.strptime(datos["fecha_inicio"], "%Y-%m-%d")
        if fecha.year == anio_actual and fecha.month == mes_actual:
            idHerramientas = datos["id_herramienta"]
            resumen[idHerramientas]["cantidad"] = resumen[idHerramientas]["cantidad"] + 1
            resumen[idHerramientas]["total"] = resumen[idHerramientas]["total"] + datos["total"]

    # Convertir a lista para ordenar manualmente
    lista_resumen = []
    for idHerramientas in resumen:
        item = {
            "id": idHerramientas,
            "nombre": resumen[idHerramientas]["nombre"],
            "cantidad": resumen[idHerramientas]["cantidad"],
            "total": resumen[idHerramientas]["total"]
        }
        lista_resumen.append(item)

    # Ordenamiento manual (por cantidad y luego total)
    for i in range(len(lista_resumen) - 1):
        for j in range(i + 1, len(lista_resumen)):
            if (lista_resumen[i]["cantidad"] > lista_resumen[j]["cantidad"]) or \
               (lista_resumen[i]["cantidad"] == lista_resumen[j]["cantidad"] and lista_resumen[i]["total"] > lista_resumen[j]["total"]):
                aux = lista_resumen[i]
                lista_resumen[i] = lista_resumen[j]
                lista_resumen[j] = aux

    # Mostrar resultados
    print(f"{'ID':<5} {'Herramienta':<50} {'Cant.Alq':<12} {'Monto ($)':<12} {'Estado':<10}")
    print("-" * 120)

    for item in lista_resumen:
        estado = "Inactiva"
        if item["cantidad"] > 0:
            estado = "Activa"
        print(f"{item['id']:<5} {item['nombre']:<50} {item['cantidad']:<12} {item['total']:<12.2f} {estado:<10}")

    print("-" * 120)
    print("Las herramientas inactivas son aquellas sin registros en el mes actual.")
    print("-" * 120)
    return

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    ...


# Punto de entrada al programa
main()
