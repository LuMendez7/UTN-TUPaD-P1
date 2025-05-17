def tabla_multiplicar(numero):
    """
    Imprime la tabla de multiplicar de un número dado.

    Args:
        numero: El número para el cual se imprimirá la tabla de multiplicar.
    """

    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Solicitar al usuario que ingrese un número
try:
    numero_usuario = int(input("Ingrese un número: "))
    # Llamar a la función tabla_multiplicar con el número ingresado por el usuario
    tabla_multiplicar(numero_usuario)
except ValueError:
    print("Error: Por favor, ingrese un número entero válido.")
