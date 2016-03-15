#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Ante
#
# Created:     09.01.2016
# Copyright:   (c) Ante 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import urllib.request
import random
import time
import re
import multiprocessing
import time









lista_id =set()

r1 = urllib.request.urlopen("http://www.omdbapi.com/?t=a")
fail = r1.read()
dat = open("Lista_Filmova9.txt", "w")

moj_url = "http://www.omdbapi.com/?i=tt0"


for rnd in range(700000,800000):

    moj_url = "http://www.omdbapi.com/?i=tt0"

    try:
        moj_url = moj_url + str(rnd)
        response = urllib.request.urlopen(moj_url)
        podatak = response.read()

    except:
        podatak=fail

    if(podatak != fail):
        lista_id.add("tt0" + str(rnd))

        podatak = str(podatak)
        ind = podatak.find('"Title":"')
        podatak = podatak[ind+9:]
        ind = podatak.find('"')
        title =podatak[:ind]

        ind = podatak.find('"Genre":"')
        podatak = podatak[ind+9:]
        ind = podatak.find('"')
        genre =podatak[:ind]
        dat.writelines(title + "*tt0"+str(rnd) +"*" + genre+"\n")

        print(title + "*tt0"+str(rnd) +"*" + genre)
    print()
dat.close()





