#commitment scheme
import random
import hashlib

def commitment(v, nbrOfRandBits): #v is a one bit value
     k = random.getrandbits(nbrOfRandBits)
     x = hashSha1(v, k) #how to hash with to inputs
     return x

# we want to hash with two input parameters: the value and some randomness

def hashSha1(bytein, randomIn):
    sha1 = hashlib.sha1()
    sha1.update(bytein)
    sha1.update(randomIn)
    return sha1.digest()


def simulation(V, nbrOfSimulations):

b'\0'
b'\x00\x00\x0bQ'

print(commitment())
