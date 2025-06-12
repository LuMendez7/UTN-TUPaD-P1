#Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la formula (a^m)^n = a^(m * n). Prueba esta función en un algoritmo general.

def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    if exponente == 1:
        return base
    if exponente % 2 == 0:
        temp = potencia_recursiva(base, exponente // 2)
        return temp * temp
    else:
        temp = potencia_recursiva(base, exponente // 2)
        return temp * temp * base

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = potencia_recursiva(base, exponente)
print("El resultado es:", resultado)