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

print("5: ", binding_property(100, 5))
print("10: ", binding_property(100, 10))
print("16: ", binding_property(100, 16))
print("20: ", binding_property(100, 20))
print("25: ", binding_property(100, 25))
