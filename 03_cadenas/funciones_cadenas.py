#Funcion len(), cuenta la cantidad de elementos en cadenas, listas entre otros
#Que cuenta la función len() ? letras, espacios, símbolos:
varios = "A B C +"
print("Al utilizar la función len() con la variable varios podemos validar que toma en cuenta los espacios, letras y símbolos")
print(len(varios))


#Funcion .upper(), permite convertir una cadena a letras mayúsculas:
mensaje = "bienvenidos al curso de pyton"
print(mensaje.upper())

#La función .lower(), permite convertir una cadena que esté con letras mayúsculas a minúsculas:
mensaje1 = "BITS"
print(mensaje1.lower())

"""
La función.replace permite buscar una cadena dentro de otra y sustituir su contenido permitiendo realizar limpiezas de texto, creación de plantillas
texto.replace ("viejo", "nuevo")
Se puede agregar un tercer parametro para indicar cuantas veces queremos que ocurra el cambio; sin embargo, por defecto viene para hacer los 
cambios en el total del texto
"""
mensaje2 = "Hola mundo, mundo"
nuevo_mensaje = mensaje2.replace("mundo", "Python")
print(mensaje2)
print(nuevo_mensaje)
print(mensaje2.replace("mundo","Dev",1))


#Inmutabilidad en cadenas, las cadenas no son mutables, es decir, no pueden ser cambiadas sin embargo si podemos utilizarlas 
#como lo vimos anteriormente para crear nuevas:
fruta = "Fresa"
"""
Forma incorrecta:
	fruta[4] = "s"
	Intentar modificar el índice directamente siempre nos dara error
"""
#Formas correctas:
#Concatenacion con símbolo +
plural =  fruta + "s"
print(plural)

#F-String
plural = f"{fruta}s"
print(plural)