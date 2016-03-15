#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Ante
#
# Created:     13.01.2016
# Copyright:   (c) Ante 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
from urllib.request import urlopen
from xml.dom.minidom import parse, parseString
import xml.etree.ElementTree as ET
import zipfile
import io

def SkiniTitlove(title,id_filma):
    try:
        rezultat = ""

        nepotpuna_adresa = "http://api.titlovi.com/xml_get_api.ashx?x-dev_api_id=X-DEV-CON_L5hcQ-7HaQq-5Yslk&language=hr&uiculture=hr&keyword="
        title = title.replace(" ","+")
        print("Search for : ",title)
        if title == "Forrest+Gump":
            print("***")
        puna_adresa = nepotpuna_adresa+title
        request = urlopen(puna_adresa)
        podatak = request.read()
        file = open("xml_titlovi6.xml", "w")
        zapis = str(podatak)
        zapis = zapis[41:-1]


        file.flush()
        file.write(zapis)
        file.close()


        pocetak = zapis.find("""<url what="download">""")

        if pocetak != -1: #ako su titlovi nadeni
            tree = ET.parse('xml_titlovi6.xml')
            root = tree.getroot()

            dwnld_IMDB_id = root[0][8].text
            if id_filma != dwnld_IMDB_id:
                return "fail"

            zapis = zapis[pocetak:]
            kraj = zapis.find("url>")

            zapis = zapis[:kraj]
            download_id = zapis[-9:-3]
            if download_id[0] == '-':
                download_id = download_id[1:]




            download_titles_addres = """http://titlovi.com/downloads/default.ashx?type=1&mediaid="""
            download_titles_addres = download_titles_addres + download_id
            try:
                zipani_titlovi_request = urlopen(download_titles_addres)
                zipani_titlovi = zipani_titlovi_request.read()


                zf = zipfile.ZipFile(io.BytesIO(zipani_titlovi), "r")
                info_zf = zf.namelist()
                zf.extract(info_zf[0], path = "Titlovi")
                rezultat = str(info_zf[0])
                return(rezultat)
            except:
                return("fail")
        else:
            return "fail"
    except:
        return("fail")

#****************************************************************************************

banned_genres = ("N/A","Musical","Short","Adult","Music")

lista_filmova = open("Lista_Filmova6.txt", "r")


film_string = lista_filmova.read()
lista_filmova.close()
film_list = film_string.split("\n")



i = 0
while i < len(film_list):
    esi_mi_dobar = True #dobar ko tiket od 50 iljada
    try:
        film_list[i] = film_list[i].split("*")
        film_list[i][2]=film_list[i][2].split(", ")
    except:
        esi_mi_dobar=False



    for x in banned_genres:
        if x in  film_list[i][2]:
            esi_mi_dobar=False
    try:
        for char in film_list[i][0]:
            if (ord(char)<65  or ord(char)>122)  and (char != " "):
                esi_mi_dobar=False
    except:
        esi_mi_dobar = False

    if esi_mi_dobar:
         skidanje_titlova = SkiniTitlove(film_list[i][0],film_list[i][1])
         if skidanje_titlova =="fail":
            esi_mi_dobar=False
         else:
            try:
                finalna_lista = open("Finalna_lista_filmova6.txt", "a")
                finalna_lista.write(film_list[i][0]+"*"+skidanje_titlova+"*")
                for g in film_list[i][2]:
                    finalna_lista.write(str(g)+";")
                finalna_lista.write("\n")
                finalna_lista.close()
            except:
                print("bad title name")



    if not esi_mi_dobar:
        film_list.pop(i)
        i= i-1
    i = i+1





print("Yeeeah")



