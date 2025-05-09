compras = [["pan","leche"], ["arroz", "fideos", "salsa"], ["agua"]]
posicion_3_compras = compras [2]
posicion_3_compras.append("jugo")
print(compras)

compras [1][1] = "tallarines"
print(compras)

lista_primer_cliente = compras[0]
if "pan" in lista_primer_cliente:
    lista_primer_cliente.remove("pan")
print(lista_primer_cliente)
print(compras)