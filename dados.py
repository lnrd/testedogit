lista = [1,2,3,4,5,6,7,8,9,10]

dic1 = {"Jack":"Elasticidade", "Fiona": "Fogo", "Finn":"Heroi"}
dic2 = {"Princesa Bubblegun":"Inteligencia", "Marceline": "Voo", "Jack":"Faz bons sanduiches"}

dic1.update(dic2) #atualiza o dicionario
print(dic1)


#Verifica se os dicionarios compartilham copias em comum

def mergeWithoutOverlap(dic1,dic2):
    novodict = dic1.copy()
    for key in dic2:
        if key in dic1:
            raise ValueError, "Os dois dicionarios compartilham chaves!"
        novodict[key] = dic2[key]
    return dic2

import copy
listOne = [{"nome":"Joao", "cidade":"parnaiba"},1, "tomate", 3.0]
listTwo = listOne[:]
listThree = copy.deepcopy(listOne)
listOne.append("culumin")
listOne[0]["cidade"] = "Buriti dos Lopes, Piaui"
print(listOne,listTwo, listThree)

import os

print(getcwd())
