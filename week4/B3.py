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

print('encode: ',OAEP_encode('c107782954829b34dc531c14b40e9ea482578f988b719497aa0687','1e652ec152d0bfcd65190ffc604c0933d0423381'))
# print("hejhej: ")

print('decode: ' ,OAEP_decode('0063b462be5e84d382c86eb6725f70e59cd12c0060f9d3778a18b7aa067f90b2178406fa1e1bf77f03f86629dd5607d11b9961707736c2d16e7c668b367890bc6ef1745396404ba7832b1cdfb0388ef601947fc0aff1fd2dcd279dabde9b10bfc51efc06d40d25f96bd0f4c5d88f32c7d33dbc20f8a528b77f0c16a7b4dcdd8f'))
print('mgf1',mgf1(hexToByte('9b4bdfb2c796f1c16d0c0772a5848b67457e87891dbc8214'),21))
