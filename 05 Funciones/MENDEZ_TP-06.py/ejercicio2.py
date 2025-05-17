def saludar_usuario(nombre):
  """
  Esta función recibe un nombre como parámetro y devuelve un saludo personalizado.
  """
  return "Hola " + nombre + "!"

# Solicitar el nombre al usuario
nombre = input("Por favor, ingresa tu nombre: ")

# Llamar a la función y mostrar el resultado
saludo = saludar_usuario(nombre)
print(saludo)