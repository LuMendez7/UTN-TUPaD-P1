def calcular_promedio(a, b, c):
    """
    Calcula el promedio de tres números.

    Args:
        a: El primer número.
        b: El segundo número.
        c: El tercer número.

    Returns:
        El promedio de los tres números.
    """
    return (a + b + c) / 3

# Solicitar los números al usuario
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
numero3 = float(input("Ingresa el tercer número: "))

# Calcular el promedio
promedio = calcular_promedio(numero1, numero2, numero3)

# Mostrar el resultado
print(f"El promedio de {numero1}, {numero2}, y {numero3} es: {promedio}")