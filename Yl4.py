#Kirjuta programm, mis leiab kahest kasutaja poolt sisestatud arvust miinimumi (ära kasuta min funktsiooni). 
# (muutuja - variable, tingimus - condition, if-lause - if statement)

n = int(input('Kirjuta siia üks arv: '))
n1 = int(input('Kirjuta siia veel üks arv: '))

if n < n1:
    print('Väiksem arv on:', n)
elif n == n1:
    print('Arvud on võrdsed.')
else: 
    print('Väiksem arv on:', n1)


