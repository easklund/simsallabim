import hashlib
import binascii

def mgf1(mgfSeed, maskLen):
    hLen = 2**32
    #If maskLen > 2^32 hLen, output "mask too long" and stop.
    if len(maskLen) > hLen :
        print("mask no long")
        return -1
    #Let T be the empty octet string.
    T = ''
    #For counter from 0 to \ceil (maskLen / hLen) - 1, do the following:
    for i in range((len(maskLen) / hLen) - 1):
        c = I2OSP(i, 4)
        T = T + Hash(mgfSeed,c)

    #Output the leading maskLen octets of T as the octet string mask.
    return truncate(T, maskLen)

def OAEP_encode(M, seed):
    hLen = 20
    k = 128 #128 bytes
    L = ''
    lHash = Hash(L) #Let lHash = Hash(L), an octet string of length hLen (see
                    #the note below).
    lPS = k - len(M) - 2*hLen - 2
    if lPS == not(0):
        PS = ''
        for i in range(lPS):
            PS = PS + '0'
    DB =   lhash + PS + '1'+ M # step c
    dbMask = mgf1(seed, k - hlen - 1)
    maskedDB = DB ^ dbMask
    seedMask = mgf1(maskedDB, hlen)
    maskedSeed = seed^seedMask
    EM = '0' + maskedSeed + maskedDB
    # output the encoded message EM; OAEP encode(M) = EM.
    return EM

# EM and output = hexadecimal strings
def OAEP_decode(EM):
    #output the decoded message M; OAEP decode(EM) = M.
    k = 128
    c = OS2IP(EM) # TODO implement metoden
    m = RSADP(K, c) #TODO implement the method, find the private key K
    EM = I2OSP(m, k)
    return EM

def I2OSP(x, xLen):
    if x >= (256**xLen):
        #integer too lagre
        return None
    c = str(x % 256)
    for i in range(xLen-1):
        x = x//256
        xi= x % 256
        c += str(xi)
    return c[::-1]

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

def hexToInt(i):
    return int(i, 16)

def truncate(T, size):
    T = hexToInt(T)
    cutT = T % (2**size)
    return cutT
