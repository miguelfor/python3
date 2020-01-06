import requests

def esmoneda(cripto):
    return cripto in monedas

monedas=()
monedas_dict={}

data=requests.get("https://api.coinmarketcap.com/v2/ticker/").json()
for id in data["data"]:
    """Guarda criptomonedas en diccionario para despues comprobar si existe a partir del simbolo guarda name"""
    monedas_dict[data["data"][id]["symbol"]]=data["data"][id]["quotes"]["USD"]["price"]

monedas = monedas_dict.keys()

moneda=input("Indique el nombre de la moneda a obtener precio: ")
while not esmoneda(moneda):
        print("Moneda Invalida.")
        moneda=input("Ingrese el nombre de la moneda: ")
else:
    print("La moneda con symbol:,",moneda," tiene un precio de:",monedas_dict.get(moneda),
          "USD")
