from base64 import b64decode
import binascii


def convertToDER(integer):
    hexRep = intToHex(integer)
    hexa = binascii.hexlify(intToByte(integer))
    print(hexa)
    print(len(hexa))
    octRep = toOct(hexa)
    print(octRep)

    print('octRep: ',toOct(intToHex(len(octRep))))
    der = convertLong(octRep, len(hexa)//2)
    return der
    #konvertera till tvåkomplements form
    #kolla längden på integern
    #lägg till typen integer
    #lägg till längden
    #lägg till value
    pass

def convertShort(i, length):
    typeInt = hexToByte('02')
    l = hexToByte(length)
    value = intToByte(i)
    return byteToHex(typeInt + l + value)

def convertLong(value, length): #length är en int
    typeInt = '02'
    leng = binascii.hexlify(intToByte((length)))
    print('leng: ', leng)
    size = binascii.hexlify(intToByte(len(leng)//2))
    #print(len(length)//2)
    #l = toOct(intToHex(8 + len(length)//2))
    print('size to bin: ', toBin(size,7))
    l = '1' + toBin(size,7)
    #l =  toOct(binascii.hexlify(b'\1' + hexToByte(toBin(size,7))))
    print('l: ',l)
    lhex= hex(int(l, 2))
    print('lhex: ', lhex)
    return typeInt + byteToHex(lhex) + value

def DERToBase64(der):
    base64form = b64encode(der)
    return base64form

def toOct(hexa):
    if len(hexa) % 2 == 0:
        return hexa
    else:
        return '0' + hexa

#=======

def toBin(hexa, nbrOfBits):
    return bin(int(hexa, 16))[2:].zfill(nbrOfBits)

def compute(p, q):
    version = 0
    e = 65537
    n = p * q
    d = e**(-1)
    ex1 = d % (p - 1) #exponent1 INTEGER, -- d mod (p-1)
    ex2 = d % (q - 1) #exponent2 INTEGER, -- d mod (q-1)
    coeff = ~q % p #coefficient INTEGER, -- (inverse of q) mod p

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
    out = twos_comp(int(string,16), 32)
    return out

def twos_comp(val, bits):
    size = 1 << (bits - 1)
    if (val & size - 1) != 0:
        size = 1 << bits
        val = val - size
    return val

#print(twos_complement('0xFFFFFFFF'))
#print(convertShort(1234, '12'))
print(convertToDER(6610823582647678679))
#print(toBin('3f',7))
