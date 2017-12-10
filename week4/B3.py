import hashlib
import binascii
import math

def mgf1(mgfSeed, maskLen):
    hLen = 2**32
    #If maskLen > 2^32 hLen, output "mask too long" and stop.
    if maskLen > hLen :
        print("mask no long")
        return -1
    #Let T be the empty octet string.
    T = ''
    #For counter from 0 to \ceil (maskLen / hLen) - 1, do the following:
    print('test: ', math.ceil(maskLen/ hLen))
    for i in range(math.ceil(maskLen/ hLen) - 1):
        c = I2OSP(i, 4)
        T = T + Hash(mgfSeed,c)
    print('T: ',T)
    #Output the leading maskLen octets of T as the octet string mask.
    return truncate(T, maskLen)

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
            PS = PS + '0'
    PS = hexToByte(PS.strip())
    DB =   lHash + PS + hexToByte('01')+ M # step c
    dbMask = mgf1(seed, k - hLen - 1)
    maskedDB = byteToInt(DB) ^ dbMask
    maskedDB = intToByte(maskedDB)
    seedMask = mgf1(maskedDB, hLen)
    maskedSeed = byteToInt(seed)^seedMask
    maskedSeed = intToByte(maskedSeed)
    EM = b'\00' + maskedSeed + maskedDB
    # output the encoded message EM; OAEP encode(M) = EM.

    return byteToHex(EM)

# EM and output = hexadecimal strings
def OAEP_decode(EM):
    hLen = 20
    k = 128
    L = hexToByte('')
    lHash = hashSha1(L)
    Y = EM[:1]
    print('EM: ',EM)
    print('EM-B: ', hexToByte(EM))
    maskedSeed = EM[1:hLen+1]
    maskedDB = EM[hLen+1:]
    seedMask= mgf1(maskedSeed, hLen)
    seed = hexToInt(maskedSeed) ^ seedMask
    seed = intToByte(seed)
    dbMask = mgf1(seed, k - hLen - 1)
    DB = hexToInt(maskedDB) ^ dbMask
    DB = intToByte(DB)
    lHashPrime = DB[:hLen]
    DBrest = DB[hLen:]
    i = 0
    while DBrest[i:i+1] == '0x00':
        i +=1
    print(DB)
    print('DB: ', intToByte(DBrest[i]), 'lHash: ', lHash, 'lHashPrime: ', lHashPrime, 'Y: ', Y)
    if DBrest[i] != '0x01' or lHash != lHashPrime or Y != '0':
        return 'decryption error'
    PS = DBrest[:i]
    M = DBrest[i+1:]
    return M


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
    hashSha1hex(hexToByte(in1),hexToByte(in2))

def hashSha1hex(bytein1, bytein2):
    sha1 = hashlib.sha1()
    sha1.update(bytein1)
    sha1.update(bytein2)
    print (sha1.hexdigest())

def hexToByte(hexa):
    d = binascii.unhexlify(hexa)
    return d

def hexToInt(hexa):
    if hexa == '':
        return 0
    integer = int(hexa, 16)
    return integer

def intToByte(integer):
    four_bytes = integer.to_bytes(128, byteorder='big')
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
    T = hexToInt(T)
    cutT = T % (2**size)
    return cutT

def hashSha1(bytein):
    sha1 = hashlib.sha1()
    sha1.update(bytein)
    return sha1.digest()

#print(convertInt(15,4))

#print(OAEP_encode('fd5507e917ecbe833878','1e652ec152d0bfcd65190ffc604c0933d0423381'))
print(OAEP_decode('0000255975c743f5f11ab5e450825d93b52a160aeef9d3778a18b7aa067f90b2178406fa1e1bf77f03f86629dd5607d11b9961707736c2d16e7c668b367890bc6ef1745396404ba7832b1cdfb0388ef601947fc0aff1fd2dcd279dabde9b10bfc51f40e13fb29ed5101dbcb044e6232e6371935c8347286db25c9ee20351ee82'))
