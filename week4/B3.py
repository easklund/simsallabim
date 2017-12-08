

def mgf1(mgfSeed, maskLen):
    T = ''
    for i in range((maskLen / hLen) - 1):
        





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

def intToHex(i):
    n = format(i,'08x')
    #print(n)
    return n


print(convertInt(1, 4))
