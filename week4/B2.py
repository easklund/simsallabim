#hej
import requests
import hashlib
import binascii
import timeit

def genValidSign(name, grade):
    foundRightChar = [20]
    for y in range(20):
        bestTime = 0
        for i in range(16):
            value= intToHex(i)
            payload={'grade': grade, 'name' : name, 'signature': value}

            #time = float(timeit.Timer('requests.get("https://eitn41.eit.lth.se:3119/ha4/addgrade.php?", params=payload)')
            r = requests.get('https://eitn41.eit.lth.se:3119/ha4/addgrade.php', params=payload, verify = False)
            time = r.elapsed.total_seconds()
            # if bestTime == None:
            #     bestTime = time
            if time >bestTime:
                bestTime = time
                foundRightChar[y-1] = i

    r = requests.get('https://eitn41.eit.lth.se:3119/ha4/addgrade.php?', params=payload)
    if r == 1:
        return value
    else:
        print("We fucked up")


    # python requeste
    # s = HMAC(name||grade, k)
#return a valid signature
#name=Kalle&grade=5&signature=1

def intToHex(i):
    n = format(i,'08x')
    return n

print(genValidSign('Kalle', '5'))
