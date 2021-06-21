def solve(data):
    n, k = map(int, data.split())

    sequence = list(range(1, n+1))

    idx = 0
    ans = []

    while sequence:
        idx = ((idx + k - 1) % len(sequence))
        ans.append(str(sequence.pop(idx)))

    return f'<{", ".join(ans)}>'


if __name__ == '__main__':
    n = input()

    ans = solve(n)
    print(ans)
