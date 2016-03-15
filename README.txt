Koraci

**********************************
1. P R I K U P LJ A NJ E       I N F O R M A C I J A

u skripti       "spajanje_na_api_za_filmove.py" u kodu možete unijeti [100 000 - 999 999] interval gdje je oznaèeno komentarom.
pretražuju se ID-evi te se pogoðeni ID-evi spremaju u 
"Lista_Filmova.txt"
Preporuèeno je paralelno pokrenuti skriptu, pa se dobije više datoteka koje æe se takoðer paralelno obraðivati.

**********************************

2.  S K I D A NJ E       T I T L O V A

U datoteci "Skidanje_Titlova" se nalaze skripta/ skripte za skidanje titlova. Ulaz je "Lista_Filmova.txt" s informacijama
Radi ubrzanja procesa skripte se mogu paralelno pokrenuti s odvojenim datekama ulaza i izlaza.
U skripti "Preuzimanje_titlova9.py" su komentarima  toèno naznaèeni ULAZ i IZLAZ.
Titlovi se spremaju u folder "Titlovi" ,  a dobiju se još informacije s  naslovom, žanrovima i path-om za svaki film u datoteci "Finalna_lista_filmova.txt"
Skriptu pokrenete i èekate da skine titlove.
Titlovi se skidaju preko apija od stranice "http://titlovi.com/"
Da bi skidanje titlova radilo trebate imate kljuè koji se šalje u zahtjevu, moguæe da ne bude radio nakon dužeg vremena (ožujak,2016)


**********************************

3. K L A S I F I K A C I J A              W O R D      D R A F T      K L A S I F I K A T O R

kraj komentara  #ULAZ u kodu unese se path datoteke koja je dobivena iz koraka 2.
Na konzoli æe se ispisati naslov filma i u [ uglatim ] zagradama njegovi pravi žanrovi a nakon toga ---> na žanr koji je word draft klasifikator odabrao
u liniji ispod se ispisuje postotak pogoðenih odabira , a sluèajevi u kojima se žanr ne može pogoditi (ne obraðujemo komedije, drame...) ne ulaze u statistiku.

U folderu "zanrovi" se nalaze skupovi specifiènih rijeèi  po kojima se vrši klasifikacija.
Naèin na koji æe se te rijeèi odabrati nije striktno definiran, a unèunkovitost klasifikatora ovisi samo o njima.
Ako želite možete izmijeniti skup rijeèi i testirati toènost.

Mi smo koristili skriptu  "pred_obrada_pregled_ponavljanja_rijeci_u_zanru.py" koja ispisuje rijeè -- broj ponavljanja za uneseni žanr te
empirijski birali neke rijeèi koje su nam djelovale karakteristièno , od tud naziv WORD DRAFT.

**********************************

4. K L A S I F I K A C I J A            N A I V N I       B A Y E S    K L A S I F I K A T O R


Ulaz je finalna_lista za train i finalna_lista  za test filmova iz koraka 2 te TESTNI titlovi iz foldera "test" , te  TRAIN titlovi iz foldera "train".
Princip funkcioniranja naivnog bayesa je opisan u prezentaciji "Naivni_Bayes_ teorija".
Kad se skripta pokrene , na konzoli æe se ispisati  naslov filma   [pravi žanrevi]
ispod naslova pravih žanrova se ispisuje svaki žanr te ocjena za odabir koju je dao NAIVNI BAYES.
Ispod toga se ispisuje odabrani žanr(s najveæom ocjenom, logièno) Te postotak pogaðanja.

Teorijska podloga ovog klasifikatora je u pdf-u "Naivni_Bayes_Theory.pdf"

Više o temi se može naæi na stranici:
https://sites.google.com/site/brankozitko/kolegiji/uopj

**********************************

5. N A Š I          R E Z U L T A T I 


Testni skup su nam 1000 titlova tj. filmova.
Kod Bayesa su podjeljeni u train skup (750) i  test (250)

Naivni Bayes daje na testnom skupu samo  15,8% pogodaka,
potrebno je još nadograditi osnovi algoritam radi kompleksnosti zadatka ili pristupiti s drugim metodama.

Word Draft -u su svi titlovi dati zajedno(1000)
Word Draft u testiranju s istim titlovima ima 57,1% pogodaka.
Može se nadograðivati empirijski mijenjanjem skupa rijeèi ili sistema ocijenjvanja.
Potreban je dobar i kvalitetan odabir rijeèi koje su specifiène za iskljuèivo jedan žanr.


