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
    typeInt = t
    leng = intToByte(length//2)
    size = intToHex(len(leng))
    l = '1' + toBin(size,7)
    lhex= hex(int(l, 2))
    return typeInt + lhex[2:] + byteToHex(leng) + byteToHex(value)

def convertValue(value):
    hexa = intToByte(value)
    hexa = byteToHex(hexa)
    if int(hexa[0],16) >= 8:
        hexa = '00' + hexa
    return hexa

def DERToBase64(der):
    base64form = b64encode(der).decode('utf8')
    return base64form

def toBin(hexa, nbrOfBits):
    return bin(int(hexa, 16))[2:].zfill(nbrOfBits)

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

print(compute(98239435950283871859290055251487823417858468872243454249930864805578758178601922742963328320272027144214094209587082053918934336062518442341992877622522975095332672112567412809022222298150735937575666451289198289595475505329663797607294450073623714366146233770815063244620511100933664529603308317292204043247, 142950010864217314767307992548770427870292379949341933588213313483471076268376149766340472267258293905363403734515658759712661283726159237082904621242037416160623811509665846997478028753887769737935058395531128044278363768970450333912996628223224277024473587994306293012156601701313473093180049624680368750619))

# print(convertToDER(115825306627494974617112936091425827835448281402401290283974432326054844087575582263242171570825991877334807270839906567633252554681180995275024879674289558948043752015524394301481393607117395367815939202699685605229794931306669415324501795766512165135642149839650203789595512247140642441374672804052150615203, '02'))
