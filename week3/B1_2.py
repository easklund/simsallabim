#commitment scheme,

import random
import hashlib

def commitment(v, k, trunSize): #v is a one bit value
     x = hashSha1(v, k) #how to hash with to input
     trun = truncateHash(x, trunSize)
     return trun

def hashSha1(bytein, randomIn):
    sha1 = hashlib.sha1()
    sha1.update(bytein)
    sha1.update(randomIn)
    return sha1.digest()

def generateK():
    k = random.randrange(0, 2**16)
    k = intToByte(k)
    return k

def intToByte(integer):
    Bytes = integer.to_bytes(2, byteorder='big')
    return Bytes

def byteToInt(i):
    return int.from_bytes(i, byteorder='big')

def checkBinding(x, invertedVote, trunSize):
    for i in range(2**16):
        i = intToByte(i)
        newX = commitment(invertedVote, i, trunSize)
        if newX == x :
            return True
    return False

def truncateHash(hashen, size):
    hashen = byteToInt(hashen)
    cutHash = hashen % (2**size)
    return cutHash


def binding_property(size, trunSize):
    san = 0
    for j in range(size):
        myX = commitment(b'\0',generateK(), trunSize)
        if checkBinding(myX, b'\1', trunSize):
            san += 1
    return (san/size) * 100

# print("5: ", binding_property(100, 5))
# print("10: ", binding_property(100, 10))
# print("12: ", binding_property(100, 12))
# print("14: ", binding_property(100, 14))
# print("16: ", binding_property(100, 16))
# print("18: ", binding_property(100, 18))
# print("20: ", binding_property(100, 20))
# print("25: ", binding_property(100, 25))



def checkConcealing(x, vote, trunSize):
    summa = 0
    for i in range(2**16):
        i = intToByte(i)
        newX = commitment(vote, i, trunSize)
        if newX == x :
            summa += 1
    return summa


def FindOutVote(x, turnSize):
    nbrOfOne = checkConcealing(x, b'\1', turnSize)
    nbrOfZero = checkConcealing(x, b'\0', turnSize)
    if nbrOfOne > nbrOfZero :
        return 1
    else:
        return 0

def conceling_property(size, turnSize, MyVote):
    nbrOfVin = 0
    for i in range(size):
        k = generateK()
        commit = commitment(MyVote, k, turnSize)
        what = FindOutVote(commit, turnSize)
        if what == 1:
            opponentVote = b'\0'
        else:
            opponentVote = b'\1'
        if MyVote != opponentVote:
            nbrOfVin += 1
    return (nbrOfVin/size) *100

print("5: ", conceling_property(500, 5, b'\1'))
print("10: ", conceling_property(500, 10, b'\1'))
print("12: ", conceling_property(500, 12, b'\1'))
print("14: ", conceling_property(500, 14, b'\1'))
print("16: ", conceling_property(500, 16, b'\1'))
print("18: ", conceling_property(500, 18, b'\1'))
print("20: ", conceling_property(500, 20, b'\1'))
print("25: ", conceling_property(500, 25, b'\1'))
