cripto = input("Indique el nombre de la moneda: ")
cant = float(input("Indique la cantidad de la moneda que posee: "))
dias = int(input("Indique la cantidad de días que negociará la moneda: "))
ganancia = float(input("Indique el porcentaje de ganancia esperada por día:"))
ganancia_total = cant*ganancia/100*dias
cant_total = cant + ganancia_total
print("La ganancia de",cripto,"durante los ",str(dias),"es",str(ganancia_total))
print("El monto total de",cripto,"a los",str(dias),"es de",str(cant_total))