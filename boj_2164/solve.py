from collections import deque

def solve(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2

    d = deque([ i for i in range(0, n+1, 2) ])
    
    if (n % 2 == 0):
        d.popleft()

    card: int
    while len(d) > 0:
        card = d.popleft()
        d.rotate(-1)

    return card

if __name__ == '__main__':
    n = int(input())
    print(solve(n))
