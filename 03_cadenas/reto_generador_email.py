#Reto: Generador de emails.

#Información a tomar en cuenta
nombre_usuario = "Andres Fernandez Gomez"
nombre_empresa = "Ubisoft Montreal"
extension_dominio = ".com.co"

#Normalizacion de la información
nombre_usuario_normalizado = nombre_usuario.lower().replace(" ", ".")
nombre_empresa_normalizado = nombre_empresa.lower().replace(" ", "")

#Organizacion de la información para el email
email_generado = f"{nombre_usuario_normalizado}@{nombre_empresa_normalizado}{extension_dominio}"

#Mensaje en pantalla

print("======= Generador De Email =======")
print(f"Nombre del usuario: {nombre_usuario}")
print(f"Nombre del empresa: {nombre_empresa}")
print(f"Extension del dominio: {extension_dominio}")
print(f"\nEmail generado: {email_generado}")
print("="*35)