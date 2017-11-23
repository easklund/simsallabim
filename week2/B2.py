#!/usr/bin/env python

from pcapfile import savefile


def printPcap():
    testcap = open('test2.pcap', 'rb')
    capfile = savefile.load_savefile(testcap, layers=2, verbose=True)

    # print the packets
    print ('timestamp\teth src\t\t\teth dst\t\t\tIP src\t\tIP dst')
    for pkt in capfile.packets:
        timestamp = pkt.timestamp
        # all data is ASCII encoded (byte arrays). If we want to compare with strings
        # we need to decode the byte arrays into UTF8 coded strings
        eth_src = pkt.packet.src.decode('UTF8')
        eth_dst = pkt.packet.dst.decode('UTF8')
        ip_src = pkt.packet.payload.src.decode('UTF8')
        ip_dst = pkt.packet.payload.dst.decode('UTF8')
        print ('{}\t\t{}\t{}\t{}\t{}'.format(timestamp, eth_src, eth_dst, ip_src, ip_dst))
        return eth_src, eth_dst, ip_src, ip_dst


def findIPinMix(NazirIP, MixIP, m, pcapfile):
    testcap = open(pcapfile, 'rb')
    capfile = savefile.load_savefile(testcap, layers=2, verbose=True)
    i = 0
    ip_src = []
    ip_dst = []
    for pkt in capfile.packets:
        timestamp = pkt.timestamp
        ip_src.append(pkt.packet.payload.src.decode('UTF8'))
        ip_dst.append(pkt.packet.payload.dst.decode('UTF8'))

    i = 0
    suspects = []
    hit = False
    print("längd: ", len(ip_src))
    for i in range(0,len(ip_src)):
        while i <= len(ip_src)-1 and ip_src[i] != MixIP:
            if ip_src[i] == NazirIP:
                hit = True
            i += 1
        if hit == True:
            mySet = set()
            while i <= len(ip_src)-1 and ip_src[i] == MixIP:
                mySet.add(ip_dst[i])
                i += 1
            suspects.append(mySet)
        else:
            while i <= len(ip_src)-1 and ip_src[i] == MixIP :
                i += 1
    return suspects, m

def learningPhase(suspects, m):
    disList = [suspects[0]]
    sets = []
    i = 1
    while len(disList) < m:
        hit = False
        for j in range(len(disList)):
            if not(suspets[i].isdisjoint(disList[j])):
                hit = True
                sets.append(suspets[i])
                break
        if hit == False:
            disList.append(suspets[i])
        i += 1
    return disList, sets

def excludingPhase(disList, sets):
    for i in range disList:
        for j in range sets:
            


#printPcap()
findIPinMix('159.237.13.37', '94.147.150.188', 2, 'test2.pcap')




def interpertationPhase(suspects):
    size = len(suspects)
    finalIntersection = []
    finalIntersection.append(suspects[0])
    finalIntersection.append(suspects[1])

    hit = False
    for i in range(2, size):
        for j in range(0, len(finalIntersection))
            temp = set.intersection(suspects[i], suspects[j])
            if(False):

    while len(finalIntersection) > 1:
        size = len(suspects)
        for i in range(0, size):
            for j in range(i, size):
                if i != j:
                    finalIntersection.append(set.intersection(suspects[i], suspects[j]))
