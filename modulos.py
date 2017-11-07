import os

#print(os.getcwd())
print(os.listdir(os.getcwd()))

lista = ["cachorro","gato","rato","pato","cobra","jegue","girafa","jaguar","baleia","suricato"]

#for item in lista:
#    os.mkdir(item)


dirnames = ["jubarte","azul","branca"]
filenames =["a.csv","b.csv","c.csv"]



top = os.getcwd()

os.walk(top, dirnames, filenames)
