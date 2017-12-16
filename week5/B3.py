from base64 import b64decode


def convertToDER(integer):
    #konvertera till tvåkomplements form
    #kolla längden på integern
    #lägg till typen integer
    #lägg till längden
    #lägg till value
    pass

def convertShort():
    pass

def convertLong():
    pass

def DERToBase64(der):
    base64form = b64encode(der)
    return base64form

def twos_complement(hexa_string):
    out = twos_comp(int(hex_string,16), 32)
    return out

print(tows_complement('0xFFFFFFFF'))
