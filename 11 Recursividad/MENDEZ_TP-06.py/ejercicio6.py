#Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus digitos.

numero = int(input("Ingrese un numero positivo: "))

def suma_digitos(n):
    if n < 10: 
        return n
    else:
        return n % 10 + suma_digitos(n // 10)

suma = suma_digitos(numero)

print(f"La suma de los dígitos de {numero} es: {suma}")