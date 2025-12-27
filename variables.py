"""
¿Qué es una variable?
Una variable es un espacio en memoria a la cual se le es asignado un valor.
Una variable está construida por una etiqueta "nombre" y un 'valor' el cual es el que asignamos.
Una variable, como su nombre lo dice, durante el desarrollo del algoritmo puede cambiar su valor.
"""
#Reglas para nombrar las variables
"""
No pueden empezar con números.
Para nombrar una variable podemos incluir letras, números, y guiones bajos
No se deben usar palabras reservadas del lenguaje 
Python es sensible a Mayúsculas y minúsculas
No se deben usar espacios
Se deben utilizar nombres descriptivos para las variables
Es recomendado usar el estilo snake_case
Si vamos a trabajar con booleanos es recomendado crear la variable como si fuera pregunta: usa_capa
en el caso de usar una constante vamos a implementar el uso de mayúsculas en la totalidad del nombre de la variable
"""
#Estilos de Nomenclatura
# snake_case para variables:
nombre_usuario = "Andres Fernandez"

#UPER_CASE para constantes:
MAX_INTENTOS = 25

# PascalCase para nombrar clases: UsuarioPremiun

#Programa: Información personal.
#Guardar los datos en variable
nombre = 'Ana'
edad = 22
pais = 'Mexico'
frase_favorita = 'Nunca dejes de aprender'
print('Nombre:', nombre)
print('Edad:', edad)
print('Pais:', pais)
print('Fase:', frase_favorita)