def final_es_vocal(cadena):
  """Comprueba si una cadena termina en vocal.
  Args:
    cadena: La cadena de texto a verificar.
  Returns:
    True si la cadena termina en vocal, False de lo contrario."""

  if not cadena:
    return False  # Si la cadena está vacía, no termina en vocal

  ultima_letra = cadena[-1].lower()
  vocales = "aeiou"

  return ultima_letra in vocales

# Solicitar al usuario una frase o palabra
frase = input("Ingrese una frase o palabra: ")

# Verificar si la frase termina en vocal
if final_es_vocal(frase):
  print("La frase termina en vocal.")
else:
  print("La frase no termina en vocal.")