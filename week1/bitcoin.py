import hashlib
import binascii

def SPVnode():
    lista = fromFileToList('mercur.txt')
    listLength = len(lista)
    leaf = lista[0]
    for i in range(1,listLength):
        sibling = lista[i]
        c = sibling[0]
        if(c == 'R'):
            sibling = sibling.replace("R", "")
            leaf = hashSha1(hexToByte(leaf + sibling))
        else:
            sibling = sibling.replace("L", "")
            leaf = hashSha1(hexToByte(sibling + leaf))
    return leaf


def fromFileToList(filename):
    file = open(filename, 'r')
    Listan = file.readlines()
    for index in range(0,len(Listan)):
        Listan[index] =  Listan[index].replace('\n','')
    return Listan

def hashSha1(bytein):
    sha1 = hashlib.sha1()
    sha1.update(bytein)
    return(sha1.hexdigest())

def hexToByte(hexa):
    d = binascii.unhexlify(hexa)
    return d

def fullNode():
    lista = fromFileToList('fullNodes.txt')
    siblingList = []
    size = len(lista)
    node = 2 + int(lista[0])
    antal = int(lista[1])
    while size > 3:
        count = 2
        for i in range(2, size, 2):
            l1 = lista[i]
            if (i+1) < size:
                l2 = lista[(i+1)]
            else:
                l2 = l1
            if i == node:
                siblingList.append('R' + l2)
                node = count
            elif (i+1) == node:
                siblingList.append('L' + l1)
                node = count
            lista[count] = hashSha1(hexToByte(l1 + l2))
            count += 1
        size = count
    return siblingList[len(siblingList)-int(antal)] + lista[2]

print(fullNode())
print(SPVnode())
