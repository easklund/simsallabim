#commitment scheme
import random

def commitment(v, nbrOfRandBits): #v is a one bit value
     k = random.getrandbits(nbrOfRandBits)
     x = hashSha1(v) #how to hash with to inputs




# we want to hash with two input parameters: the value and some randomness

def hashSha1(bytein):
    sha1 = hashlib.sha1()
    sha1.update(bytein)
    return sha1.digest()
