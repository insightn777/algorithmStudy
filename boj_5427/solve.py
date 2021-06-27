import itertools
from collections import deque


def solve(col_cnt: int, row_cnt: int, field) -> int:
    deq = deque()
    sg_deq = deque()
    sg: tuple
    success = 0

    visit_field = [ [0] * col_cnt ] * row_cnt
    
    for r in range(row_cnt):
        for c in range(col_cnt):
            spot = field[r][c]
            if spot == '*':
                deq.append((True, r, c, 0))
            elif spot == '@':
                sg = (False, r, c, 1)

    deq.append(sg)
    visit_field[sg[0]][sg[1]] = 1
    sg_deq.append(0)

    while len(deq) > 0 and len(sg_deq):
        flag, row, col, sec = deq.popleft()
        if flag:
            visit_spot = [
                (row - 1, col), 
                (row + 1, col), 
                (row, col + 1), 
                (row, col - 1)
            ]

            for r, c in visit_spot:
                if r >= row_cnt or c <= col_cnt or c < 0 or r < 0:
                    continue
                elif field[r][c] == '.' or field[r][c] == '@':
                    field[r][c] == '*'
                    deq.append((True, r, c, 0))
            
        else:
            sg_deq.popleft()
            visit_spot = [
                (row - 1, col, sec + 1), 
                (row + 1, col, sec + 1), 
                (row, col + 1, sec + 1), 
                (row, col - 1, sec + 1)
            ]

            for r, c, s in visit_spot:
                if r >= row_cnt or c <= col_cnt or c < 0 or r < 0:
                    success = s
                    deq.clear()
                    break
                elif field[r][c] == '.' and visit_field[spot] == 0:
                    visit_field[spot] = 1
                    deq.appned((False, r, c, s))
                    sg_deq.append(0)

    return 'IMPOSSIBLE' if success == 0 else success


if __name__ == '__main__':
    n = input()
    case = int(n)
    for i in range(case):
        c, r = input().split()
        col = int(c)
        row = int(r)
        field = [ list(input()) for i in range(row) ]
        ans = solve(col, row, field)
        print(ans)
