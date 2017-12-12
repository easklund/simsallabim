import hashlib
import binascii
import math

def mgf1(mgfSeed, maskLen):
    hLen = 2**32
    if maskLen > hLen :
        print("mask no long")
        return -1
    hLen = 20
    T = ''
    for i in range(math.ceil(maskLen / hLen)):
        c = I2OSP(i, 4)
        h = hashSha1hex(mgfSeed + c)
        T = T + h
    return T[:maskLen*2]

def OAEP_encode(M, seed):
    M = hexToByte(M)
    seed = hexToByte(seed)
    hLen = 20
    k = 128 #128 bytes
    L = hexToByte('')
    lHash = hashSha1(L) #Let lHash = Hash(L), an octet string of length hLen (see
              #the note below).
    lPS = k - len(M) - 2*hLen - 2
    PS = ''
    if lPS != 0:
        for i in range(lPS):
            PS = PS + '00'
    PS = hexToByte(PS.strip())
    DB =   lHash + PS + I2OSP(1, 1) + M # step c
    dbMask = mgf1(seed, k - hLen - 1)
    maskedDB = hexToInt(dbMask) ^ byteToInt(DB)
    maskedDB = intToByte(maskedDB)
    seedMask = mgf1(maskedDB, hLen)
    maskedSeed = byteToInt(seed) ^ hexToInt(seedMask)
    maskedSeed = intToByte(maskedSeed)
    temp = maskedSeed + maskedDB
    EM = I2OSP(0,1) + temp
    return byteToHex(EM)

# EM and output = hexadecimal strings
def OAEP_decode(EM):
    EM = hexToByte(EM)
    hLen = 20
    k = 128
    L = hexToByte('')
    lHash = hashSha1(L)
    Y = EM[:1]
    maskedSeed = EM[1:hLen+1]
    maskedDB = EM[hLen+1:]
    seedMask= mgf1(maskedDB, hLen)
    seed = byteToInt(maskedSeed) ^ hexToInt(seedMask)
    seed = intToByte(seed)
    dbMask = mgf1(seed, k - hLen - 1)
    DB = hexToInt(dbMask) ^ byteToInt(maskedDB)
    DB = intToByte(DB)
    lHashPrime = DB[:hLen]
    DBrest = DB[hLen:]
    i = 0
    while DBrest[i:i+1] == b'\x00':
        i += 1
    PS = DBrest[:i]
    M = DBrest[i+1:]
    return byteToHex(M)


def I2OSP(x, xLen):
    if x >= (256**xLen):
        #integer too lagre
        return None
    c = []
    for i in range(xLen):
        xi= x % 256
        x = x//256
        c.append(xi)
    return bytes(reversed(c))

def OS2IP(X):
    a = X[0]
    b = X[1]


def Hash(in1, in2):
    return hashSha1hex(in1, in2)

def hashSha1hex(bytein1):
    sha1 = hashlib.sha1()
    sha1.update(bytein1)
    return sha1.hexdigest()

def hexToByte(hexa):
    d = binascii.unhexlify(hexa)
    return d

def hexToInt(hexa):
    if hexa == '':
        return 0
    integer = int(hexa, 16)
    return integer

def intToByte(integer):
    size = (integer.bit_length() + 7 ) // 8
    if integer == 0:
        size = 1
    four_bytes = integer.to_bytes(size, byteorder='big')
    return four_bytes

def byteToHex(byte):
    hexa = binascii.hexlify(byte).decode('utf-8')
    return hexa

def intToHex(i):
    n = format(i,'08x')
    return n

def byteToInt(byte):
    i = int.from_bytes(byte, byteorder='big')
    return i

# def hexToInt(i):
#     return int(i, 16)

def truncate(T, size):
    cutT = T[:size]
    return cutT

def hashSha1(bytein):
    sha1 = hashlib.sha1()
    sha1.update(bytein)
    return sha1.digest()

#print(convertInt(15,4))

print('encode: ',OAEP_encode('0d4413b8823db607b594f3d7e86c4db168a4a17eb4fffd97bb71','e1683401d63da920ccced24b47c53cca7479f0ec'))
# print("hejhej: ")

print('decode: ' ,OAEP_decode('00b2f73d91326091417ed768c1bab03bdf7d32cb15d2345866989457444e4884695e81d6241ec8130c631733247498de28d4b5acfa50496127730f60b29cfad2157ca073fc373e40305f7eaeadcd30a7d591185f84876ca9e9d417f8441127dfb137ff4faf8437bd955e5dc03ed9094e6ea8429fa67e15173c42b2839afbd156'))
print('mgf1: ',mgf1(hexToByte('46dad84c7fa3460344bda67c31e8f948addb0649f13b7509'),24))
