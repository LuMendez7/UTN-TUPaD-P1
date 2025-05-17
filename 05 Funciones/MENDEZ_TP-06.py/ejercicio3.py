def informacion_personal(nombre, apellido, edad, residencia):
  """
  Imprime la información personal proporcionada.

  Args:
      nombre: El nombre de la persona.
      apellido: El apellido de la persona.
      edad: La edad de la persona.
      residencia: El lugar de residencia de la persona.
  """
  print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Pedir los datos al usuario
nombre_usuario = input("Ingrese su nombre: ")
apellido_usuario = input("Ingrese su apellido: ")
edad_usuario = int(input("Ingrese su edad: "))  # Convertir a entero
residencia_usuario = input("Ingrese su lugar de residencia: ")

# Llamar a la función con los datos ingresados
informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario)