def suma_entre_rangos(numero):
  """
  Calcula la suma de todos los números entre 0 y un número entero positivo dado.

  Args:
    numero: Un entero positivo.

  Returns:
    La suma de todos los números entre 0 y el número dado.
  """

  if numero <= 0:
    return "El número debe ser positivo."

  suma = 0
  for i in range(numero + 1):
    suma += i
  return suma


while True:
  try:
    numero_usuario = int(input("Introduce un número entero positivo: "))
    if numero_usuario > 0:
      break  
    else:
      print("El número debe ser positivo.")
  except ValueError:
    print("Entrada inválida. Introduce un número entero.")


suma_total = suma_entre_rangos(numero_usuario)
print(f"La suma de los números entre 0 y {numero_usuario} es: {suma_total}")