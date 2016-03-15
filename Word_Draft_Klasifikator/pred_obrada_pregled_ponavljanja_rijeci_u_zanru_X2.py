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
zanrovi = ("action", "sci-fi", "war", "sport", "romance", "western", "crime", "horror")
Spec_Rijeci = {}
for zanr in zanrovi:
    with open("zanrovi/" + zanr + ".txt") as f:
        content = f.read()
    Spec_Rijeci[zanr] = content.split("\n")


word_count = {}
dozvoljeni_formati =("sub","srt","txt")

with open("filmovi_info.txt") as f:
    content = f.readlines()

broj = 0

result =[]
genre = input("Action, Sci-fi, War, Sport, Romance, Western, Crime, Horror \n \n unesi genre za pregled rijeci :  ")
for line in content:
    temp = line.split('*')
    if genre in temp[2]:
        #-------------------
        path ="Titlovi/" + temp[1]
        if(path[-3:] in dozvoljeni_formati):
            try:
                broj = broj + 1
                print(broj)
                file = open(path,'r')
                titlovi = file.read()
                rijeci = re.findall("[^\W\d_]+",titlovi)

                for i in range(len(rijeci)-1):
                    korisna = False
                    w = rijeci[i].lower() + " " + rijeci[i+1].lower()
                    for spec_word in Spec_Rijeci["war"]:
                        if spec_word in w:
                            korisna = True
                            break
                    if korisna:
                        if w in word_count:
                            word_count[w] = word_count[w] + 1
                        else:
                            word_count[w] = 1
            except:
                print("mini fail")

za_pregled = []

for w in word_count:
    if(word_count[w] > 5 ):
        za_pregled.append([w,word_count[w]])

za_pregled.sort(key=lambda x: x[1])

total = sum(word_count.values())


for line in za_pregled:
    print(line[0] + "        [" + str(line[1]) + "]")
print("Sve je dobro.")