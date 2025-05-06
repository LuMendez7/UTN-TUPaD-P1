def contar_digitos(numero):
    """
    Cuenta la cantidad de dígitos de un número entero.

    Args:
        numero: El número entero a analizar.

    Returns:
        La cantidad de dígitos del número.
    """
    if numero == 0:
        return 1  # Caso especial para el cero

    if numero < 0:
        numero = abs(numero)  # Manejar números negativos

    count = 0
    while numero > 0:
        numero //= 10  # División entera para quitar el último dígito
        count += 1

    return count


numero = int(input("Ingrese un número entero: "))

cantidad_digitos = contar_digitos(numero)

print("El número", numero, "tiene", cantidad_digitos, "dígitos.")