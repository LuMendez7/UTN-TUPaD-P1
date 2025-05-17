def calcular_imc(peso, altura):
  """
  Calcula el índice de masa corporal (IMC).

  Args:
    peso: Peso en kilogramos.
    altura: Altura en metros.

  Returns:
    El IMC (índice de masa corporal).
  """
  return peso / (altura ** 2)

# Solicitar al usuario los datos
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

# Calcular el IMC
imc = calcular_imc(peso, altura)

# Mostrar el resultado con dos decimales
print("Su índice de masa corporal (IMC) es: {:.2f}".format(imc))