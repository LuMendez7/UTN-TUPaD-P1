#Crear una función en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.

num = int(input("Ingrese un numero positivo: "))

def decimal_a_binario_bin(num):
    return bin(num)[2:]

print(decimal_a_binario_bin(num)) # Salida: 1010