import random
import hashlib
import numpy as np
import math


def b2(u, k, c, width):
    n = 0
    std = 0
    l = 3.66
    mean = 0
    summ = 0
    nbrArray = []

    nbrArray.append(microMint(u, k, c))
    x = nbrArray[0]

    n += 1
    nbrArray.append(microMint(u, k, c))

    mean = np.mean(nbrArray)
    std = np.std(nbrArray)

    x = mean - (l*(std/math.sqrt(n)))
    y = mean + (l*(std/math.sqrt(n)))
    while (y - x) >= (width) :
        n += 1
        nbrArray.append(microMint(u, k, c))

        mean = np.mean(nbrArray)
        std = np.std(nbrArray)

        x = mean - (l*(std/math.sqrt(n)))
        y = mean + (l*(std/math.sqrt(n)))

    print("mean: ", mean, "std: ", std, "x: ", x, "y: ", y)
    return mean, std, x, y


def microMint(u, k, c):
    binArray = [0 for x in range(2**u)]
    coins = 0
    tries = 0

    while coins < c:
        randomIndex = (random.randrange(0,2**(2*u)))
        hashIndex = hashInt(randomIndex) % (2**u)
        binArray[hashIndex] += 1
        tries += 1
        if binArray[hashIndex] == k :
            coins += 1;
    return tries

def hashInt(integer) :
    bytein = intToByte(integer)
    h = hashSha1(bytein)
    return byteToInt(h)

def hashSha1(bytein):
    sha1 = hashlib.sha1()
    sha1.update(bytein)
    return(sha1.digest())

def intToByte(integer):
    four_bytes = integer.to_bytes(8, byteorder='big', signed=True)
    return four_bytes

def byteToInt(byte):
    i = int.from_bytes(byte, byteorder='big', signed=True)
    return i

b2(19, 6, 1, 23834)
