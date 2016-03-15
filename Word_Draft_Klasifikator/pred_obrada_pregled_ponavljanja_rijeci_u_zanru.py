#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Ante
#
# Created:     23.02.2016
# Copyright:   (c) Ante 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import re

word_count = {}
dozvoljeni_formati =("sub","srt","txt")

with open("filmovi_info.txt") as f:
    content = f.readlines()

broj = 0

G = input("Action, Sci-fi, War, Sport, Romance, Western, Crime, Horror \n \n unesi genre za pregled rijeci :  ")

result =[]
for line in content:
    temp = line.split('*')
    if G in temp[2]: #Ovdje je
        #-------------------
        path ="Titlovi/" + temp[1]
        if(path[-3:] in dozvoljeni_formati):
            try:
                broj = broj + 1
                print(broj)
                file = open(path,'r')
                titlovi = file.read()
                rijeci = re.findall("[^\W\d_]+",titlovi)

                for wrd in rijeci:
                    w = wrd.lower()
                    if w in word_count:
                        word_count[w] = word_count[w] + 1
                    else:
                        word_count[w] = 1
            except:
                print("mini fail")

za_pregled = []

for w in word_count:
    if(word_count[w] > 20 ):
        za_pregled.append([w,word_count[w]])

za_pregled.sort(key=lambda x: x[1])

total = sum(word_count.values())

for p in za_pregled:
    print(p)



print("dobaaar")