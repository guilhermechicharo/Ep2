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

#lista de paises
nl = []
for c,v in dadosnormalizados.items():
    nl.append(c)


#sorteando pais
pais = dev1.sorteia_pais(dadosnormalizados)
i = 0



pais = dev1.sorteia_pais(dadosnormalizados)
i = 0

print(pais)

print('Um país foi escolhido, tente adivinhar!')
print('Você tem 20 tentativa(s)')

while i <= 20:
    tentativas = input('Qual seu palpite?')
    tentativa = tentativas.lower()
    if tentativa == pais:
        print ('Você acertou!')
        break
    if tentativa not in nl:
        print ('Pais desconhecido')
        print ('Você tem {0} tentativa(s)'.format(20-i))
    if tentativa in nl:
        if tentativa != pais:
            i += 1
            print('Você tem {0} tentativa(s)'.format(20-i))
            if i== 19:
                print('Você tem 0 tentativa(s)')
                print('>>> Você perdeu, o país era: {0}'.format(pais))
                break
            
