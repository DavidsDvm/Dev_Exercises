"""
Enunciado
Reto 1: Impuestos sobre el salario

Un empleado desea conocer a cuánto dinero equivalen los descuentos
al pagar los impuestos exigidos por la ley en relación con los pagos
que la compañía para la que trabaja le realiza mensualmente.
Se ha firmado un contrato que le permite trabajar 38 horas semanales.
Con el propósito de verificar el valor total de los descuentos decide
construir un programa en Python que le permita verificar el valor de su
salario antes y después de realizar los descuentos para el pago de los impuestos.
Después de consultar sobre la normatividad y revisar con detalle su contrato
laboral nota que debe tener en cuenta los siguientes aspectos:

    El valor de una hora de trabajo normal se obtiene dividiendo el salario base sobre 170.
    Este valor corresponde a la jornada laboral establecida en el contrato
    (38 horas a la semana y 4 semanas al mes).

    Las horas extras se liquidan con un recargo del 45% sobre el valor de una hora normal.
    Debido a buen desempeño de un empleado la empresa ocasionalmente otorga bonificaciones
    de 2.8% del salario base.

    El salario total antes de descuentos se calcula como la suma del salario base,
    más el valor de las horas extras, más las bonificaciones (si las hay).

    Se descontará 4.9% del salario total antes de descuentos para el plan obligatorio de salud.

    Se descontará 5% del salario total antes de descuentos para el aporte a pensión.

    Se descontará 3% del salario total antes de descuentos para caja de compensación.

Luego de considerar toda esta información, el empleado decide construir un programa
que permita a cualquier empleado de la empresa verificar si los pagos son correctos.
"""

__autor__ = "David Vargas Monroy"
__version__ = 0.1

# Entradas
salarioBase, horasExtra, bonificaciones = input().split()
salarioBase = float(salarioBase)
horasExtra = int(horasExtra)
bonificaciones = int(bonificaciones)

# Calcular los beneficios economicos
precioHora = salarioBase / 170
pagoHoraExtra = horasExtra * (precioHora + (precioHora*0.45))
pagoBonificacion = bonificaciones * (salarioBase*0.028)

# Calcular las perdidas por impuestos
impuestos = 0.049 + 0.05 + 0.03

# Calcular el salario total antes de impuestos:
salarioTotalAD = salarioBase + pagoHoraExtra + pagoBonificacion

#Calcular el salario total despues de impuestos:
salarioTotal = salarioTotalAD - (salarioTotalAD*impuestos)

# Imprimir totales y resultados finales: 
print(round(salarioTotal,1),round(salarioTotalAD,1))