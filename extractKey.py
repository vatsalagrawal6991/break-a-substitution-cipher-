from random import randint, shuffle, seed
from os import path
from math import log10
from time import time
from sys import argv
#import json

# Initialization
pla = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
plaxg = "abcdefghijklmnopqrstuvwxyz"
freq=  "etaoinshrdlcumwfgypbvkjxqz"
cip = "1234567890@#$zyxwvutsrqpon"
#cip1 = ['1','2','3','4','5','6','7','8','9','0','@','#','$','z','y','x','w','v','u','t','s','r','q','p','o','n']
cipf = []
gramn = {}
itera = 8
itera1 =1000
scorem = -80e8

# file open
abspath = path.dirname(path.abspath(__file__))
rlvpath = path.join(abspath,'quadgrams.txt')
rlvpath2 = path.join(abspath,'INPUT','ciphertext-2.txt')
if (len(argv)==2):
    rlvpath2 = argv[1]
if (len(argv)==3):
    rlvpath2 = argv[1]
    itera = argv[2]
if (len(argv)==4):
    rlvpath2 = argv[1]
    itera = argv[2]
    itera1 = argv[3]
file1 = open(rlvpath2,"r")
#file2 = open(r"/home/baadalvm/NSS/Lab1/OUTPUT/plaintext-212.txt","w")
file3 = open(rlvpath)
textc = file1.read()
#print(textc)


# setting param of quadgrams
lcn = file3.readline()
while lcn:
    a = lcn.split(" ")
    gramn[a[0]] = int(a[1])
    lcn = file3.readline()

#file2.write(json.dumps(gramn))
gramsum = sum(gramn.values())
randio = 0.01/gramsum
finalscore = log10(randio)
for b in gramn:
    gramn[b] = (float(gramn[b]))/gramsum
    gramn[b] = log10(gramn[b])

def testsc(cp12):
    sco = 0
    k = 0
    while k < (len(cp12)-3):
        if cp12[k:k+4] in gramn.keys():
            sco = sco + gramn[cp12[k:k+4]]
        else:
            sco = sco + finalscore
        k = k+1
    return sco

# frequency calculation
lc = {}
for abcde in cip:
    lc[abcde]=0
    #lc1[i]=0

mabc = 0
chc = len(textc)
dictio1234 = {}

while mabc<chc:
    #print(m)
    if textc[mabc] in cip:
        lc[textc[mabc]] = lc[textc[mabc]] +1
    mabc = mabc+1

sor3 = sorted(lc.items(), key = lambda a: (a[1],a[0]), reverse = True )

jabc = 0
for iabcd in sor3:
    dictio1234[freq[jabc]] = iabcd[0]
    jabc = jabc +1

cip1 = []
for jabd in plaxg:
    cip1.append(dictio1234[jabd])

#print(cip1)

# hill climbing algo
i=0
while i<itera:
    dictio202 = {cip1[abg]: abg for abg in range(26)}
    #print(dictio202)
    m = 0
    textp=[]
    while m<chc:
        #print(m)
        if textc[m] in cip:
            pos = dictio202[textc[m]]
            textp.append(pla[pos])
        m=m+1
    textp = "".join(textp)
    #print(textp)
    scorep = testsc(textp)
    z = 0
    x = 0
    y = 0
    while z<=itera1:
        cip2 = [abc for abc in cip1]
        z=z+1
        x,y = randint(0, 25),randint(0, 25)
        temp = cip2[x]
        cip2[x] = cip2[y]
        cip2[y] = temp
        dictio21 = {cip2[abf]: abf for abf in range(26)}
        #print(dictio21)
        w = 0
        textp2 = []
        while w < chc:
            # print(m)
            if textc[w] in cip:
                pos2 = dictio21[textc[w]]
                textp2.append(pla[pos2])
            w = w + 1
        textp2 = ("".join(textp2))
        # print(textp)
        scorep2 = testsc(textp2)
        '''y = y + 1
        if (y>25) or (x>25):
            y=0
            x=x+1'''
        if scorep < scorep2:
            z,scorep = 0,scorep2
            #x = 0
            #y = 0
            cip1=[abd for abd in cip2]
    if scorep > scorem:
        scorem = scorep
        cipf = [abe for abe in cip1]
        #print("scsc")
    i = i + 1
    seed(time())
    shuffle(cip1)
#print(cipf)
cipf = "".join(cipf)
print(cipf)



