def segundos_a_horas(segundos):
    """
    Convierte segundos a horas.

    Args:
        segundos: La cantidad de segundos a convertir.

    Returns:
        La cantidad de horas equivalentes a los segundos proporcionados.
    """
    return segundos / 3600

# Solicitar al usuario la cantidad de segundos
segundos = float(input("Ingrese la cantidad de segundos: "))

# Calcular y mostrar las horas
horas = segundos_a_horas(segundos)
print(f"La cantidad de segundos {segundos} equivale a {horas} horas.")