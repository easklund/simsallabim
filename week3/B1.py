#commitment scheme
import random
import hashlib

def commitment(v, k): #v is a one bit value
     #k = random.getrandbits(nbrOfRandBits)
     x = hashSha1(v, k) #how to hash with to input
     return x

# we want to hash with two input parameters: the value and some randomness

def check(x, v, k):
    x2 = hashSha1(v, k)
    print(x2)
    if x == x2 :
        return "true"
    else :
        return "false"


def hashSha1(bytein, randomIn):
    sha1 = hashlib.sha1()
    sha1.update(bytein)
    sha1.update(randomIn)
    return sha1.digest()


def simulation(V, nbrOfSimulations):
    pass
#v = b'\0'
#k = b'\x00\x00\x0bQ'

print(commitment(b'\0', b'\x00\x00\x0bQ'))

print(check(commitment(b'\0', b'\x00\x00\x0bQ'), b'\1', b'\x00\x00\x0bQ'))
