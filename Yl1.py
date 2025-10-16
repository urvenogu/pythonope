# Kirjuta programm, mis teisendab kasutaja poolt kroonides sisestatud summa eurodesse ja väljastab ümardatud tulemuse. (round)
# küsime kasutajalt summa kroonides
# teisendame eurodesse 
# väljastame tulemuse

eek = int(input('Sisesta summa kroonides: '))
eur = round(eek / 15.6466, 2)
print(eur)

