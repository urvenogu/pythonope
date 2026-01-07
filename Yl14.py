### Kirjuta programm, mis küsib kasutajalt failinime kujul “failinimi.ext” 
# (ext - extension - faili laiend) ja prindib välja laiendi (“ext”). (str.split)

filename = input('Kirjuta failinimi kujul näiteks failinimi.ext: ')
extend = filename.split('.')
result = extend[-1]
print('Faili laiend on', result + '.')
