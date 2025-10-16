#Kirjuta programm, mis küsib kasutajalt täisarvu n vahemikus 1-9. 
# Arvuta n + nn + nnn väärtus ja väljasta see. 
# (Näiteks kui kasutaja sisestab 2, siis on vaja väljastada tulemus 2 + 	22 + 222 = 246). 
# Ära kasuta korrutamistehet. Ülesanne on lahendatav ainult liitmise operaatorit kasuades.

n = input('Kirjuta täisarv vahemikus 1-9: ')
n1 = int(n + n)
n2 = int(n + n + n)

n = int(n)

n3 = n + n1 + n2

print((n), '+', (n1), '+', (n2), '=', n3)






