#commitment scheme
import random
import hashlib
from bitstring import *

def commitment(v): #v is a one bit value
     k = random.getrandbits(16)
     k = k.bytes
     x = hashSha1(v, k) #how to hash with to input
     return x

# we want to hash with two input parameters: the value and some randomness

def check(x, v, k):
    x2 = hashSha1(v, k)
    print(x2)
    if x == x2 :
        return True
    else :
        return False


def hashSha1(bytein, randomIn):
    sha1 = hashlib.sha1()
    sha1.update(bytein)
    sha1.update(randomIn)
    return sha1.digest()


def simulation(nbrOfSimulations):
    sumOfBreak = 0
    for i in range(nbrOfSimulations):
        com = commitment(b'\0')#, b'\x00\x00\x0bQ')
        if not(check(com, b'\1', b'\x00\x00\x0bQ')):
            sumOfBreak += 1

    return (sumOfBreak / nbrOfSimulations) * 100


#v = b'\0'
#k = b'\x00\x00\x0bQ'

#print(commitment(b'\0', b'\x00\x00\x0bQ'))

#print(check(commitment(b'\0', b'\x00\x00\x0bQ'), b'\1', b'\x00\x00\x0bQ'))

print(simulation(1000), "%")
