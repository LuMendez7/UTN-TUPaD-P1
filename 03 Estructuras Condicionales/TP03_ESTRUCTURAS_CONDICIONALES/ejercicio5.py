# Comprobar la longitud de una contraseña
contraseña = input("Introduce tu contraseña: ")
 
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contrseña de entre 8 y 14 caracteres.")