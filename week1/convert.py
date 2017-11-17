import hashlib

def intToHex(i):
    return format(i, '08x')

def intToByte(i):
    return i.to_bytes(4, byteorder='big', signed=True)

def hexToInt(i):
    return int(i, 16)

def hexToByte(i):
    return hexToInt(i).to_bytes(8, byteorder='big', signed=True)

def byteToInt(i):
    return int.from_bytes(i, byteorder='big', signed=True)

def byteToHex(i):
    return intToHex(byteToInt(i))

def shaInByte(i):
    m = hashlib.sha1(i)
    return m.digest()

def shaInHex(i):
    m = hashlib.sha1(i)
    return m.hexdigest()

def run():
    print("intToHex: ", intToHex(500))
    print("intToByte: ", intToByte(500))
    print("hexToInt: ", hexToInt('000001f4'))
    print("hexToByte: ", hexToByte('000001f4'))
    print("byteToInt: ", byteToInt(b'\x00\x00\x01\xf4'))
    print("byteToHex: ", byteToHex(b'\x00\x00\x01\xf4'))

    print("testet:")

    print("intToByteSha: ", shaInHex(intToByte(2897)))
    print("String to Byte sha", byteToInt(shaInByte(hexToByte('0123456789abcdef'))))

    print("intToHex: ", intToHex(2897))
    print("hexToByte: ", hexToInt('0123456789abcdef'))
