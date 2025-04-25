#Clasificación de la magnitud de un terremoto

maginitud_terremoto = int(input("Introduce la magnitud del terremoto: "))

if maginitud_terremoto < 3:
    print("Muy leve.")
elif maginitud_terremoto >= 3 and maginitud_terremoto < 4:
    print("Leve.")
elif maginitud_terremoto >= 4 and maginitud_terremoto < 6:
    print("Moderado.")
elif maginitud_terremoto >= 6 and maginitud_terremoto < 7:
    print("Fuerte.")
elif maginitud_terremoto >= 7:
    print("Muy fuerte")