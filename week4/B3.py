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
        print('c: ', c)
        h = hashSha1hex(mgfSeed + c)
        T = T + h
    print('T: ',T)
    return T[:maskLen*2]

def OAEP_encode(M, seed):
    M = hexToByte(M)
    seed = hexToByte(seed)
    hLen = 20
    k = 128 #128 bytes
    L = hexToByte('')
    print('L: ', L)

    lHash = hashSha1(L) #Let lHash = Hash(L), an octet string of length hLen (see
    print('lHash: ', lHash)                #the note below).
    lPS = k - len(M) - 2*hLen - 2
    PS = ''
    if lPS != 0:
        for i in range(lPS):
            PS = PS + '0'
    PS = hexToByte(PS.strip())
    print('PS: ', PS)
    DB =   lHash + PS + hexToByte('01') + M # step c
    print('DB: ', DB)
    dbMask = mgf1(seed, k - hLen - 1)
    # dbMask = '23ead46446dce10b4dc50df81166e28eb42f780af86629dd5607d11b9961707736c2d16e7c668b367890bc6ef1745396404ba7832b1cdfb0388ef601947fc0aff1fd2dcd279dabde9b10bfc51f40e13fb29ed5101dbcb044e6232e6371935c8346d538b5b5890ebdd2d6fa'
    print('dbMask: ', dbMask)
    maskedDB = hexToInt(dbMask) ^ byteToInt(DB)
    maskedDB = intToByte(maskedDB)
    print('maskedDB: ', maskedDB)
    seedMask = mgf1(maskedDB, hLen)
    print('seedMask: ', seedMask)
    maskedSeed = byteToInt(seed) ^ hexToInt(seedMask)
    maskedSeed = intToByte(maskedSeed)
    print('maskedSeed: ', maskedSeed)
    EM = b'\00' + maskedSeed + maskedDB
    print('EM: ', byteToHex(EM))
    # output the encoded message EM; OAEP encode(M) = EM.

    return byteToHex(EM)

# EM and output = hexadecimal strings
def OAEP_decode(EM):
    EM = hexToByte(EM)
    print('EM: ', EM)
    hLen = 20
    k = 128
    L = hexToByte('')
    lHash = hashSha1(L)
    Y = EM[:1]
    # print('EM: ',EM)
    # print('EM-B: ', hexToByte(EM))
    maskedSeed = EM[1:hLen+1]
    #print('maskedSeed: ', maskedSeed)
    maskedDB = EM[hLen+1:]
    #print('maskedDB: ', maskedDB)
    seedMask= mgf1(maskedDB, hLen)
    #print('seedMask: ', seedMask)
    seed = byteToInt(maskedSeed) ^ hexToInt(seedMask)
    seed = intToByte(seed)
    #print('seed: ', seed)
    # seed = bytes(a ^ b for a, b in zip(maskedSeed, hexToByte(seedMask)))
    dbMask = mgf1(seed, k - hLen - 1)
    #dbMask = '23ead46446dce10b4dc50df81166e28eb42f780af86629dd5607d11b9961707736c2d16e7c668b367890bc6ef1745396404ba7832b1cdfb0388ef601947fc0aff1fd2dcd279dabde9b10bfc51f40e13fb29ed5101dbcb044e6232e6371935c8346d538b5b5890ebdd2d6fa'
    print('dbMask: ', dbMask)
    DB = hexToInt(dbMask) ^ byteToInt(maskedDB)
    DB = intToByte(DB)
    # DB = bytes(a ^ b for a, b in zip(hexToByte(dbMask), maskedDB))[hLen:]
    lHashPrime = DB[:hLen]
    DBrest = DB[hLen:]
    print('DB: ', DBrest)
    i = 0
    while DBrest[i:i+1] == b'\x00':
        i += 1
    #print('DB efter while: ', DBrest)
    # print('i: ', i)
    # print('DB: ', byteToHex(DBrest))
    # print('DBrest: ', intToHex(DBrest[i]))
    # print('lHash: ', byteToHex(lHash))
    # print('lHashPrime: ', byteToHex(lHashPrime))
    # print('Y: ', Y)
    # if DBrest[i] != '0x01' or lHash != lHashPrime or Y != '0':
    #     return 'decryption error'
    PS = DBrest[:i]
    M = DBrest[i+1:]
    print('M: ', M)
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
    hexa = intToHex(byteToInt(byte))
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

print(OAEP_encode('fd5507e917ecbe833878','1e652ec152d0bfcd65190ffc604c0933d0423381'))
# print("hejhej: ")
# print(OAEP_decode('0000255975c743f5f11ab5e450825d93b52a160aeef9d3778a18b7aa067f90b2178406fa1e1bf77f03f86629dd5607d11b9961707736c2d16e7c668b367890bc6ef1745396404ba7832b1cdfb0388ef601947fc0aff1fd2dcd279dabde9b10bfc51f40e13fb29ed5101dbcb044e6232e6371935c8347286db25c9ee20351ee82'))
