def calcular_media_100_numeros():
  """
  Permite ingresar 100 números enteros y calcula la media de esos valores.
  """
  numeros = []
  for i in range(100):
    while True:
      try:
        numero = int(input(f"Ingrese el número {i+1}: "))
        numeros.append(numero)
        break  
      except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")

  suma = sum(numeros)
  media = suma / len(numeros)

  print(f"La media de los 100 números es: {media}")

calcular_media_100_numeros()