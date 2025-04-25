def obtener_estacion(dia, mes):
  
  if mes == 12 or mes == 1 or mes == 2:
    return "Invierno"
  elif mes == 3 or mes == 4 or mes == 5:
    return "Primavera"
  elif mes == 6 or mes == 7 or mes == 8:
    return "Verano"
  elif mes == 9 or mes == 10 or mes == 11:
    return "Otoño"
  else:
    return "Mes inválido"

# Solicitar al usuario el día y el mes
while True:
  try:
    dia = int(input("Ingrese el día del mes: "))
    mes = int(input("Ingrese el mes (1-12): "))
    if 1 <= dia <= 31 and 1 <= mes <= 12:
      break
    else:
      print("Día o mes inválidos. Inténtelo nuevamente.")
  except ValueError:
    print("Ingrese números enteros válidos.")

# Obtener y mostrar la estación
estacion = obtener_estacion(dia, mes)
print(f"La estación para {mes}/{dia} es {estacion}")