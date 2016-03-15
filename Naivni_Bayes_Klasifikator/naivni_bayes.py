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
import sys
import math
import re

#******* S T E M M Y ********
def Stemmy(words):
    stop=set(['biti','jesam','budem','sam','jesi','budeĂ„â€šĂ˘â‚¬ĹľÄ‚â€žĂ˘â‚¬Â¦Ă„â€šĂ˘â‚¬Ä…Ä‚ËĂ˘â€šÂ¬Ă‹â€ˇ','si','jesmo','budemo','smo','jeste','budete','ste','jesu','budu','su','bih','bijah','bjeh','bijaĂ„â€šĂ˘â‚¬ĹľÄ‚â€žĂ˘â‚¬Â¦Ă„â€šĂ˘â‚¬Ä…Ä‚ËĂ˘â€šÂ¬Ă‹â€ˇe','bi','bje','bjeĂ„â€šĂ˘â‚¬ĹľÄ‚â€žĂ˘â‚¬Â¦Ă„â€šĂ˘â‚¬Ä…Ä‚ËĂ˘â€šÂ¬Ă‹â€ˇe','bijasmo','bismo','bjesmo','bijaste','biste','bjeste','bijahu','biste','bjeste','bijahu','bi','biĂ„â€šĂ˘â‚¬ĹľÄ‚â€žĂ˘â‚¬Â¦Ă„â€šĂ˘â‚¬Ä…Ä‚ËĂ˘â€šÂ¬Ă‹â€ˇe','bjehu','bjeĂ„â€šĂ˘â‚¬ĹľÄ‚â€žĂ˘â‚¬Â¦Ă„â€šĂ˘â‚¬Ä…Ä‚ËĂ˘â€šÂ¬Ă‹â€ˇe','bio','bili','budimo','budite','bila','bilo','bile','Ä‚â€žĂ˘â‚¬ĹˇÄ‚ËĂ˘â€šÂ¬ÄąÄľĂ„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚â€ąĂ˘â‚¬Ë‡u','Ä‚â€žĂ˘â‚¬ĹˇÄ‚ËĂ˘â€šÂ¬ÄąÄľĂ„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚â€ąĂ˘â‚¬Ë‡eĂ„â€šĂ˘â‚¬ĹľÄ‚â€žĂ˘â‚¬Â¦Ă„â€šĂ˘â‚¬Ä…Ä‚ËĂ˘â€šÂ¬Ă‹â€ˇ','Ä‚â€žĂ˘â‚¬ĹˇÄ‚ËĂ˘â€šÂ¬ÄąÄľĂ„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚â€ąĂ˘â‚¬Ë‡e','Ä‚â€žĂ˘â‚¬ĹˇÄ‚ËĂ˘â€šÂ¬ÄąÄľĂ„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚â€ąĂ˘â‚¬Ë‡emo','Ä‚â€žĂ˘â‚¬ĹˇÄ‚ËĂ˘â€šÂ¬ÄąÄľĂ„â€šĂ‹ÂÄ‚ËĂ˘â‚¬ĹˇĂ‚Â¬Ä‚â€ąĂ˘â‚¬Ë‡ete','Ă„â€šĂ˘â‚¬ĹľÄ‚â€žĂ˘â‚¬Â¦Ă„â€šĂ˘â‚¬ĹľÄ‚â€žĂ„Äľelim','Ă„â€šĂ˘â‚¬ĹľÄ‚â€žĂ˘â‚¬Â¦Ă„â€šĂ˘â‚¬ĹľÄ‚â€žĂ„ÄľeliĂ„â€šĂ˘â‚¬ĹľÄ‚â€žĂ˘â‚¬Â¦Ă„â€šĂ˘â‚¬Ä…Ä‚ËĂ˘â€šÂ¬Ă‹â€ˇ','Ă„â€šĂ˘â‚¬ĹľÄ‚â€žĂ˘â‚¬Â¦Ă„â€šĂ˘â‚¬ĹľÄ‚â€žĂ„Äľeli','Ă„â€šĂ˘â‚¬ĹľÄ‚â€žĂ˘â‚¬Â¦Ă„â€šĂ˘â‚¬ĹľÄ‚â€žĂ„Äľelimo','Ă„â€šĂ˘â‚¬ĹľÄ‚â€žĂ˘â‚¬Â¦Ă„â€šĂ˘â‚¬ĹľÄ‚â€žĂ„Äľelite','Ă„â€šĂ˘â‚¬ĹľÄ‚â€žĂ˘â‚¬Â¦Ă„â€šĂ˘â‚¬ĹľÄ‚â€žĂ„Äľele','moram','moraĂ„â€šĂ˘â‚¬ĹľÄ‚â€žĂ˘â‚¬Â¦Ă„â€šĂ˘â‚¬Ä…Ä‚ËĂ˘â€šÂ¬Ă‹â€ˇ','mora','moramo','morate','moraju','trebam','trebaĂ„â€šĂ˘â‚¬ĹľÄ‚â€žĂ˘â‚¬Â¦Ă„â€šĂ˘â‚¬Ä…Ä‚ËĂ˘â€šÂ¬Ă‹â€ˇ','treba','trebamo','trebate','trebaju','mogu','moĂ„â€šĂ˘â‚¬ĹľÄ‚â€žĂ˘â‚¬Â¦Ă„â€šĂ˘â‚¬ĹľÄ‚â€žĂ„ÄľeĂ„â€šĂ˘â‚¬ĹľÄ‚â€žĂ˘â‚¬Â¦Ă„â€šĂ˘â‚¬Ä…Ä‚ËĂ˘â€šÂ¬Ă‹â€ˇ','moĂ„â€šĂ˘â‚¬ĹľÄ‚â€žĂ˘â‚¬Â¦Ă„â€šĂ˘â‚¬ĹľÄ‚â€žĂ„Äľe','moĂ„â€šĂ˘â‚¬ĹľÄ‚â€žĂ˘â‚¬Â¦Ă„â€šĂ˘â‚¬ĹľÄ‚â€žĂ„Äľemo','moĂ„â€šĂ˘â‚¬ĹľÄ‚â€žĂ˘â‚¬Â¦Ă„â€šĂ˘â‚¬ĹľÄ‚â€žĂ„Äľete'])
    rezultat = []
    def istakniSlogotvornoR(niz):
    	return re.sub(r'(^|[^aeiou])r($|[^aeiou])',r'\1R\2',niz)

    def imaSamoglasnik(niz):
        if re.search(r'[aeiouR]',istakniSlogotvornoR(niz)) is None:
        	return False
        else:
        	return True

    def transformiraj(pojavnica):
    	for trazi,zamijeni in transformacije:
    		if pojavnica.endswith(trazi):
    			return pojavnica[:-len(trazi)]+zamijeni
    	return pojavnica

    def korjenuj(pojavnica):
    	for pravilo in pravila:
    		dioba=pravilo.match(pojavnica)
    		if dioba is not None:
    			if imaSamoglasnik(dioba.group(1)) and len(dioba.group(1))>1:
    				return dioba.group(1)
    	return pojavnica

    if __name__=='__main__':
    	"""if len(sys.argv)!=3:
    		print ('Usage: python Croatian_stemmer.py input_file output_file')
    		print ('input_file should be an utf8-encoded text file which is then tokenized, stemmed and written in the output_file in a tab-separated fashion.')
    		sys.exit(1)"""


    	pravila=[re.compile(r'^('+osnova+')('+nastavak+r')$') for osnova, nastavak in [e.strip().split(' ') for e in open('rules.txt')]]
    	transformacije=[e.split('\t') for e in open('transformations.txt')]
    	for token in words:
    		if token.lower() in stop:
    			rezultat.append((token.lower()))
    			continue
    		rezultat.append(korjenuj(transformiraj(token.lower())))
    return rezultat
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *








