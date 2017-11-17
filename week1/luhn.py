from convert import *

def luhnFindX(i):
    myList = list(reversed(i))
    size = len(myList)
    siffra = 0;
    summa = 0;
    for x in range(0, len(i)):
        nbr = myList[x]
        if nbr == 'X':
            if x%2 == 0:
                siffra = 1
            else:
                siffra = 2
        else:
            nbr = int(nbr)
            if x%2 == 0:
                summa += nbr
            else:
                nbr = nbr*2
                if nbr > 9:
                    summa += nbr % 10
                    summa += 1
                else:
                    summa += nbr
    rest = 10 - (summa%10)
    if rest == 10:
        return 0
    elif siffra == 1:
        return int(rest)
    else:
        if (rest % 2) == 0:
            return int(rest / 2)
        else:
            return int((10 + rest - 1) / 2)

def ListLuhn(cardNbrList):
    listLength = len(cardNbrList)
    stringOfX = ""
    for item in range(0,listLength):
        nbrX = luhnFindX(cardNbrList[item])
        string = str(nbrX)
        stringOfX = stringOfX + string

    return stringOfX

def luhn():
    print(ListLuhn(fromFileToList('Luhnfile.txt')))

def fromFileToList(filename):
    file = open(filename, 'r')
    Listan = file.readlines()
    for index in range(0,len(Listan)):
        Listan[index] =  Listan[index].replace('\n','')
    return Listan


luhn()
