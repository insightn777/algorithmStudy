from queue import Queue

def solve(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2

    q = Queue()
    for i in range(0, n+1, 2):
        q.put_nowait(i)
    
    if (n % 2 == 0):
        q.get_nowait()

    card: int
    while q:
        card = q.get_nowait()
        if q.empty():
            return card
        else:
            q.put_nowait(q.get_nowait())


if __name__ == '__main__':
    n = int(input())
    print(solve(n))
