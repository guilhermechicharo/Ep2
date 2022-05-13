import dev1
import json
import random

raio_terra = 6371

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
lista_paises = []
tmax = 20
distancias = []


print(pais)

print('Um país foi escolhido, tente adivinhar!')
print('Você tem 20 tentativa(s)')

while i <= tmax:
    tentativas = input('Qual seu palpite?')
    tentativa = tentativas.lower()
    if tentativa in nl:
        lista_paises.append(tentativa)
        if tentativa == pais:
            print ('Você acertou!')
            break
        else:
            la = dadosnormalizados[pais]['geo']['latitude']
            ya = dadosnormalizados[pais]['geo']['longitude']
            lb = dadosnormalizados[tentativa]['geo']['latitude']
            yb = dadosnormalizados[tentativa]['geo']['longitude']
            d = (dev1.haversine(raio_terra,la,ya,lb,yb))
        

            distancias = dev1.adiciona_em_ordem(tentativa,d,distancias)
            for f in range(len(distancias)):
                print('{0: .3f} km -> {1}'.format((distancias[f][1])/1000,distancias[f][0]))

            
            i += 1
            
            print('Você tem {0} tentativa(s)'.format(tmax-i))
            if i== tmax:
                print('>>> Você perdeu, o país era: {0}'.format(pais))
                break
    else:
        print ('Pais desconhecido')
        print ('Você tem {0} tentativa(s)'.format(tmax-i))

    
    
    
            
