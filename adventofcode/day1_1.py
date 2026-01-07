import sys

def count_zero_positions(lines):
    position = 50        
    zero_count = 0       

    for line in lines:
        line = line.strip()
        if not line:
            continue  

        direction = line[0]       
        distance = int(line[1:])   

        if direction == 'L':
            position = (position - distance) % 100
        elif direction == 'R':
            position = (position + distance) % 100
        else:
            raise ValueError(f"Tundmatu suund: {direction}")

        if position == 0:
            zero_count += 1

    return zero_count


if __name__ == "__main__":
    
    lines = sys.stdin.readlines()
    result = count_zero_positions(lines)
    print(result)