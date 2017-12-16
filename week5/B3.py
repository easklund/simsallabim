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

def twos_complement(input_value, num_bits):
	'''Calculates a two's complement integer from the given input value's bits'''
	mask = 2**(num_bits - 1)
	return -(input_value & mask) + (input_value & ~mask)

print(tows_complement('0xFFFFFFFF'))
print(convertShort(1234, '12'))
