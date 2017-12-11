from hashlib import sha1
from math import ceil
from binascii import unhexlify, hexlify
from sys import argv

def to_byte(h):
    return unhexlify(h)

def to_hex(b):
    return hexlify(b).decode('utf-8')

def I2OSP(x, xLen):
    X = []
    for i in range(xLen):
        X.append(x % 256)
        x //= 256
    return bytes(X[::-1])

def OAEP_encode(M, seed, k = 128, hLen = 20, L=b'', Hash=sha1):
    lHash = Hash(L).digest()
    print('lHash: ', lHash)
    PS = I2OSP(0, k - len(M) // 2 - 2 * hLen - 2)
    print('PS: ', PS)
    DB = lHash  + PS + I2OSP(1, 1) +  to_byte(M)
    print('DB: ', DB)
    dbMask = MGF1(seed, k- hLen - 1)
    print('dbMask: ', dbMask)
    maskedDB = bytes(a ^ b for a, b in zip(to_byte(dbMask), DB))
    print('maskedDB: ', maskedDB)
    seedMask = MGF1(to_hex(maskedDB), hLen)
    print('seedMask: ', seedMask)
    maskedSeed = bytes(a ^ b for a, b in zip(to_byte(seed), to_byte(seedMask)))
    print('maskedSeed: ', maskedSeed)
    EM = I2OSP(0, 1) +  maskedSeed + maskedDB
    print('EM: ', to_hex(EM))
    return to_hex(EM)

def OAEP_decode(EM, k = 128, hLen = 20):
    EM = to_byte(EM)
    print('EM: ', EM)
    maskedSeed = EM[1:hLen + 1]
    print('maskedSeed: ', maskedSeed)
    maskedDB = EM[hLen + 1:]
    print('maskedDB: ', maskedDB)
    seedMask = MGF1(to_hex(maskedDB), hLen)
    print('seedMask: ', seedMask)
    seed = bytes(a ^ b for a, b in zip(maskedSeed, to_byte(seedMask)))
    print('seed: ', seed)
    dbMask = MGF1(to_hex(seed), k - hLen - 1)
    print('dbMask: ', dbMask)
    DB = bytes(a ^ b for a, b in zip(to_byte(dbMask), maskedDB))[hLen:]
    print('DB: ', DB)
    index = DB.index(1) + 1
    M = DB[index:]
    print('M: ', M)
    return to_hex(M)

def MGF1(mgfSeed, maskLen, hLen = 20, Hash=sha1):
    mgfSeed = to_byte(mgfSeed)
    T = b''
    for i in range(ceil(maskLen / hLen)):
         C = I2OSP(i, 4)
         # print('C: ', C)
         T += Hash(mgfSeed + C).digest()
    return to_hex(T[:maskLen])

OAEP_encode('fd5507e917ecbe833878','1e652ec152d0bfcd65190ffc604c0933d0423381')
# OAEP_decode('0000255975c743f5f11ab5e450825d93b52a160aeef9d3778a18b7aa067f90b2178406fa1e1bf77f03f86629dd5607d11b9961707736c2d16e7c668b367890bc6ef1745396404ba7832b1cdfb0388ef601947fc0aff1fd2dcd279dabde9b10bfc51f40e13fb29ed5101dbcb044e6232e6371935c8347286db25c9ee20351ee82')

# if __name__ == '__main__':
#     if len(argv) == 2:
#         mgfSeed = input('').split("=")[1]
#         maskLen = int(input('').split("=")[1])
#         MG = MGF1(mgfSeed, maskLen)
#         M = input('').split("=")[1]
#         seed = input('').split("=")[1]
#         ec_M = OAEP_encode(M, seed)
#         EM = input('').split("=")[1]
#         dc_M = OAEP_decode(EM)
#     else:
#         mgfSeed = input('mgfSeed: ')
#         maskLen = int(input('maskLen: '))
#         MG = MGF1(mgfSeed, maskLen)
#         M = input('M: ')
#         seed = input('seed: ')
#         ec_M = OAEP_encode(M, seed)
#         EM = input('EM: ')
#         dc_M = OAEP_decode(EM)
#     print("MGF1:", MG)
#     print("\nEM:", ec_M)
#     print("\nDM:",dc_M)
