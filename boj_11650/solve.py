if __name__ == '__main__':
    n = int(input())
    coordinates = []    
    for i in range(n):
        [x, y] = input().split()
        coordinates.append((int(x), int(y)))

    for item in sorted(coordinates):
        print(f'{item[0]} {item[1]}')