def Megadoc_Train_Prior_Builder_VocabulryLen():
    megadoc_model = {}
    train_model = {}
    get_prior = {}
    prior_brojac = 0

    vocabulary = set()

   # zanrovi = ("Action", "Sci-Fi", "War", "Sport", "Romance", "Western", "Crime", "Horror")
    for genre in zanrovi:
        megadoc_model[genre] = {}
        train_model[genre] =[]
        get_prior[genre] = 0

    dozvoljeni_formati =("sub","srt","txt")

    with open("filmovi_info_train.txt") as f:
        content = f.readlines()

    broj = 0

    result =[]
    for line in content:
        prior_brojac = prior_brojac + 1
        temp = line.split('*')  #temp[0] ---> naslov filma |  temp[1] ---> path titlova | temp[2] ---> zanrovi
        for genre in zanrovi:
            if genre in temp[2]:
                #******  skretanje za PRIOR ******
                get_prior[genre] = get_prior[genre] + 1
                #-------------------
                path ="train/" + temp[1]
                if(path[-3:] in dozvoljeni_formati):
                    #try:
                        broj = broj + 1
                        print(broj)
                        file = open(path,'r')
                        titlovi = file.read()
                        rijeci = re.findall("[^\W\d_]+",titlovi)

                        train_model[genre].append({})

                      #  rijeci = Stemmy(rijeci)


                        for w in rijeci:
                            w=w.lower()
                            #******  skretanje za MEGADOC MODEL ******
                            if w in megadoc_model[genre]:
                                megadoc_model[genre][w] = megadoc_model[genre][w] + 1
                            else:
                                megadoc_model[genre][w] = 1
                            #*****       -------       ********


                            #          --TRAIN MODEL
                            if w in train_model[genre][-1].keys():
                                train_model[genre][-1][w] = train_model[genre][-1][w] + 1
                            else:
                                train_model[genre][-1][w] = 1
                            #****                      *****
                            vocabulary.add(w)




                   # except:
                        #print("mini fail")


    for genre in zanrovi:
        get_prior[genre] = get_prior[genre] / prior_brojac



    #for p in za_pregled:
        #p.append(p[1]/total)
    return megadoc_model,train_model,get_prior,len(vocabulary)


