#!/usr/bin/env python

from pcapfile import savefile


def printPcap():
    testcap = open('test.pcap', 'rb')
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
def learning_phase(sender_ip, mix_ip, m, file_in):
    testcap = open(file_in, 'rb')
    capfile = savefile.load_savefile(testcap, layers=2, verbose=True)
    i = 0
    ip_sources = []
    ip_dests = []
    for pkt in capfile.packets:
        timestamp = pkt.timestamp
        ip_sources.append(pkt.packet.payload.src.decode('UTF8'))
        ip_dests.append(pkt.packet.payload.dst.decode('UTF8'))

    R, sets, i = [], [], 0
    while i is not None:
        i = ip_sources.index(sender_ip, i)
        start = i = ip_sources.index(mix_ip, i)
        try: i = ip_dests.index(mix_ip, i)
        except: i = None
        receivers = ip_dests[start:i]
        t_set = R if len(R) < m and is_disjoint(R, receivers) else sets
        t_set.append(set(receivers))
    return R, sets

def emma(NazirIP, MixIP, m, pcapfile):
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
            t_set = disList if len(disList) < m and is_disjoint(disList, mySet) else sets
            t_set.append(set(mySet))

        else:
            while i <= len(ip_src)-1 and ip_src[i] == MixIP :
                i += 1
    return disList, sets

def learningPhase(suspects, m):
    disList = [suspects[0]]
    sets = []
    i = 1
    while len(disList) < m:
        hit = False
        for j in range(len(disList)):
            if not(suspects[i].isdisjoint(disList[j])):
                hit = True
                sets.append(suspects[i])
                break
        if hit == False:
            disList.append(suspects[i])
        i += 1
    return disList, sets

def is_disjoint(list_of_sets, set2):
    joint_sets = [0 for item_set in list_of_sets if not(item_set.isdisjoint(set2))]
    return len(joint_sets) == 0

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

#printPcap()
#suspects, m = findIPinMix('159.237.13.37', '94.147.150.188', 2, 'test2.pcap')
#disList, sets = learningPhase(suspects, m)
disList, sets = learning_phase('159.237.13.37', '94.147.150.188', 2, 'test2.pcap')
done = excludingPhase(disList, sets)
print("Anton: ", done)
disList, sets = emma('159.237.13.37', '94.147.150.188', 2, 'test2.pcap')
done = excludingPhase(disList, sets)
print("Emma: ", done)
