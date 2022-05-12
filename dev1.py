import random
from math import *

def sorteia_pais(entrada):
    paises = []
    for i in entrada.keys():
        paises.append(i)
    aleatorio = random.choice(paises)
    return aleatorio

def haversine(r, la, ya, lb, yb):
    func1 = sin(radians((lb - la)/2))**2
    func2 = cos(radians(la)) * cos(radians(lb)) * (sin(radians((yb - ya)/2))**2)
    func3 = (func1 + func2)**(1/2)
    func4 = asin(func3)
    final = 2 * r * func4
    return final

def adiciona_em_ordem(p,d,lp):
    nl = []
    pd = [p, d]
    if lp == []:
        nl.append(pd)
    else:
        for i in range (len(lp)):
            if d > lp[i][1]:
                nl.append(lp[i])
            elif d <= lp[i][1]:
                nl.append(pd)
                nl.append(lp[i])
                d = (lp[-1][1] + 1)
        if pd not in nl:
            nl.append(pd)
        
    return nl

def esta_na_lista(pais,lista):
    for i in range (len(lista)):
        if lista[i][0] == pais:
            return True
    return False

def sorteia_letra(palavra,lista):
    m = palavra.lower()
    p = list(m)
    sem = ['.', ',', '-', ';', ' ']
    nl = []
    for i in p:
        if i not in lista and i not in sem:
            nl.append(i)
    print (nl)
    if nl == []:
        return ''
    final = random.choice(nl)
    return final


def normaliza(dic):
    final = {}
    for c, v in dic.items():
        for c2, v2 in v.items():
            final[c2] = v2
            final[c2]['continente'] = c

    return final