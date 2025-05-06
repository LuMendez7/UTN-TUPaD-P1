def sumar_numeros():
    """
    Pide al usuario números enteros, los sume secuencialmente y que el programa se detenga al ingresar 0.
    Muestra el total acumulado al final.
    """
    total = 0
    
    while True:
        numero = int(input("Ingrese un número entero (0 para terminar): "))
        
        if numero == 0:
            break  
        
        total += numero
    
    print("El total acumulado es:", total)

sumar_numeros()