###yl11 Kirjuta programm, mis küsib kasutajalt sisendina stringi.
# Eemalda selle sisendi algusest ja lõpust tühikud.
#String peab vastama tingimustele, et selles on vähemalt seitse sümbolit ja et sümbolite arv on paarituarvuline.
#Väljasta selle stringi kolm keskmist sümbolit.
#(stringi meetodid, list)

write = input('Kirjuta siia tekst koos sümbolitega: ')

write = write.strip()

print(write)

if len(write) < 7 or len(write) % 2 == 0:
    print('Sisestatud tekstis peab olema vähemalt 7 sümbolit.')
else:
    i = int(len(write) / 2)
    print(write[i-1 : i+2])