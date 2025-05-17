import math

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    Args:
        radio: El radio del círculo.

    Returns:
        El área del círculo.
    """
    return math.pi * radio**2

def calcular_perimetro_circulo(radio):
    """
    Calcula el perímetro (o circunferencia) de un círculo dado su radio.

    Args:
        radio: El radio del círculo.

    Returns:
        El perímetro del círculo.
    """
    return 2 * math.pi * radio

# Solicitar el radio al usuario
while True:
    try:
        radio = float(input("Ingrese el radio del círculo: "))
        if radio > 0:
            break
        else:
            print("El radio debe ser mayor que cero.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Calcular el área y el perímetro
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

# Mostrar los resultados
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")