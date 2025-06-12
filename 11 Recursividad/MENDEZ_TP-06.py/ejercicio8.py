#Escribí una función recursiva llamada contar_digito(numero digital) que reciba un número entero positivo (numero) y un digito (entre 0 y 9), y devuelva cuántas veces aparece ese digito dentro del número.

numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese un digito entre 0 y 9: "))

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    if numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

print("Ese digito aparece", contar_digito(numero, digito), "veces dentro del número ingresado.")