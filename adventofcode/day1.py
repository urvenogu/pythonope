f = open('input_txt')
start = 50
password = 0
#lines = [line.strip() for line in f.readlines()]
for line in f.readlines():
    line = line.strip()
    direction = line[0]
    distance = int(line[1:])

    if direction == 'L':
        start = (start - distance) % 100
    else:
        start += distance
    
    print(line + ':', start)




