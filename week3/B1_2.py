#commitment scheme,

import random
import hashlib

def commitment(v, k): #v is a one bit value
     x = hashSha1(v, k) #how to hash with to input
     return x

def hashSha1(bytein, randomIn):
    sha1 = hashlib.sha1()
    sha1.update(bytein)
    sha1.update(randomIn)
    return sha1.digest()

def generateK():
    k = random.randint(0, (2^16) -1)
    k = intToByte(k)
    return k

def intToByte(integer):
    four_bytes = integer.to_bytes(2, byteorder='big', signed=True)
    return four_bytes

def checkBining(x, invertedVote):
    for i in range(2^16):
        i = intToByte(i)
        newX = commitment(invertedVote, i)
        if newX == x :
            return True
    return False

def trancateHash(hashen, size):
    cutHash = hashen % (size)


#print(commitment(b'\0',generateK()))
myX = commitment(b'\0',generateK())
print(myX)
print(checkBining(myX, b'\1'))
#print(generateK())
