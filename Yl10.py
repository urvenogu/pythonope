###Kirjuta programm, mis küsib kasutajalt nime, tervitab teda nimepidi, küsib kasutajalt elukoha, 
# kui elukoht on Saaremaa, siis väljastab mingi kommentaari, 
# küsib kasutajalt vanuse, kui vanus on väiksem kui 18, siis ütleb, et kasutaja on liiga noor, 
# et autot juhtida, kui vanus on 18, siis õnnitleb täisealiseks saamise puhul, 
# kui kasutaja on vanem kui 18, siis ütleb, et kasutaja võib autot juhtida. (sõne - string)

name = input('Kirjuta oma nimi: ')
print('Tere, ', name,'!')

living = input('Kirjuta oma elukoht: ')
if living == 'Saaremaa':
    print('Sul on väga lahe elukoht!')
else:
    print('Koli Saaremaale!')

age = int(input('Kui vana Sa oled?. Palun sisesta enda vanus siia: '))

if age >= 18:
    print('Palju õnne! Oled täisealine ja võid autot juhtida!')
elif age < 18:
    print('Pead veel ootama täisealiseks saamiseni.')