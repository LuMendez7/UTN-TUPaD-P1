import random

def jugar_adivina_numero():
    """Juego de adivinar un número aleatorio entre 0 y 9.
    """
    numero_secreto = random.randint(0, 9)
    intentos = 0

    while True:
        intentos += 1
        
        # Solicitar al usuario que adivine
        adivina = input("Adivina el número (entre 0 y 9): ")
        
        # Verificar que la entrada sea un número válido
        try:
            adivina = int(adivina)
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
        
        # Comparar el número ingresado con el número secreto
        if adivina == numero_secreto:
            print(f"¡Correcto! Has adivinado el número en {intentos} intentos.")
            break  # Salir del bucle
        elif adivina < numero_secreto:
            print("Demasiado bajo.")
        else:
            print("Demasiado alto.")

# Llamar a la función para iniciar el juego
jugar_adivina_numero()