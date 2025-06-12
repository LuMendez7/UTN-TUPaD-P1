#Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestre la serie completa hasta la posición que el usuario especifique.

def fibonacci_recursivo(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

def mostrar_serie_fibonacci(n):
    
    if n <= 0:
        print("La serie de Fibonacci no es válida para posiciones menores o iguales a 0.")
        return
  
    print("Serie de Fibonacci hasta la posición", n, ":")
    for i in range(n + 1):
        print(fibonacci_recursivo(i), end=" ")
    print()

while True:
  try:
    position = int(input("Ingresa la posición hasta la cual mostrar la serie de Fibonacci: "))
    break
  except ValueError:
    print("Por favor, ingresa un número entero.")

mostrar_serie_fibonacci(position)