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
    k = random.randrange(0, 2**16)
    k = intToByte(k)
    return k

def intToByte(integer):
    Bytes = integer.to_bytes(2, byteorder='big')
    return Bytes

def byteToInt(i):
    return int.from_bytes(i, byteorder='big')

def checkBinding(x, invertedVote):
    print('x: ', x)
    for i in range(2**16-1):
        i = intToByte(i)
        newX = commitment(invertedVote, i)
        newX = truncateHash(newX, 16)
        #print('newX: ', newX)
        if newX == x :
            return True
    return False

def truncateHash(hashen, size):
    #print("hashen1: ", hashen)
    hashen = byteToInt(hashen)
    #print("hashen2: ", hashen)
    cutHash = hashen % (2**size)
    #print("hej: ", cutHash)
    return intToByte(cutHash)


#print(commitment(b'\0',generateK()))
myX = commitment(b'\0',generateK())
print("MyX: ", myX)
trun = truncateHash(myX, 17)
print('trun: ', trun)
print(checkBinding(trun, b'\1'))

#tran = truncateHash(myX, 10000000)
#print(tran)
#print(myX)
#print(checkBinding(myX, b'\1'))

#print(generateK())
