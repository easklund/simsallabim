from base64 import b64decode
from base64 import b64encode
import binascii

def convertToDER(integer, t):
    hexa = convertValue(integer)
    if len(hexa) < 127:
        return convertShort(integer, len(hexa)//2, t)
    else:
        byteRep = hexToByte(hexa)
        return convertLong(byteRep, len(hexa), t)

def convertShort(i, length, t):
    typeInt = hexToByte(t)
    l = intToByte(length)
    i_hex = convertValue(i)
    value = hexToByte(i_hex)
    return byteToHex(typeInt + l + value)


def convertLong(value, length, t): #length är en int
    print("long")
    typeInt = t
    leng = intToByte(length//2)
    size = intToHex(len(leng))
    l = '1' + toBin(size,7)
    lhex= hex(int(l, 2))
    return typeInt + lhex[2:] + byteToHex(leng) + byteToHex(value)

def convertPQ(value, length): #length är en int
    print("long")
    typeInt = '30'
    leng = intToByte(length//2)
    size = intToHex(len(leng))
    l = '1' + toBin(size,7)
    lhex= hex(int(l, 2))
    return hexToByte(typeInt) + hexToByte(lhex[2:]) + leng + value

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

    v1 = convertToDER(version, '02')
    e1 = convertToDER(e, '02')
    n1 = convertToDER(n, '02')
    e1 = convertToDER(e, '02')
    d1 = convertToDER(d, '02')
    p1 = convertToDER(p, '02')
    q1 = convertToDER(q, '02')
    ex11 = convertToDER(ex1, '02')
    ex21 = convertToDER(ex2, '02')
    c1 = convertToDER(coeff, '02')

    value = v1+n1+e1+d1+p1+q1+ex11+ex21+c1

    byteRep = hexToInt(value)
    total = convertToDER(byteRep, '30')
    total = hexToByte(total)
    coded = DERToBase64(total)
    return coded

def hexToInt(i):
    return int(i, 16)

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
# (compute(2530368937, 2612592767))
# print(compute(139721121696950524826588106850589277149201407609721772094240512732263435522747938311240453050931930261483801083660740974606647762343797901776568952627044034430252415109426271529273025919247232149498325412099418785867055970264559033471714066901728022294156913563009971882292507967574638004022912842160046962763, 141482624370070397331659016840167171669762175617573550670131965177212458081250216130985545188965601581445995499595853199665045326236858265192627970970480636850683227427420000655754305398076045013588894161738893242561531526805416653594689480170103763171879023351810966896841177322118521251310975456956247827719))
# print("int1: ", DER_encode_int(161863091426469985001358176493540241719547661391527305133576978132107887717901972545655469921112454527920502763568908799229786534949082469136818503316047702610019730504769581772016806386178260077157969035841180863069299401978140025225333279044855057641079117234814239380100022886557142183337228046784055073741))
# print(convertShort(3920879998437651233, len(intToByte(3920879998437651233))))
print(convertToDER(161863091426469985001358176493540241719547661391527305133576978132107887717901972545655469921112454527920502763568908799229786534949082469136818503316047702610019730504769581772016806386178260077157969035841180863069299401978140025225333279044855057641079117234814239380100022886557142183337228046784055073741, '02'))
# print("int2: ", convertToDER(161863091426469985001358176493540241719547661391527305133576978132107887717901972545655469921112454527920502763568908799229786534949082469136818503316047702610019730504769581772016806386178260077157969035841180863069299401978140025225333279044855057641079117234814239380100022886557142183337228046784055073741))
# print("hej: ", convertToDER(6610823582647678679))
#print(toBin('3f',7))
#print(convertValue(2530368937))
