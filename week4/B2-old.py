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
            # value = ''
            # for c in range(len(foundRightChar)):
            #     if foundRightChar[c] != None:
            #         value = value + foundRightChar[c]
            #         #print(value)
            # value = value +  intToHex(i)
            #print(value)
            temp = signString + intToHex(i)
            payload={'name' : name, 'grade': grade,  'signature': temp}
            r = requests.get('https://eitn41.eit.lth.se:3119/ha4/addgrade.php', params=payload, verify = False)
            time = r.elapsed.total_seconds()
            if time > bestTime:
                bestTime = time
                # print("i: ", i)
                # print("y: ", y)
                foundRightChar[y] = intToHex(i)
        signString = signString + foundRightChar[y]
    # print(foundRightChar)
    # signature = ListToString(foundRightChar)
    # print(signature)
    signature = signString
    print(signature)
    payload={'grade': grade, 'name' : name, 'signature': signature}
    r = requests.get('https://eitn41.eit.lth.se:3119/ha4/addgrade.php', params=payload, verify = False)
    print('r: ', r.text.strip())
    if r.text.strip() == 1:
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

print(genValidSign('Kalle', '5'))
