###Kolmnurki liigitatakse külgede pikkuse järgi erikülgseteks, võrdhaarseteks ja võrdkülgseteks. 
# Kirjutada programm, mis küsib kasutajalt kolme külje pikkused ning väljastab vastusena kolmnurga liigi. 
# Lisaks tuleb kontrollida, kas etteantud küljepikkustega kolmnurk saab üldse eksisteerida. 
# Külje pikkused ei pea olema täisarvud. (ujukomaarv - float)

a = float(input("Sisesta kolmnurga ühe külje pikkus: "))
b = float(input("Sisesta kolmnurga teise külje pikkus: "))
c = float(input("Sisesta kolmnurga kolmanda külje pikkus: "))  

if a + b < c or a + c < b or b + c < a:
    print('Kolmnurka ei saa eksisteerida')
    quit()

if a == b and b == c:
    print('Kolmnurk on võrdkülgne')
elif a != b and b != c and a != c:
    print('Kolmnurk on erikülgne')
else:
    print('Kolmnurk on võrdhaarne')

    

