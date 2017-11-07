#Operacoes de dicionarios

D1 = {}
D2 = {'spam':2, 'eggs':3 }

print(D2.keys())
print(D2.has_key('eggs'))

print(D2.values())


l1 = ["a","b","c","d"]
l2 = ["vaca","frango","tatu","foca"]
l3 = ["muge","pia","cava","nada"]
l3 = [1,2,3,4]

D4 = dict(zip(l1,l2))

D4["e"] = "cabrito"
print(D4)
