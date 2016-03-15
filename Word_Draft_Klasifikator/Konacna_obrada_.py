# coding=utf-8

import random
import math
import os
import re
import time

zanrovi = ("action", "sci-fi", "war", "sport", "romance", "western", "crime", "horror")

#dict sa imenima filmova i puta do titlova
dozvoljeni_formati =("sub","srt","txt")
ime_path= {}
ime_genre = {}
with open("filmovi_info.txt") as f:   #ULAZ !!! **** !!!
    content = f.readlines()
    for line in content:
        temp = line.split('*')
        ime_path[temp[0]] = temp[1]
        ime_genre[temp[0]] = temp[2]





Spec_Rijeci = {}
for zanr in zanrovi:
    with open("zanrovi/" + zanr + ".txt") as f:
        content = f.read()
    Spec_Rijeci[zanr] = content.split("\n")


Spec_Rijeci_X2 = {}
for zanr in zanrovi:
    with open("zanrovi/" + zanr + "_X2.txt") as f:
        content = f.read()
    Spec_Rijeci_X2[zanr] = content.split("\n")




def make_letter_features(naslov):
    #IME NIJE PROMINJENO , ZAMJENSKA FUNKCIJA ZA FILMOVE , VRAĆA SKUP SPEC. RIJEĆI (osobina)


   # imamo titlove za odabrani film
   rijeci=[]
   path ="Titlovi/" + ime_path[naslov]
   if(path[-3:] in dozvoljeni_formati):
        file = open(path,'r')
        titlovi = file.read()
        rijeci = re.findall("[^\W\d_]+",titlovi)

    # ode imamo titlove u listi rijeci

    #TRAŽENJE spec riči u titlu
   final_draft_zanrova = {}
   draft_zanrova = { "action": {}, "sci-fi":{}, "war":{}, "sport":{}, "romance":{}, "western":{}, "crime":{}, "horror":{}}
   draft_zanrova_X2 = { "action": {}, "sci-fi":{}, "war":{}, "sport":{}, "romance":{}, "western":{}, "crime":{}, "horror":{}}

   for i in range(len(rijeci)):
        word = rijeci[i]  # za normalnu obradu
        if(i!= len(rijeci)-1):
            word_X2 = rijeci[i] + " " + rijeci[i+1] # za w-w kombinacije


        for zanr in zanrovi:
            #za normalnu obradu
            if word in Spec_Rijeci[zanr]:
                if word in draft_zanrova[zanr]:
                    draft_zanrova[zanr][word] = draft_zanrova[zanr][word] + 1 # mozemo složeniju funkciju ako bude tribalo
                else:
                    draft_zanrova[zanr][word] = 1
            #-----
            #Za w-w kombinacije
            if word_X2 in Spec_Rijeci_X2[zanr]:
                if word_X2 in draft_zanrova_X2[zanr]:
                    draft_zanrova_X2[zanr][word_X2] = draft_zanrova_X2[zanr][word_X2] + 1 # mozemo složeniju funkciju ako bude tribalo
                else:
                    draft_zanrova_X2[zanr][word_X2] = 1
                    break


   for genre in draft_zanrova.keys():
    if len(draft_zanrova[genre]) == 0:
        final_draft_zanrova[genre] = 0
    else:
     final_draft_zanrova[genre] = sum( draft_zanrova[genre].values()) + len(draft_zanrova[genre].values()) + sum( draft_zanrova_X2[genre].values())*5
   # uzima prvi pick na draftu

   pick = max( final_draft_zanrova, key=final_draft_zanrova.get)


   return pick





def PrintArray(niz):
    stringy = "[ "
    for el in niz:
        stringy = stringy + str(el) + " , "
    return stringy + "]"







brojac = 0
pogodeni =0

for film in ime_path.keys():
    pravi_genre = ime_genre[film]
    dobar = False
    for z in zanrovi:
        if z in pravi_genre.lower():
            dobar= True
    if dobar:
        brojac = brojac + 1



    predpostavka = make_letter_features(film)
    pravi_genre = ime_genre[film]
    if(predpostavka in pravi_genre.lower()  ):
        pogodeni = pogodeni + 1
    print(film + ":   [" + predpostavka + "]--------" + pravi_genre)
    if brojac != 0:
        print( "***  :" + str(pogodeni/brojac))


print("Sve je dobro")


