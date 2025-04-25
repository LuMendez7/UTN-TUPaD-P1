import statistics

def determinar_sesgo(lista):
    """Determina si hay sesgo en una distribución de datos, comparando la media, mediana y moda.

    Args:
    lista: Una lista de números.

    Returns:
    Una cadena de texto indicando si hay sesgo positivo, negativo o ninguno."""

    try:
        media = statistics.mean(lista)
        mediana = statistics.median(lista)
        moda = statistics.mode(lista) if len(set(lista)) > 1 else None

        if moda is None:
            return "No hay moda definida (todos los valores son iguales)."
        elif media > mediana > moda:
            return "Sesgo positivo"
        elif media < mediana < moda:
            return "Sesgo negativo"
        else:
            return "No hay sesgo o el sesgo es mínimo"
    except statistics.StatisticsError:
        return "No hay moda definida (todos los valores son iguales)."

# Ejemplo de uso
lista_numeros = [1, 2, 2, 3, 3, 3, 4, 4, 5]
resultado = determinar_sesgo(lista_numeros)
print(resultado)

lista_numeros_sesgo_negativo = [1, 1, 2, 2, 3, 3, 4, 5, 5, 5, 5, 5]
resultado = determinar_sesgo(lista_numeros_sesgo_negativo)
print(resultado)

lista_numeros_no_sesgo = [1, 2, 3, 4, 5]
resultado = determinar_sesgo(lista_numeros_no_sesgo)
print(resultado)