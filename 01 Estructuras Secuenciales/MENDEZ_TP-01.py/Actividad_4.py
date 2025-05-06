#Cálculo del área y perímetro de un circulo

radio = float(input("Ingrese el radio de un circulo: "))

pi = 3.1416
perimetro = 2 * radio * pi
area = radio * radio * pi

print("El área del circulo es", area, "y su perimetro es", perimetro)