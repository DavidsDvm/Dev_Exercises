"""
Enunciado

Reto 5: Inventario para una tienda de víveres

    La tienda de Pepe vende diferentes productos, usualmente frutas,
    dulces y algunos tipos de carne. Con el propósito de mejorar el control
    sobre las ventas y el inventario de la tienda,
    Pepe decide construir una aplicación que le permita almacenar
    la información de los productos y realizar algunos cálculos sobre los datos.

    En la primera parte del reto se debe construir una base de datos
    que almacene la información de los productos disponibles en la tienda.
    Debido a que Pepe no cuenta con un servidor de base de datos,
    solicita que temporalmente la base de datos sea representada mediante
    un diccionario de Python llamado productos que tendrá por llave
    el código del producto y por valor una lista formada por los atributos:
    nombre, precio e inventario.
    La Tabla 1 presenta los productos disponibles a la fecha.

        código	|  nombre	|   precio  |  inventario
        1	    |Manzanas	|5000.0	    |25
        2	    |Limones	|2300.0	    |15
        3	    |Peras	    |2700.0	    |33
        4	    |Arandanos	|9300.0	    |5
        5	    |Tomates	|2100.0	    |42
        6	    |Fresas	    |4100.0	    |3
        7	    |Helado	    |4500.0	    |41
        8	    |Galletas	|500.0	    |8
        9	    |Chocolates	|3500.0	    |80
        10	    |Jamon	    |15000.0	|10
    Tabla 1: Productos disponibles en la tienda.

    Para simular de una manera más realista la base de datos,
    es necesario construir 3 funciones que representen las operaciones de:
    AGREGAR, ACTUALIZAR y BORRAR los productos disponibles.
    Se debe implementar una función independiente por cada una de las acciones mencionadas.
    En este caso, para poder realizar las operaciones de ACTUALIZAR o BORRAR
    es necesario especificar todos los atributos del producto.

    Adicionalmente, Pepe está interesado en analizar los datos de
    los productos disponibles y conocer: el nombre del producto con
    el precio mayor; el nombre del producto con el precio menor;
    el promedio de precios de todos los productos y el valor total
    del inventario a la fecha. Este último se obtiene multiplicando
    el precio de cada producto por el inventario disponible y luego sumando
    todos los resultados. Por ejemplo, al calcular estos 4 valores
    para los datos disponibles en la Tabla 1 obtendríamos :

        Producto precio mayor: Jamon
        Producto precio menor: Galletas
        Promedio de precios: 4900.0
        Valor del inventario: 101410.0

"""

__autor__ = "David Vargas Monroy"
__version__ = 0.1

baseDatos = {
    "codigo" : [1,2,3,4,5,6,7,8,9,10],
    "nombre" : ['Manzanas', 'Limones', 'Peras', 'Arandanos', 'Tomates',
                'Fresas', 'Helado', 'Galletas', 'Chocolates', 'Jamon'],
    "precio" : [5000.0, 2300.0, 2700.0, 9300.0, 2100.0, 4100.0, 4500.0, 500.0, 3500.0, 15000.0],
    "inventario" : [25, 15, 33, 5, 42, 3, 41, 8, 80, 10]
}

def operacionArtimetica():
    # Saber el producto de mayor precio
    maxPrice = max(baseDatos["precio"])
    posicionProducto = [i for i, j in enumerate(baseDatos["precio"]) if j == maxPrice]
    posicionProductoMax = int(posicionProducto[0])
    productoMayorPrecio = baseDatos["nombre"][posicionProductoMax]
    
    # saber el producto de menor precio
    minPrice = min(baseDatos["precio"])
    posicionProducto = [i for i, j in enumerate(baseDatos["precio"]) if j == minPrice]
    posicionProductoMin = int(posicionProducto[0])
    productoMenorPrecio = baseDatos["nombre"][posicionProductoMin]

    # Conocer el promedio de los precios
    sumatoriaPrecios = 0
    for i in baseDatos.get("precio"):
        sumatoriaPrecios += i
    promedioPrecios = sumatoriaPrecios / len(baseDatos.get("precio"))

    # Conocer el valor del inventario
    totalProducto = 0
    valorInventario = 0
    for i in range(len(baseDatos.get("codigo"))):
        totalProducto = baseDatos["precio"][i-1] * baseDatos["inventario"][i-1]
        valorInventario += totalProducto

    print(productoMayorPrecio,productoMenorPrecio, round(promedioPrecios,1), round(valorInventario,1))

def BORRAR():
    codigo, nombre, precio, inventario = input().split()
    codigo = int(codigo)
    nombre = str(nombre)
    precio = float(precio)
    inventario = int(inventario)
    if codigo in baseDatos.get("codigo") and nombre in baseDatos.get("nombre") and precio in baseDatos.get("precio") and inventario in baseDatos.get("inventario"):
        baseDatos["codigo"].pop(codigo-1)
        baseDatos["nombre"].pop(codigo-1)
        baseDatos["precio"].pop(codigo-1)
        baseDatos["inventario"].pop(codigo-1)
        operacionArtimetica()
    else:
        print('ERROR')

def AGREGAR():
    codigo, nombre, precio, inventario = input().split()
    codigo = int(codigo)
    nombre = str(nombre)
    precio = float(precio)
    inventario = int(inventario)
    if codigo in baseDatos["codigo"]:
        print('ERROR')
    else:
        baseDatos["codigo"].append(codigo)
        baseDatos["nombre"].append(nombre)
        baseDatos["precio"].append(precio)
        baseDatos["inventario"].append(inventario)
        operacionArtimetica()

def ACTUALIZAR():
    codigo, nombre, precio, inventario = input().split()
    codigo = int(codigo)
    nombre = str(nombre)
    precio = float(precio)
    inventario = int(inventario)
    if codigo in baseDatos.get("codigo"):
        baseDatos["codigo"][codigo-1] = codigo
        baseDatos["nombre"][codigo-1] = nombre
        baseDatos["precio"][codigo-1] = precio
        baseDatos["inventario"][codigo-1] = inventario
        operacionArtimetica()
    else:
        print('ERROR')

accionRealizar = str(input())
accionRealizar = accionRealizar + '()'
exec(accionRealizar)
