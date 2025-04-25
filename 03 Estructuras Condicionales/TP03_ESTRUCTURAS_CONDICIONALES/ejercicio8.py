name = input("Ingresa tu nombre: ")
numero = int(input("Presiona 1 si lo quieres en mayúscula, presiona 2 si lo quieres en miníscula o presiona 3 si solo quiere la primera letra en mayúscula: "))

if numero == 1:
    print(name.upper())
elif numero == 2:
    print(name.lower())
elif numero ==3:
    print(name.title())