def Likeliehood(megadoc,words,vocabulary_len):
    likelihood = {}
    for genre in zanrovi:
        likelihood[genre] = {}

    for genre in zanrovi:
        for word in words:
            if word in megadoc[genre].keys():
                likelihood[genre][word] = megadoc[genre][word]  + 1 / (len(megadoc[genre].keys()) + vocabulary_len)
            else:
                1 / (len(megadoc[genre].keys()) + vocabulary_len)
    return likelihood

def Posterior(prior,megadoc, titl,vocab_len):
    posterior = {}
    #titl = Stemmy(titl)
    likelihood = Likeliehood(megadoc,titl,vocabulary_len)
    for genre in zanrovi:
        posterior[genre] = math.log(prior[genre]);
        for word in titl:
            word=word.lower()
            if(word in likelihood[genre].keys()):
                posterior[genre] = posterior[genre] + math.log(likelihood[genre][word])
    return posterior


def PraviPodatci(mega_doc,Prior,vocabulary_len):

    posterior_title = {}
    dozvoljeni_formati =("sub","srt","txt")
    with open("filmovi_info.txt") as f:
        content = f.readlines()

    for line in content:
        temp = line.split('*')  #temp[0] ---> naslov filma |  temp[1] ---> path titlova | temp[2] ---> zanrovi
        path ="test/" + temp[1]
        if(path[-3:] in dozvoljeni_formati):
            #print("!!!!")
            file = open(path,'r')
            titlovi = file.read()
            rijeci = re.findall("[^\W\d_]+",titlovi)
            #rijeci = Stemmy(rijeci)


            kljuc = temp[0]+"*"+temp[2][:-2]
            posterior_title[kljuc] = Posterior(Prior,mega_doc,rijeci,vocabulary_len)



            """print("*****      " + temp[0] + "      *******"  + "  ---> "+ temp[2])
            for genre in posterior_title[temp[0]]:
                print(genre + ":   " + str(round(posterior_title[temp[0]][genre],3)))
            """
    return posterior_title



# PROGRAM START


zanrovi = ("Action", "Sci-Fi", "War", "Sport", "Romance", "Western", "Crime", "Horror")

megadoc,train,prior,vocabulary_len = Megadoc_Train_Prior_Builder_VocabulryLen()


posterior = PraviPodatci(megadoc,prior,vocabulary_len)

counter = 0
valjani_filmovi = len(posterior.keys())

for kljuc in posterior.keys():
    parts = kljuc.split('*')
    title = parts[0]
    true_genre = parts[1].split(';')

    selected_genre = max(posterior[kljuc], key=posterior[kljuc].get)

    dobar = False
    for g in true_genre:
        if g in zanrovi:
            dobar = True
            break

    if selected_genre in true_genre:
        counter = counter + 1

    print("*****      " + title + "   ******* -->" + ' '.join(true_genre))
    for genre in posterior[kljuc]:
        print(genre + ":   " + str(round(posterior[kljuc][genre],3)))
    print("*  -->" + selected_genre)
    print (counter/valjani_filmovi)
    print()



print("dobaaar")
#for genre in zanrovi:
    #print(genre +  "   "+ str(posterior[genre]))
