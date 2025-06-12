#Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin epacion ni tildes, y devuelva True si es un palíndromo o Flase si no lo es.

palabra = input("Ingrese una cadena de texto sin espacios ni tildes: ")

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])
   
print(es_palindromo(palabra)) 