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

print(compute(129546416390918892633521788734635577320647078456612976998136037668757166839677002751887356738368424049688976054669291051538993948711521348817508593719692308977966944224400232748906474103001313687040647327924599636673492551167648360769116047845690067593351731150264205315240004227367623816322350455523911020919, 109690639789780343026052789532684436727126095861552077291187266690465860592548618603482692099175361845491898725906822221052776690443608650844168031864443802791437292504579980347644787905385409664503783308899176403319950232048284236334297123118725860369711431270323422013041870615375322030837965948196897327659))

# print(convertToDER(168217199074060165239226710278165035349949947032889571539238996186766637061492280872525137538021859499532607381338958006231157040880095589868299716253276123631246236688161037373019406433446565771144059193187436068312932748830340434768831412264979291837831652750107852614212398455053809414148031777860743455253, '02'))
