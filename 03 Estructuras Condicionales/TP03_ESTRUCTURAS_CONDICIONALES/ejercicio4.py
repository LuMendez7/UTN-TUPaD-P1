edad = int(input("Introduce tu edad: "))

if edad >= 0 and edad <= 12:
    print("Eres un/a niña/o.")
elif edad >= 12 and edad < 18:
    print("Eres un/a adolescente.")
elif edad >= 18 and edad < 30:
    print("Eres un/a adulta/o joven.")
elif edad >= 30:
    print("Eres un/a adulta/o.")