
from Crypto.PublicKey import RSA
import random
import hashlib
#private = RSA.generate(1024, os.urandom)


def generate2kq(k, rand_range, n):
    TwoK = 2*k
    #vektor a
    a = [0 for i in range(TwoK)]
    for j in range(0, TwoK):
        a[j] = (random.randrange(rand_range)) % n

    c = [0 for i in range(TwoK)]
    for j in range(0, TwoK):
        c[j] = (random.randrange(rand_range)) % n

    d = [0 for i in range(TwoK)]
    for j in range(0, TwoK):
        d[j] = (random.randrange(rand_range)) % n

    r = [0 for i in range(TwoK)]
    for j in range(0, TwoK):
        r[j] = (random.randrange(rand_range)) % n

    return a, c, d, r
    #generera mod(n) a_i, c_i, d_i, r_i,  vektorer
    #this will result in a coin
    #assosiera cion med ett ID(Alice's)

def computeX(a, c):
    size = len(a)
    x = [0 for i in range(size)]
    for j in range(0, size) :
        x[j] = hashInt(a[j] + d[j]) #vet ej om det är så här man gör med dubbel input på hashen
    return x

def computeY(a,d, ID):
    size = len(a)
    y = [0 for i in range(size)]
    for j in range(0, size):
        temp = bool(a[j]) ^ bool(ID)
        y[j]=  hashInt(temp+d[j])
    return y

def computeB(x, y, r, n, e):
    size = len(x)
    b = [0 for i in range(size)]
    for j in range(0, size) :
        b[j] = (r[j]**e) * f(x[j], y[j])
    return b

def indexChoise(size):
    indexes = [0 for i in range(size/2)]
    for i in range(size):
        #välj en random int, modulo size
        index = random.randint(0,size) % n
        #kolla så att indexet inte valts tidigare

def banksChoise(b) :
    #banken väljer ut k av 2k
    size = len(b)
    indexes = indexChoise(size)
    r = [0 for i in range(size/2)]
    for i in range(size):
        r[i] = b[indexes[i]]
    return r

def computeBlindSign(bHalf, n, e):
    size = len(bHalf)
    blindSign = 1
    for i in range(size):
        temp = (bHalf[i] **(1/e)) % n
        blindSign = blindSign * temp
    return blindSign

def extractSign(bHalf, e):
    size = len(bHalf)
    sign = 1
    for i in range(size):
        temp = (f(x_i, y_i))**(1/e)  #här behöver jag ha koll på vilka xy som hör till vilket b
        sign = sign * temp
    return sign

#Makes a list with BClass ovjects to store which a, c, d and r that are conneced to B
 def storeB(a, c, d, r, B):
     lista = []
     size = len(a)
     for i in range(size):
         ob = Bclass()
         ob.setA(a[i])
         ob.setC(c[i])
         ob.setD(d[i])
         ob.setR(r[i])
         ob.setB(B[i])
         lista.append(ob)
     return lista

 #Returns a BClass object with B as its B
 def findB(l, B):
     size = len(l)
     for i in range(size):
         if l[i].getB() == B:
             return l[i]
     return 0




#hjälpfunktioner

def f(x_i, y_i):
    return x_i*y_i

def hashInt(integer):
    byte = intToByte(integer)
    h = hashSha1(byte)
    newInt = byteToInt(h)
    return newInt

def hashSha1(bytein):
    sha1 = hashlib.sha1()
    sha1.update(bytein)
    return(sha1.digest())

#int to four bytes
def intToByte(integer):
    four_bytes = integer.to_bytes(4, byteorder='big', signed=True)
    #print(four_bytes)
    return four_bytes

#byte to int
def byteToInt(byte):
    i = int.from_bytes(byte, byteorder='big', signed=True)
    #print(i)
    return i

n = 3
a, c, d, r =  generate2kq(4, 100, n)
print(computeB(computeX(a,c), computeY(a,d, 12345), r, n, 3))
