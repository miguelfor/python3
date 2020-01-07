import requests
from datetime import datetime
_ENDPOINT = "https://api.binance.com"

ETHBTC=0
LTCBTC=0
BNBBTC=0
NEOBTC=0

miCode = "123"

def _url(api):
    return _ENDPOINT+api

def get_price(cripto):
    return requests.get(_url("/api/v3/ticker/price?symbol="+cripto))

nombre_archivo = "billetera.txt"
archivo = open(nombre_archivo,"r")
texto = archivo.read()
archivo.close()

def esmoneda(cripto):
    criptos = ["ETHBTC","LTCBTC","BNBBTC","NEOBTC"]
    if cripto in criptos:
        return True
    else:
        return False


def trasaccionPosible(moneda,cantidad):
    global ETHBTC,LTCBTC,BNBBTC,NEOBTC
    if (moneda == "ETHBTC"):
        if (ETHBTC >= int(cantidad)):
            return True
    if (moneda == "LTCBTC"):
        if (LTCBTC >= int(cantidad)):
            return True
    if (moneda == "BNBBTC"):
        if (BNBBTC >= int(cantidad)):
            return True
    if (moneda == "NEOBTC"):
        if (NEOBTC >= int(cantidad)):
            return True  
    else:
        return False


def saldo(moneda,cantidad):
    global ETHBTC,LTCBTC,BNBBTC,NEOBTC
    if (moneda == "ETHBTC"):
        ETHBTC = ETHBTC+cantidad 
    if (moneda == "LTCBTC"):
        LTCBTC = LTCBTC+cantidad 
    if (moneda == "BNBBTC"):
        BNBBTC = BNBBTC+cantidad 
    if (moneda == "NEOBTC"):
        NEOBTC = NEOBTC+cantidad        

def printSaldo(moneda):
    global ETHBTC,LTCBTC,BNBBTC,NEOBTC
    if (moneda == "ETHBTC"):
        return ETHBTC  
    if (moneda == "LTCBTC"):
        return ETHBTC  
    if (moneda == "BNBBTC"):
        return ETHBTC  
    if (moneda == "NEOBTC"):
        return ETHBTC    
                  


def menuFuncion():
    global ETHBTC,LTCBTC,BNBBTC,NEOBTC,miCode
    print("--------------------------------------")
    print("1. Recibir cantidad/(coins)")
    print("2. Transferir monto/(coins)") 
    print("3. Mostrar balance de una moneda") 
    print("4. Mostrar balance general") 
    print("5. Mostrar historico de transacciones") 
    print("6. Salir")
    print("--------------------------------------") 
    menu = (input("Indique opción menu: "))
   
    if menu == "1":        
        archivo = open(nombre_archivo,"a")
        moneda=""        
        while not esmoneda(moneda):
            moneda = input("Ingrese nombre de la moneda (ETHBTC,LTCBTC,BNBBTC,NEOBTC): ")
       
        cantidad=""        
        while not (cantidad.isdigit()):
            cantidad = input("Indique cantidad de monedas: ") 

        codigo=""        
        while not (codigo.isdigit()):
            codigo = input("Indique codigo: ")

        if(codigo != miCode):
            archivo.write("\n"+str(datetime.now())+";"+moneda+";Recibir;"+codigo+";"+cantidad)
            saldo(moneda,float(cantidad))   
            archivo.close() 
        else:
            print("***** Transacción rechazada. Codigo no puede ser el dueño de la cuenta *****")
        
        menuFuncion()  
    
    if menu == "2":         
        archivo = open(nombre_archivo,"a")
        moneda=""      
        while not esmoneda(moneda):
            moneda = input("Ingrese nombre de la moneda (ETHBTC,LTCBTC,BNBBTC,NEOBTC): ")
        
        cantidad=""        
        while not (cantidad.isdigit()):
            cantidad = input("Indique cantidad de monedas: ") 

        codigo=""        
        while not (codigo.isdigit()):
            codigo = input("Indique codigo: ")
            
        if(trasaccionPosible(moneda,cantidad)):
            archivo.write("\n"+str(datetime.now())+";"+moneda+";Transferir;"+codigo+";-"+cantidad) 
            saldo(moneda,(-(float(cantidad))))   
            archivo.close()  
            menuFuncion()
        else:
            print("***** Transacción rechazada. Fondos insuficientes. *****")
            menuFuncion()
    
    if menu == "3": 
        moneda=""        
        while not esmoneda(moneda):
            moneda = input("Ingrese nombre de la moneda (ETHBTC,LTCBTC,BNBBTC,NEOBTC): ")
        
        print(moneda+" :"+str(printSaldo(moneda)))
        data = get_price(moneda).json()
        print("El precio de",moneda,"es",data["price"]) 
        print("Total en USD: "+str(printSaldo(moneda)*float(data["price"])))
        menuFuncion()
    
    if menu == "4":
        data = get_price("ETHBTC").json()
        print("ETHBTC: "+ str(ETHBTC))
        print("El precio unidad es de",data["price"]+" Total: "+str(float(data["price"])*ETHBTC))
        data1 = get_price("LTCBTC").json()
        print("LTCBTC: "+ str(LTCBTC))
        print("El precio unidad es de",data1["price"]+" Total: "+str(float(data1["price"])*LTCBTC))
        data2 = get_price("BNBBTC").json()
        print("BNBBTC: "+ str(BNBBTC))
        print("El precio unidad es de",data2["price"]+" Total: "+str(float(data2["price"])*BNBBTC))
        data3 = get_price("NEOBTC").json()
        print("NEOBTC: "+ str(NEOBTC))
        print("El precio unidad es de",data3["price"]+" Total: "+str(float(data3["price"])*NEOBTC))
        total= (float(data3["price"])*NEOBTC)+(float(data2["price"])*BNBBTC)+(float(data1["price"])*LTCBTC)+(float(data["price"])*ETHBTC)
        print("Total billetera en USD: "+str(total))
        menuFuncion()
    
    if menu == "5":
        archivo = open(nombre_archivo,"r")
        texto = archivo.read()
        archivo.close()
        lineas = texto.splitlines() 
        print ("Fecha;moneda;tipo de operación;código del usuario, cantidad")
        for linea in lineas:
           print (linea)
    
        menuFuncion()
    
    if menu == "6":
        print("Chao Sr python...")
        exit()
    else:
        print("Opcion no valida, intente de nuevo.")
        menuFuncion()

menuFuncion()