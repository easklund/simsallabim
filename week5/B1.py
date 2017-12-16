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


print('Message: ', decryptM('u7JjHxBYy084Vtfy3ydceAKGK6OFj8uQe3IhyN7mvpJcYLDm3iaTWzJya0xliHSp8nriYALPrrBp8rO9wN4zMXLIlQodHv1nOS1pHMqIfykqteD7l6WWKqtDrWpsOn/pr2y45+DJQiTzxuC4/qTqtCs4NHQ/NrNP1bq+aJnOGBM='))
