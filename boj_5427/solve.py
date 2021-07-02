from collections import deque


def solve(col_cnt: int, row_cnt: int, field) -> int:
    deq = deque()
    sg_stack = []
    success = 0

    visit_field = [[0 for col in range(col_cnt)] for row in range(row_cnt)]

    for r in range(row_cnt):
        for c in range(col_cnt):
            spot = field[r][c]
            if spot == '*':
                deq.append((True, r, c, 0))
            elif spot == '@':
                sg = (False, r, c, 1)
                deq.append(sg)
                visit_field[r][c] = 1
                sg_stack.append(0)

    del spot

    while len(deq) > 0 and sg_stack and success == 0:
        flag, row, col, sec = deq.popleft()
        if flag:
            visit_spot = [
                (row - 1, col),
                (row + 1, col),
                (row, col + 1),
                (row, col - 1)
            ]

            for r, c in visit_spot:
                if r >= row_cnt or c >= col_cnt or c < 0 or r < 0:
                    continue
                elif field[r][c] == '.' or field[r][c] == '@':
                    field[r][c] = '*'
                    deq.append((True, r, c, 0))

        else:
            sg_stack.pop()
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
                elif field[r][c] == '.' and visit_field[r][c] == 0:
                    visit_field[r][c] = 1
                    deq.append((False, r, c, s))
                    sg_stack.append(0)

    return 'IMPOSSIBLE' if success == 0 else success


if __name__ == '__main__':
    cases = int(input())
    for case in range(cases):
        input_c, input_r = input().split()
        ans = solve(int(input_c), int(input_r), [list(input()) for r in range(int(input_r))])
        print(ans)
