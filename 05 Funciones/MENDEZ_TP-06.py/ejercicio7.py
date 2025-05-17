def operaciones_basicas(a, b):
    """
    Realiza las operaciones básicas (suma, resta, multiplicación, división)
    con dos números y devuelve los resultados en una tupla.
    """
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "División por cero"  # Manejo de división por cero

    return suma, resta, multiplicacion, division

# Ejemplo de uso
numero1 = 10
numero2 = 5

resultados = operaciones_basicas(numero1, numero2)

print(f"Para los números {numero1} y {numero2}:")
print(f"La suma es: {resultados[0]}")
print(f"La resta es: {resultados[1]}")
print(f"La multiplicación es: {resultados[2]}")
print(f"La división es: {resultados[3]}")