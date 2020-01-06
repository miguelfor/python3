nombre_archivo = "Glosario.txt"
archivo = open(nombre_archivo,"r")

texto = archivo.read()
archivo.close()
lineas = texto.splitlines()
terminos = texto.split(":")
diccionario={}
for linea in lineas:
    termino = linea.split(":")
    diccionario[termino[0]]=termino[1]

buscar = input("Indique el termino a buscar en el diccionario: ")
encontrado = diccionario.get(buscar)
if encontrado:
    print(buscar+":"+" "+encontrado)
else:
    print("Termino no existe en el glosario")
    ingresar_termino = input("Desea ingresar este termino(s/n):")
    if (ingresar_termino=='s'):
        archivo = open(nombre_archivo,"a")
        nuevo_termino = input("Indique la descripción del termino "+buscar+":")
        archivo.write("\n"+buscar+":"+nuevo_termino)
        archivo.close()