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


def twos_complement(input_value, num_bits):
	'''Calculates a two's complement integer from the given input value's bits'''
	mask = 2**(num_bits - 1)
	return -(input_value & mask) + (input_value & ~mask)

print(twos_complement(100,3))
