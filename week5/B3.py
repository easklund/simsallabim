from base64 import b64decode
import binascii


def convertToDER(integer):
    #hexRep = intToHex(integer)
    hexa = intToByte(integer)
    print('hexa: ', byteToHex(hexa))
    print(len(hexa))
    if len(hexa) < 127:
        return convertShort(integer, len(hexa))
    else:
        return convertLong(octRep, len(hexa)//2)
    # octRep = toOct(hexa)
    # print(octRep)
    #
    # print('octRep: ',toOct(intToHex(len(octRep))))
    # der =
    # return der
    #konvertera till tvåkomplements form
    #kolla längden på integern
    #lägg till typen integer
    #lägg till längden
    #lägg till value
    pass

def convertShort(i, length):
    typeInt = hexToByte('02')
    l = intToByte(length)
    i = twos_complement(i)
    value = intToByte(i)
    return byteToHex(typeInt + l + value)

def convertLong(value, length): #length är en int
    typeInt = '02'
    leng = intToByte((length))
    print('leng: ', leng)
    size = binascii.hexlify(intToByte(len(leng)//2))
    #print('längden',len(length)//2)
    #l = toOct(intToHex(8 + len(length)//2))
    print('size to bin: ', toBin(size,7))
    l = '1' + toBin(size,7)
    #l =  toOct(binascii.hexlify(b'\1' + hexToByte(toBin(size,7))))
    print('l: ',l)
    lhex= hex(int(l, 2))
    print('lhex: ', lhex)
    return typeInt + lhex[2] + lhex[3] + byteToHex(value)

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
    d = e**(-1)
    ex1 = d % (p - 1) #exponent1 INTEGER, -- d mod (p-1)
    ex2 = d % (q - 1) #exponent2 INTEGER, -- d mod (q-1)
    coeff = ~q % p #coefficient INTEGER, -- (inverse of q) mod p
    v1 = convertToDER(version)
    e1 = convertToDER(e)
    n1 = convertToDER(n)
    d1 = convertToDER(d)
    ex11 = convertToDER(ex11)
    ex21 = convertToDER(ex21)
    c1 = convertToDER(c1)
    value = v1+e1+n1+d1+ex11+ex21+c1

    return hexToByte('30' + intToHex(lenValue(value)) + value)


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
    n = format(i,'08x')
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
    if l >= 0x80:
        l_hex = '8' + str(len(l_hex) // 2) +  l_hex
    return l_hex

def DER_encode_int(i):
    i_hex = hex2(i)
    if int(i_hex[0], 16) >= 0b1000:
        i_hex = '00' +  i_hex
    print(i_hex)
    l_hex = DER_encode_len(len(i_hex) // 2)
    print(l_hex)
    return '02' + l_hex + i_hex

def hex2(x):
    return '{}{:x}'.format('0' * (len(hex(x)) % 2), x)

#print(twos_complement('0xFFFFFFFF'))
print(compute(2530368937, 2612592767))
# print(DER_encode_int(3920879998437651233))
# print(convertShort(3920879998437651233, len(intToByte(3920879998437651233))))
# print(convertToDER(6610823582647678679))
#print(convertToDER(161863091426469985001358176493540241719547661391527305133576978132107887717901972545655469921112454527920502763568908799229786534949082469136818503316047702610019730504769581772016806386178260077157969035841180863069299401978140025225333279044855057641079117234814239380100022886557142183337228046784055073741))
#print(toBin('3f',7))
