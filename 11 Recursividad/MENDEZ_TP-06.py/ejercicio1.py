#Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario.


num = int(input("Ingrese un numero positivo: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n

print(factorial(num))

print(f"El factorial del numero ingresado es : {factorial(num)}")