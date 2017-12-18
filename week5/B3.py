# from base64 import b64decode
import binascii
from base64 import b64encode

def convertToDER(integer):
    hexa = convertValue(integer)
    if len(hexa) < 127:
        return convertShort(integer, len(hexa))
    else:
        byteRep = hexToByte(hexa)
        return convertLong(byteRep, len(hexa))

def convertShort(i, length):
    typeInt = hexToByte('02')
    l = intToByte(length//2)
    i = toOct(intToHex(i))
    # i = twos_complement(i)
    print("v", i)
    print("m", hex(i[0]))
    value = hexToByte(i)
    # value = intToByte(i)
    return byteToHex(typeInt + l + value)

def convertLong(value, length): #length är en int
    typeInt = '02'
    leng = intToByte(length//2)
    size = intToHex(len(leng))
    l = '1' + toBin(size,7)
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
    base64form = b64encode(der)
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
    d = mulinv(e, (p - 1) * (q - 1))
    coeff = mulinv(q, p)
    print("c: ", coeff)
    # d = int(e**(-1))
    ex1 = (d % (p - 1)) #exponent1 INTEGER, -- d mod (p-1)
    ex2 = (d % (q - 1)) #exponent2 INTEGER, -- d mod (q-1)
    coeff1 = (~q % p) #coefficient INTEGER, -- (inverse of q) mod p
    print("c1: ", coeff1)
    v1 = convertToDER(version)
    n1 = convertToDER(n)
    e1 = convertToDER(e)
    d1 = convertToDER(d)
    p1 = convertToDER(p)
    q1 = convertToDER(q)
    ex11 = convertToDER(ex1)
    ex21 = convertToDER(ex2)
    c1 = convertToDER(coeff)
    value = v1+n1+e1+d1+p1+q1+ex11+ex21+c1
    lhex = DER_encode_len(len(value)//2)
    #räkna ut längden
    print("value: ", value)
    # print('30')
    # lhex = intToHex(len(value))
    # print("lhex: ", lhex)

    total = hexToByte('30' + lhex + value)
    # print("total: ", ('30' + lhex + value))
    coded = b64encode(total).decode('utf8')
    # print("coded: ", coded)
    return coded

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

#Antons:
def DER_encode_len(l):
    l_hex = hex2(l)
    # print("l: ", l_hex)
    if l >= 0x80:
        l_hex = '8' + str(len(l_hex) // 2) +  l_hex
    return l_hex

def DER_encode_int(i):
    i_hex = hex2(i)
    if int(i_hex[0], 16) >= 0b1000:
        i_hex = '00' +  i_hex
    # print("i_hex: ", i_hex)
    l_hex = DER_encode_len(len(i_hex) // 2)
    # print("antons lhex: ", l_hex)
    return '02' + l_hex + i_hex

def hex2(x):
    return '{}{:x}'.format('0' * (len(hex(x)) % 2), x)

def mulinv(b, n):
    g, x = extendex_euc_alg(b, n)
    if g == 1:
        return x % n

def extendex_euc_alg(x, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, x, n = x // n, n, x % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  x, x0

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
