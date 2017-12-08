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
    hlen = 20
    k = 128

    #output the decoded message M; OAEP decode(EM) = M.
    #EM = Y + maskedSeed + maskedDB (len(Y)= 1 octet, len(maskedSeed) = hlen, len(maskedDB(k-hlen-1))
    # b.  Separate the encoded message EM into a single octet Y, an
    #           octet string maskedSeed of length hLen, and an octet
    #           string maskedDB of length k - hLen - 1 as
    #
    #              EM = Y || maskedSeed || maskedDB.
    #
    #       c.  Let seedMask = MGF(maskedDB, hLen).
    #
    #       d.  Let seed = maskedSeed \xor seedMask.
    #
    #       e.  Let dbMask = MGF(seed, k - hLen - 1).
    #
    #       f.  Let DB = maskedDB \xor dbMask.
    #
    #       g.  Separate DB into an octet string lHash' of length hLen, a
    #           (possibly empty) padding string PS consisting of octets
    #           with hexadecimal value 0x00, and a message M as
    #
    #              DB = lHash' || PS || 0x01 || M.
    #
    #           If there is no octet with hexadecimal value 0x01 to
    #           separate PS from M, if lHash does not equal lHash', or if
    #           Y is nonzero, output "decryption error" and stop.  (See
    #           the note below.)

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

def hexToInt(i):
    return int(i, 16)

def truncate(T, size):
    T = hexToInt(T)
    cutT = T % (2**size)
    return cutT

print(convertInt(15,4))
