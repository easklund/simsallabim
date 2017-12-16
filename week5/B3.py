from base64 import b64decode
import binascii


def convertToDER(integer):
    hexRep = intToHex(integer)
    octRep = toOct(hexRep)
    der = convertLong(octRep, toOct(intToHex(len(octRep))))
    return der
    #konvertera till tvåkomplements form
    #kolla längden på integern
    #lägg till typen integer
    #lägg till längden
    #lägg till value
    pass

def convertShort(i, length):
    # TLV where type is integer that has tag 2
    typeInt = hexToByte('02')
    l = hexToByte(length)
    value = intToByte(i)
    return byteToHex(typeInt + l + value)

def convertLong(value, length):
    # TLV where type is integer that has tag 2
    typeInt = '02'
    size = intToHex(len(length)//2)
    l =  toOct(binascii.hexlify(b'\1' + toBin(size,7)))
    return typeInt + l + value
    #Kolla hur många octets vi ska ha
    #1 sen hur många octets som följer som repreensterar längden
    #restern va octeterna som respresenterar längden
    #l = hexToByte(length)
    #value = intToByte(i)
    #return byteToHex(typeInt + l + value)

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

def twos_complement(hexa_string):
    out = twos_comp(int(hexa_string,16), 32)
    return out

def twos_comp(val, bits):
    size = 1 << (bits - 1)
    if (val & size - 1) != 0:
        size = 1 << bits
        val = val - size
    return val

#print(twos_complement('0xFFFFFFFF'))
#print(convertShort(1234, '12'))
print(convertToDER(161863091426469985001358176493540241719547661391527305133576978132107887717901972545655469921112454527920502763568908799229786534949082469136818503316047702610019730504769581772016806386178260077157969035841180863069299401978140025225333279044855057641079117234814239380100022886557142183337228046784055073741))
#print(toBin('3f',7))
