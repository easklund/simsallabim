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
        c = convertInt(i, 4)
        T = T + Hash(mgfSeed,c)

    #Output the leading maskLen octets of T as the octet string mask.
    return truncate(T, maskLen)

def OAEP_encode(M, seed):
#     Length checking:
#
#           a.  If the length of L is greater than the input limitation
#               for the hash function (2^61 - 1 octets for SHA-1), output
#               "label too long" and stop.
#
#           b.  If mLen > k - 2hLen - 2, output "message too long" and
#               stop.
#
#       2.  EME-OAEP encoding (see Figure 1 below):
#
#           a.  If the label L is not provided, let L be the empty string.
#               Let lHash = Hash(L), an octet string of length hLen (see
#               the note below).
#
#           b.  Generate a padding string PS consisting of k - mLen -
#               2hLen - 2 zero octets.  The length of PS may be zero.
#
#
#     L =
#
# Moriarty, et al.              Informational                    [Page 22]
#
# RFC 8017                      PKCS #1 v2.2                 November 2016
#
#
#           c.  Concatenate lHash, PS, a single octet with hexadecimal
#               value 0x01, and the message M to form a data block DB of
#               length k - hLen - 1 octets as
#
#                  DB = lHash || PS || 0x01 || M.
#
#           d.  Generate a random octet string seed of length hLen.
#
#           e.  Let dbMask = MGF(seed, k - hLen - 1).
#
#           f.  Let maskedDB = DB \xor dbMask.
#
#           g.  Let seedMask = MGF(maskedDB, hLen).
#
#           h.  Let maskedSeed = seed \xor seedMask.
#
#           i.  Concatenate a single octet with hexadecimal value 0x00,
#               maskedSeed, and maskedDB to form an encoded message EM of
#               length k octets as
#
#                  EM = 0x00 || maskedSeed || maskedDB.
#
#       3.  RSA encryption:
#
#           a.  Convert the encoded message EM to an integer message
#               representative m (see Section 4.2):
#
#                  m = OS2IP (EM).
#
#           b.  Apply the RSAEP encryption primitive (Section 5.1.1) to
#               the RSA public key (n, e) and the message representative m
#               to produce an integer ciphertext representative c:
#
#                  c = RSAEP ((n, e), m).
#
#           c.  Convert the ciphertext representative c to a ciphertext C
#               of length k octets (see Section 4.1):
#
#                  C = I2OSP (c, k).
#
#
#
#
#
#
#
#
#
#
#
#
# Moriarty, et al.              Informational                    [Page 23]
#
# RFC 8017                      PKCS #1 v2.2                 November 2016
#
#
#       4.  Output the ciphertext C.
#
#       _________________________________________________________________
#
#                                 +----------+------+--+-------+
#                            DB = |  lHash   |  PS  |01|   M   |
#                                 +----------+------+--+-------+
#                                                |
#                      +----------+              |
#                      |   seed   |              |
#                      +----------+              |
#                            |                   |
#                            |-------> MGF ---> xor
#                            |                   |
#                   +--+     V                   |
#                   |00|    xor <----- MGF <-----|
#                   +--+     |                   |
#                     |      |                   |
#                     V      V                   V
#                   +--+----------+----------------------------+
#             EM =  |00|maskedSeed|          maskedDB          |
#                   +--+----------+----------------------------+
#       _________________________________________________________________
#
#                    Figure 1: EME-OAEP Encoding Operation

    # output the encoded message EM; OAEP encode(M) = EM.
    return -1

# EM and output = hexadecimal strings
def OAEP_decode(EM):
    #output the decoded message M; OAEP decode(EM) = M.

    return -1

def convertInt(x, xLen):
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

def truncate(T, size):
    T = hexToInt(T)
    cutT = T % (2**size)
    return cutT
