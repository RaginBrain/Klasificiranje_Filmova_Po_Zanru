Koraci

**********************************
1. P R I K U P LJ A NJ E       I N F O R M A C I J A

u skripti       "spajanje_na_api_za_filmove.py" u kodu mo�ete unijeti [100 000 - 999 999] interval gdje je ozna�eno komentarom.
pretra�uju se ID-evi te se pogo�eni ID-evi spremaju u 
"Lista_Filmova.txt"
Preporu�eno je paralelno pokrenuti skriptu, pa se dobije vi�e datoteka koje �e se tako�er paralelno obra�ivati.

**********************************

2.  S K I D A NJ E       T I T L O V A

U datoteci "Skidanje_Titlova" se nalaze skripta/ skripte za skidanje titlova. Ulaz je "Lista_Filmova.txt" s informacijama
Radi ubrzanja procesa skripte se mogu paralelno pokrenuti s odvojenim datekama ulaza i izlaza.
U skripti "Preuzimanje_titlova9.py" su komentarima  to�no nazna�eni ULAZ i IZLAZ.
Titlovi se spremaju u folder "Titlovi" ,  a dobiju se jo� informacije s  naslovom, �anrovima i path-om za svaki film u datoteci "Finalna_lista_filmova.txt"
Skriptu pokrenete i �ekate da skine titlove.
Titlovi se skidaju preko apija od stranice "http://titlovi.com/"
Da bi skidanje titlova radilo trebate imate klju� koji se �alje u zahtjevu, mogu�e da ne bude radio nakon du�eg vremena (o�ujak,2016)


**********************************

3. K L A S I F I K A C I J A              W O R D      D R A F T      K L A S I F I K A T O R

kraj komentara  #ULAZ u kodu unese se path datoteke koja je dobivena iz koraka 2.
Na konzoli �e se ispisati naslov filma i u [ uglatim ] zagradama njegovi pravi �anrovi a nakon toga ---> na �anr koji je word draft klasifikator odabrao
u liniji ispod se ispisuje postotak pogo�enih odabira , a slu�ajevi u kojima se �anr ne mo�e pogoditi (ne obra�ujemo komedije, drame...) ne ulaze u statistiku.

U folderu "zanrovi" se nalaze skupovi specifi�nih rije�i  po kojima se vr�i klasifikacija.
Na�in na koji �e se te rije�i odabrati nije striktno definiran, a un�unkovitost klasifikatora ovisi samo o njima.
Ako �elite mo�ete izmijeniti skup rije�i i testirati to�nost.

Mi smo koristili skriptu  "pred_obrada_pregled_ponavljanja_rijeci_u_zanru.py" koja ispisuje rije� -- broj ponavljanja za uneseni �anr te
empirijski birali neke rije�i koje su nam djelovale karakteristi�no , od tud naziv WORD DRAFT.

**********************************

4. K L A S I F I K A C I J A            N A I V N I       B A Y E S    K L A S I F I K A T O R


Ulaz je finalna_lista za train i finalna_lista  za test filmova iz koraka 2 te TESTNI titlovi iz foldera "test" , te  TRAIN titlovi iz foldera "train".
Princip funkcioniranja naivnog bayesa je opisan u prezentaciji "Naivni_Bayes_ teorija".
Kad se skripta pokrene , na konzoli �e se ispisati  naslov filma   [pravi �anrevi]
ispod naslova pravih �anrova se ispisuje svaki �anr te ocjena za odabir koju je dao NAIVNI BAYES.
Ispod toga se ispisuje odabrani �anr(s najve�om ocjenom, logi�no) Te postotak poga�anja.

Teorijska podloga ovog klasifikatora je u pdf-u "Naivni_Bayes_Theory.pdf"

Vi�e o temi se mo�e na�i na stranici:
https://sites.google.com/site/brankozitko/kolegiji/uopj

**********************************

5. N A � I          R E Z U L T A T I 


Testni skup su nam 1000 titlova tj. filmova.
Kod Bayesa su podjeljeni u train skup (750) i  test (250)

Naivni Bayes daje na testnom skupu samo  15,8% pogodaka,
potrebno je jo� nadograditi osnovi algoritam radi kompleksnosti zadatka ili pristupiti s drugim metodama.

Word Draft -u su svi titlovi dati zajedno(1000)
Word Draft u testiranju s istim titlovima ima 57,1% pogodaka.
Mo�e se nadogra�ivati empirijski mijenjanjem skupa rije�i ili sistema ocijenjvanja.
Potreban je dobar i kvalitetan odabir rije�i koje su specifi�ne za isklju�ivo jedan �anr.


