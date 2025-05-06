def imprimir_pares_decreciente():
  """
  Imprime todos los números pares entre 0 y 100 en orden decreciente.
  """
  for i in range(100, -1, -2):
    if i % 2 == 0:  
      print(i)

imprimir_pares_decreciente()