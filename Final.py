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

#variaveis para dicas
cores = []
naopalavras = []
listacores = []

#inventario
inventario_dicas = []
inventario_dist = []

#Forma lista com cores da bandeira
coresbandeira = dadosnormalizados[pais]['bandeira']
for a in coresbandeira:
    if coresbandeira[a] > 0:
        cores.append(a)
        if 'outras' in cores:
            cores.remove('outras')

#forma lista com letras da capital
capital = dadosnormalizados[pais]['capital']
lista_letras = []
lista_letras_final = []


dicas = ['----------------------------------------','1. Cor da bandeira  - custa 4 tentativas','2. Letra da capital - custa 3 tentativas','3. Área             - custa 6 tentativas','4. População        - custa 5 tentativas','5. Continente       - custa 7 tentativas','0. Sem dica','----------------------------------------']




#Início do Jogo, Instruções
print('============================')
print('|                          |')
print(' Bem-vindo ao Insper Paises ')
print('|                          |')
print('==== Design de Software ===')

print('Comandos:')

print(' dica       - entra no mercado de dicas')
print(' desisto    - desiste da rodada' )
print(' inventario - exibe sua posição')



print('Um país foi escolhido, tente adivinhar!')
print('Você tem 20 tentativa(s)')


while i <= tmax:
    #Palpite
    tentativas = input('Qual seu palpite?')
    tentativa = tentativas.lower()
    if tentativa in nl:
        lista_paises.append(tentativa)
        if tentativa == pais:
            print ('Você acertou!')
            break 
            #Vitória!!
        else:
            #Calculo da distancia
            la = dadosnormalizados[pais]['geo']['latitude']
            ya = dadosnormalizados[pais]['geo']['longitude']
            lb = dadosnormalizados[tentativa]['geo']['latitude']
            yb = dadosnormalizados[tentativa]['geo']['longitude']
            d = (dev1.haversine(raio_terra,la,ya,lb,yb))
        
            #Adiciona em ordem        
            distancias = dev1.adiciona_em_ordem(tentativa,d,distancias)
            for f in range(len(distancias)):
                print('{0: .3f} km -> {1}'.format((distancias[f][1])/1000,distancias[f][0]))
                inventario_dist.append('{0: .3f} km -> {1}'.format((distancias[f][1])/1000,distancias[f][0]))
            i += 1
            
            print('Você tem {0} tentativa(s)'.format(tmax-i))
            if i== tmax:
                print('>>> Você perdeu, o país era: {0}'.format(pais))
                break 
                #Derrota :(
    if tentativa == 'dica':
        #Dicas
        print('Mercado de dicas')
        print(('\n').join(dicas))
        dc = input('Escolha sua opção [0|1|2|3|4|5]:')
        if dc == '1':
            #Dicas de cores
            tmax -= 4
            corescolhida = random.choice(cores)
            cores.remove(corescolhida)
            listacores.append(corescolhida)
            print(('\n').join(listacores))
            inventario_dicas.append(corescolhida)
        if dc == '2':
            #Dica capital
            tmax -= 3
            letra = dev1.sorteia_letra(capital,lista_letras)
            lista_letras_final.append(letra)
            print(('\n').join(lista_letras_final))
            inventario_dicas.append(letra)


    # desistencia
    if tentativa == 'desisto':
        desisto = input('Tem certeza que deseja desistir da rodada? [s/n]')
        if desisto == 's':
            print('>>> Essa tava moleza!! O senhor ficou nervoso, o pais era: {0}'.format(pais)) 
            jn = input('Jogar novamente?[s/n]')
            if jn =='s':
                continuar = True   

    if tentativa == 'inventario':
        print('Dicas:')
        print((inventario_dicas))
        print('Distancias:')
        print(inventario_dist)       
    if tentativa not in nl and tentativa != 'dica'and tentativa != 'desisto' and tentativa != 'inventario':
        print ('Pais desconhecido')
        print ('Você tem {0} tentativa(s)'.format(tmax-i))
    


    

    
            
    
