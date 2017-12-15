#RSA key
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Hash import SHA
from base64 import b64decode

def recoverKey(): #key is in PEM format
    key = open('key.pem', 'rb')
    key = RSA.importKey(key.read())
    e = getattr(key, 'e')
    p = getattr(key, 'p')
    q = getattr(key, 'q')
    d = getattr(key, 'd')
    n = p * q
    return RSA.construct((n,e,d,p,q))

def decryptM(EM):
    decoded_data = b64decode(EM) #Because it is = in the end of the encrypted message we know it is Base64
    dsize = SHA.digest_size
    key = recoverKey()
    s = Random.new().read(15 + dsize)
    cipher = PKCS1_v1_5.new(key)
    m = cipher.decrypt(decoded_data,s)
    return m


print('Message: ', decryptM('T9FAfFVcVCdPH45kv3OU/Kot9NOyQ2t5tWI1GW6nJ4Ul435T68wq1f1vm3KhDcKONzdN3krJ/VwlIzdssIcqmVizw5mnMupmd1gNmf7EKLZWjT4LaMQhDMijrfhxCdbiQKjKqYnUehlOCeDS0JXOJpiYcCtbmTVYHBmxBuOZ1l8='))
