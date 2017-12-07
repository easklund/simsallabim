#hej
import requests
requests.packages.urllib3.disable_warnings()
import hashlib
import binascii
import timeit

def genValidSign(name, grade):
    foundRightChar = [None]*20
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
                # print("i: ", i)
                # print("y: ", y)
                foundRightChar[y] = value

    print(foundRightChar)
    signature = ListToString(foundRightChar)
    print(signature)
    payload={'grade': grade, 'name' : name, 'signature': signature}
    r = requests.get('https://eitn41.eit.lth.se:3119/ha4/addgrade.php', params=payload, verify = False)
    print('r: ', r.text)
    if r.text == 1:
        return signature
    else:
        print("We fucked up")

def ListToString(list):
    size = len(list)
    string = ''
    for i in range(size):
        string = string + list[i]
    return string

    # python requeste
    # s = HMAC(name||grade, k)
#return a valid signature
#name=Kalle&grade=5&signature=1

def intToHex(i):
    n = format(i,'01x')
    return n

print(genValidSign('Kalle', '5'))
