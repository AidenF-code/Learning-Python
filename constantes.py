"""
Python al ser un lenguaje dinámico, no existe un tipo específico para definir una constante de manera estricta, sin embargo,
podemos utilizar una convención para indicar que el valor de una variable no debe ser cambiado, esta convención es conocida
como UPPER_CASE.
"""
import math
from re import match

NOMBRE_CONSTANTE = "Soy una constante"
PI = 3.14
print("*** Constantes en Python ***")
print(NOMBRE_CONSTANTE)
print(PI)

# Se debe tener en cuenta que en Python ya existen constantes integradas en el lenguaje, por ejemplo el módulo match ya viene con la
#constante pi, y esta no está escrita en mayúscula:

print("Esta es una constante integrada:", math.pi)