from collections import deque

deq = deque()
left = 0
right = 100000
field = [0] * (right + 1)

def solve(subin: int, bro: int) -> int:
    if subin == bro:
        return 0

    deq.append((subin, 1))
    field[subin] = 1

    while True:
        current, sec = deq.popleft()
        visit_spot = [current - 1, current + 1, current * 2]

        for spot in visit_spot:
            if spot == bro:
                return sec

            if spot >= left and spot <= right and field[spot] == 0:
                field[spot] = 1
                deq.append((spot, sec + 1))


if __name__ == '__main__':
    subin, bro = input().split()
    print(solve(int(subin), int(bro)))
