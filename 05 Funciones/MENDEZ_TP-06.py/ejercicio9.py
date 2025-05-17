def celsius_a_fahrenheit(celsius):
    """
    Convierte una temperatura de Celsius a Fahrenheit.

    Args:
        celsius: La temperatura en grados Celsius.

    Returns:
        La temperatura equivalente en grados Fahrenheit.
    """
    return (celsius * 9/5) + 32

# Pedir al usuario la temperatura en Celsius
temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Convertir a Fahrenheit y mostrar el resultado
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius}°C es equivalente a {temperatura_fahrenheit}°F")