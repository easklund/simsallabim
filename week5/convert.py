from base64 import b64decode
from base64 import b64encode
import binascii

def convertToDER(integer):
    hexa = convertValue(integer)
    if len(hexa) < 127:
        return convertShort(integer, len(hexa)//2)
    else:
        byteRep = hexToByte(hexa)
        return convertLong(byteRep, len(hexa))

def convertShort(i, length):
    typeInt = hexToByte('02')
    l = intToByte(length)
    i_hex = convertValue(i)
    value = hexToByte(i_hex)
    return byteToHex(typeInt + l + value)


def convertLong(value, length): #length är en int
    print("long")
    typeInt = '02'
    leng = intToByte(length//2)
    size = intToHex(len(leng))
    l = '1' + toBin(size,7)
    lhex= hex(int(l, 2))
    return typeInt + lhex[2:] + byteToHex(leng) + byteToHex(value)

def convertPQ(value, length): #length är en int
    print("long")
    typeInt = '30'
    leng = intToByte(length//2)
    l = intToHex(len(leng))
    # l = '1' + toBin(size,7)
    lhex= hex(int(l, 2))
    return typeInt + lhex[2:] + byteToHex(leng) + byteToHex(value)

def byteToInt(i):
    return int.from_bytes(i, byteorder='big', signed=True)

def convertValue(value):
    hexa = intToByte(value)
    hexa = byteToHex(hexa)
    if int(hexa[0],16) >= 8:
        hexa = '00' + hexa
    return hexa

def DERToBase64(der):
    base64form = b64encode(der).decode('utf8')
    return base64form

def toOct(hexa):
    if len(hexa) % 2 == 0:
        return hexa
    else:
        return '0' + hexa

def toBin(hexa, nbrOfBits):
    return bin(int(hexa, 16))[2:].zfill(nbrOfBits)

def lenValue(value):
    return len(intToByte(value))

def compute(p, q):
    version = 0
    e = 65537
    n = p * q
    phi = (p-1)*(q-1)
    d = mulinv(e, phi)
    ex1 = int(d % (p - 1)) #exponent1 INTEGER, -- d mod (p-1)
    ex2 = int(d % (q - 1)) #exponent2 INTEGER, -- d mod (q-1)
    coeff = mulinv(q,p) #coefficient INTEGER, -- (inverse of q) mod p

    v1 = convertToDER(version)
    e1 = convertToDER(e)
    n1 = convertToDER(n)
    e1 = convertToDER(e)
    d1 = convertToDER(d)
    p1 = convertToDER(p)
    q1 = convertToDER(q)
    ex11 = convertToDER(ex1)
    ex21 = convertToDER(ex2)
    c1 = convertToDER(coeff)

    value = v1+n1+e1+d1+p1+q1+ex11+ex21+c1

    byteRep = hexToByte(value)
    total = convertPQ(byteRep, len(value))

    print("total: ", total)

    # coded = DERToBase64(hexToByte(value))
    # print("c:", coded)
    # return hexToByte('30' + len(value) + value)

# function taken from https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def xgcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0

# function taken from https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def mulinv(b, n):
    g, x, _ = xgcd(b, n)
    if g == 1:
        return x % n

def hexToByte(hexa):
    d = binascii.unhexlify(hexa)
    return d

def byteToHex(byte):
    hexa = binascii.hexlify(byte).decode('utf-8')
    return hexa

def intToByte(integer):
    size = (integer.bit_length() + 7 ) // 8
    if integer == 0:
        size = 1
    four_bytes = integer.to_bytes(size, byteorder='big')
    return four_bytes

def intToHex(i):
    n = binascii.hexlify(intToByte(i))
    return n

def twos_complement(string):
    out = twos_comp(string, 32)
    return out

def twos_comp(val, bits):
    size = 1 << (bits - 1)
    if (val & size - 1) != 0:
        size = 1 << bits
        val = val - size
    return val

#print(twos_complement('0xFFFFFFFF'))
#print(twos_comp(1111, 4))
(compute(2530368937, 2612592767))
# print("int1: ", DER_encode_int(161863091426469985001358176493540241719547661391527305133576978132107887717901972545655469921112454527920502763568908799229786534949082469136818503316047702610019730504769581772016806386178260077157969035841180863069299401978140025225333279044855057641079117234814239380100022886557142183337228046784055073741))
# print(convertShort(3920879998437651233, len(intToByte(3920879998437651233))))
# print(convertToDER(161863091426469985001358176493540241719547661391527305133576978132107887717901972545655469921112454527920502763568908799229786534949082469136818503316047702610019730504769581772016806386178260077157969035841180863069299401978140025225333279044855057641079117234814239380100022886557142183337228046784055073741))
# print("int2: ", convertToDER(161863091426469985001358176493540241719547661391527305133576978132107887717901972545655469921112454527920502763568908799229786534949082469136818503316047702610019730504769581772016806386178260077157969035841180863069299401978140025225333279044855057641079117234814239380100022886557142183337228046784055073741))
# print("hej: ", convertToDER(6610823582647678679))
#print(toBin('3f',7))
#print(convertValue(2530368937))
