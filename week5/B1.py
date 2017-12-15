#RSA key
from Crypto.PublicKey import RSA

def crackDecryption(M, EM):
    return RSA.decrypt(M,EM)




def recoverKey(): #key is in PEM format
    key = open('key.pem', 'r') # do I need to decrypt the key first?
    key = RSA.importKey(key.read())
    return key


#print(recoverKey())
crackDecryption('This is secret','Qe7+h9OPQ7PN9CmF0ZOmD32fwpJotrUL67zxdRvhBn2U3fDtoz4iUGRXNOxwUXdJ2Cmz7zjS0DE8ST5dozBysByz/u1H//iAN+QeGlFVaS1Ee5a/TZilrTCbGPWxfNY4vRXHP6CB82QxhMjQ7/x90/+JLrhdA99lvmdNetGZjY=')
