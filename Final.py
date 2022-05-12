import dev1
import json
import random

EARTH_RADIUS = 6371

#Abre o arquivo e transforma em um dicionario

with open('paises.json', 'r') as arq_json:
    texto = arq_json.read()

dadoscerto =  json.loads(texto)

#Usa a função normaliza para botar o continente como valor

dadosnormalizados = dev1.normaliza(dadoscerto)




#sorteando pais
pais = dev1.sorteia_pais(dadosnormalizados)
print(pais)
