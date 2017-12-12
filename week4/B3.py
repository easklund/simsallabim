import hashlib
import binascii
import math

def mgf1(mgfSeed, maskLen):
    hLen = 20
    if maskLen > 2**32 :
        print("mask to long")
        return -1
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
    k = 128
    L = hexToByte('')
    lHash = hashSha1(L)
    lPS = k - len(M) - 2*hLen - 2
    PS = ''
    if lPS != 0:
        for i in range(lPS):
            PS = PS + '00'
    PS = hexToByte(PS.strip())
    DB =   lHash + PS + I2OSP(1, 1) + M
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
        # integer too lagre
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

def byteToInt(byte):
    i = int.from_bytes(byte, byteorder='big')
    return i

def hashSha1(bytein):
    sha1 = hashlib.sha1()
    sha1.update(bytein)
    return sha1.digest()

print('encode: ',OAEP_encode('e79e5fb79ece9bd30699792ec38e927fa4c6e3c229503b3794','58b2ec96cf9cb1f9f4dab72fde2b8588381d7244'))
print('decode: ' ,OAEP_decode('00cbbfadbb0b9e0d96f094a3d6e552b4d82db3e4f4f9d3778a18b7aa067f90b2178406fa1e1bf77f03f86629dd5607d11b9961707736c2d16e7c668b367890bc6ef1745396404ba7832b1cdfb0388ef601947fc0aff1fd2dcd279dabdfcd92a7a13808d96ceea0a999a9947874a4741e7530bd99046c3368c6485702ea93ad95'))
print('mgf1: ',mgf1(hexToByte('601c47ea27444ce24417a1526c8c65ca8c3191f9877343c202'),25))
