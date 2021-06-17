"""
Enunciado

Reto 3: Selección de Vivienda:


    Catalina es una habitante y ama de casa en Boston Mass.
    Ella junto con su esposo deciden comprar un nuevo inmueble en el
    mismo lugar donde llevan viviendo por más de 5 años, así que deciden
    ir a una compañía que los oriente acerca de qué inmueble pueden comprar.
    Catalina manifiesta que para comprar la vivienda esta debe
    cumplir con las siguientes características:

        Que tenga 3 o más baños.
        Que tenga 4 o más habitaciones.
        Que el tiempo promedio en llegar al trabajo sea menos de 35 minutos.
        Que tenga 4 o más parques verdes alrededor.

    Usted hace parte del equipo de desarrollo encargado en la selección
    de las viviendas que cumplen con las condiciones del cliente,
    así que debe construir el software que procesará los datos de
    las bases de datos registradas en el sistema.Su misión es crear
    un programa en Python que permita mostrarle al cliente la lista de
    las casas que cumplen con sus requerimientos y por supuesto el valor
    de las mismas para su consideración.

"""

__autor__ = "David Vargas Monroy"
__version__ = 0.1

#Declaracion de variables
casasMostradas = 0

#Entrada para saber la cantidad de datos en la base de datos a digitar
cantidadDatos = int(input())

#Se le pedira volver a ingresar nuevos datos dependiendo de la entrada anterior
for i in range(cantidadDatos):
    #Entrada de datos en split mode
    cantidadBanos, cantidadHabitaciones, tiempoTrabajo, parquesCercanos, valorCasa = input().split()

    #Transformacion de str a int
    cantidadBanos = int(cantidadBanos)
    cantidadHabitaciones = int(cantidadHabitaciones)
    tiempoTrabajo = int(tiempoTrabajo)
    parquesCercanos = int(parquesCercanos)
    valorCasa = int(valorCasa)

    #Condicional para comprabar si se cumplen los requisitos de la sra
    if (cantidadBanos >= 3 and cantidadHabitaciones >= 4 and tiempoTrabajo < 35 and parquesCercanos >= 4):
        casasMostradas += 1
        print(valorCasa)

#Si no hay ninguna casa que cumpla la condicion se dira que no hay disponibles
if (casasMostradas == 0):
    print('NO DISPONIBLE')