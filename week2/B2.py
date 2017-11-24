from pcapfile import savefile
from socket import *
import ipaddress

def learningPhase(NazirIP, MixIP, m, pcapfile):
    testcap = open(pcapfile, 'rb')
    capfile = savefile.load_savefile(testcap, layers=2, verbose=True)
    i = 0
    ip_src = []
    ip_dst = []
    for pkt in capfile.packets:
        timestamp = pkt.timestamp
        ip_src.append(pkt.packet.payload.src.decode('UTF8'))
        ip_dst.append(pkt.packet.payload.dst.decode('UTF8'))
    disList = []
    sets = []
    hit = False
    first = True
    while i <= len(ip_src)-1:
        while i <= len(ip_src)-1 and ip_src[i] != MixIP:
            if ip_src[i] == NazirIP:
                hit = True
            i += 1

        if hit == True:
            mySet = set()
            while i <= len(ip_src)-1 and ip_src[i] == MixIP:
                mySet.add(ip_dst[i])
                i += 1
            putInRightSet(disList, sets, mySet, m)
            hit = False

        else:
            while i <= len(ip_src)-1 and ip_src[i] == MixIP :
                i += 1
    return disList, sets

def isDisjointFromAllSets(lists, mySet):
    for i in range(len(lists)):
        if not(lists[i].isdisjoint(mySet)):
            return False
    return True

def putInRightSet(disList, sets, mySet, m):
    if len(disList) < m and isDisjointFromAllSets(disList, mySet):
        disList.append(mySet)
    else:
        sets.append(mySet)

def excludingPhase(disList, sets):
    hit = -1
    bad = False
    for i in range(len(sets)):
        for j in range(len(disList)):
            if not(sets[i].isdisjoint(disList[j])):
                if hit == -1:
                    hit = j
                else:
                    bad = True
        if hit != -1 and not(bad):
            disList[hit] &= sets[i]
        hit = -1
        bad = False
    return disList

def ipToInt(ip):
    interger = int(ipaddress.IPv4Address(ip))
    return interger

def sumIpFromSet(done):
    summa = 0
    for i in range(len(done)):
        kl = str(done.pop()).replace('{','').replace('}','').replace('\'','')
        summa += ipToInt(kl)
    return summa

disList, sets = learningPhase('159.237.13.37', '94.147.150.188', 2, 'test2.pcap')
done = excludingPhase(disList, sets)
print("summa1: ", sumIpFromSet(done))

disList, sets = learningPhase('161.53.13.37', '11.192.206.171', 12, 'test3.pcap')
done = excludingPhase(disList, sets)
print("summa2: ", sumIpFromSet(done))
