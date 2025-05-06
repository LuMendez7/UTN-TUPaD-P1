def sumar_entre_numeros(num1, num2):
    """
    Suma todos los números enteros comprendidos entre dos valores dados por el usuario,
    excluyendo esos dos valores.

    Args:
    num1: El primer número entero.
    num2: El segundo número entero.

    Returns:
    La suma de los números enteros entre num1 y num2, excluidos num1 y num2.
    """

    if num1 >= num2:
        print("El primer número debe ser menor que el segundo.")
        return None

    suma = 0
    for numero in range(num1 + 1, num2):
        suma += numero

    return suma

# Solicitar al usuario los dos números
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero (mayor que el primero): "))

# Calcular y mostrar la suma
resultado = sumar_entre_numeros(numero1, numero2)

if resultado is not None:
    print("La suma de los números enteros entre {} y {} es: {}".format(numero1, numero2, resultado))