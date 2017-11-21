

def stripNetFile():
    lista = fromFileToList('DCnet.txt')
    size = len(lista)
    if size == 6:
        SA = lista[0]
        SA = SA[4]+SA[5]+SA[6]+SA[7]

        SB = lista[1]
        SB = SB[4]+SB[5]+SB[6]+SB[7]

        DA = lista[2]
        DA = DA[4]+DA[5]+DA[6]+DA[7]

        DB = lista[3]
        DB = DB[4]+DB[5]+DB[6]+DB[7]

        M = lista[4]
        M = M[3]+M[4]+M[5]+M[6]

        b = lista[5]
        b = b[3]

    else:
        print("Filen har fel antal rader")

    return SA, SB, DA, DB, M, b


def fromFileToList(filename):
    file = open(filename, 'r')
    Listan = file.readlines()
    for index in range(0,len(Listan)):
        Listan[index] =  Listan[index].replace('\n','')
    return Listan


print(stripNetFile())
