def invertir_numero(numero):
  """Invierte el orden de los dígitos de un número.

  Args:
    numero: El número a invertir.

  Returns:
    El número con los dígitos invertidos.
  """
  numero_str = str(numero)
  numero_invertido_str = numero_str[::-1]
  numero_invertido = int(numero_invertido_str)
  return numero_invertido

while True:
  try:
    numero = int(input("Ingresa un número entero: "))
    break
  except ValueError:
    print("Entrada inválida. Ingresa un número entero.")

numero_invertido = invertir_numero(numero)

print(f"El número invertido es: {numero_invertido}")