# ¿Qué es un String? Es una cadena de texto formada por un conjunto de caracteres que usualmente utilizamos para almacenar, nombres, direcciones, frases, mensajes etc.
#En Python podemos definir las cadenas o Strings mediante comillas sencillas o dobles:
#Comillas sencillas ''
nombre = 'Andres'

#Comillas dobles""
fruta = "Uva"

#Python permite el uso de ambas comillas con el fin de poder colocar comillas dentro de un texto, ej.
cita = 'El maestro dijo: "Estudien mucho" '
libro = "Lei el libro 'El Principito' ayer "
print ( "Ejemplo de uso de comillas en texto: ")
print (cita)
print (libro)

#Podemo usar el uso de comillas triples """ tanto para hacer comentarios como para asignarlos a una variable:
mensaje = """
Python es un gran lenguaje de programacion
que brinda una gran facilidad en su escritura y lectura
y es fuertemente usado en Machine Learning e Inteligencia Artificial
"""
menu = """
--------------------
Menu del dia

1. Arroz con pollo
2. Bandeja paisa
3. Churrasco ahumado

--------------------
"""
print(menu)
print (mensaje)