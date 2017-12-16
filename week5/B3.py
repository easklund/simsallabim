from base64 import b64decode
import binascii


def convertToDER(integer):
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
    typeInt = hexToByte('02')
    size = len(length)
    #Kolla hur många octets vi ska ha
    #1 sen hur många octets som följer som repreensterar längden
    #restern va octeterna som respresenterar längden
    l = hexToByte(length)
    value = intToByte(i)
    return byteToHex(typeInt + l + value)

def DERToBase64(der):
    base64form = b64encode(der)
    return base64form

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

def twos_complement(hexa_string):
    out = twos_comp(int(hexa_string,16), 32)
    return out
    
def twos_comp(val, bits):
    if (val & (1 << (bits - 1))) != 0:
        val = val - (1 << bits)
    return val

print(twos_complement('0xFFFFFFFF'))
print(convertShort(1234, '12'))
