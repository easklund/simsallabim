import hashlib
import binascii

def mgf1(mgfSeed, maskLen):
    hLen = 2**32
    #If maskLen > 2^32 hLen, output "mask too long" and stop.
    if maskLen > hLen :
        print("mask no long")
        return -1
    #Let T be the empty octet string.
    T = ''
    #For counter from 0 to \ceil (maskLen / hLen) - 1, do the following:
    for i in range((maskLen // hLen) - 1):
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
    maskedDB = DB ^ dbMask
    seedMask = mgf1(maskedDB, hLen)
    maskedSeed = seed^seedMask
    EM = b'\00' + maskedSeed + maskedDB
    # output the encoded message EM; OAEP encode(M) = EM.
    return EM

# EM and output = hexadecimal strings
def OAEP_decode(EM):
    hLen = 20
    k = 128
    L = ''
    lHash = hashSha1(L)
    Y = EM[:1]
    maskedSeed = EM[1:hLen+1]
    maskedDB = EM[hLen+1:]
    seedmask= mgf1(maskedSeed, hLen)
    seed = maskedSeed ^ seedMask
    dbMask = mgf1(seed, k - hLen - 1)
    DB = maskedDB ^ dbMask
    lHashPrime = DB[:hLen]
    DBrest = DB[hlen:]
    i = 0
    while DBrest[i:i+1] == '0x00':
        i +=1
    if DBrest[i] != '0x01' or lHash != lHashPrime or Y != b'\00':
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
    integer = int(hexa, 16)
    return integer

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

OAEP_encode('fd5507e917ecbe833878','1e652ec152d0bfcd65190ffc604c0933d0423381')
