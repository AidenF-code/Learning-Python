#Slicing es la tecnica para extraer un fragmento específico de una cadena sin modificar su contenido original
"""
texto[inicio : fin : paso]
texto = Python
Python
012345
print(texto[0:2]) = "Py"
print(texto[2:6]) = "thon"
"""
texto = "Python"
print(texto[0:2])
print(texto[2:6])
"""
Podemos utilizar índices negativos para contar desde el último hasta el primero:
	-6-5-4-3-2-1
	  P  y  t   h  o  n
	  print(texto[-1]) = "n"
	  
"""
print(texto[-1])
print(texto[-4:]) #Imprime desde el índice -4 hasta el final

#Invertir una cadena:
print(texto[::-1])

#El método .find() devuelve el indice de la primera aparición de la subcadena, si no encuentra la subcadena, devuelve -1

cadena = "Hola mundo, y bienvenidos a Pytho"
posicion =  cadena.find("mundo") # = 5
print(posicion)
posicion = cadena.find("hola") # = -1 porque no existe la cadena hola
print(posicion)