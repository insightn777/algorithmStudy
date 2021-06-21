def solve(n, sequence, x):
    n = int(n)
    sequence = [ int(num) for num in sequence.split() ]
    sequence.sort()
    x = int(x)

    left = 0
    right = n - 1
    ans = 0

    while left < right:
        tmp = sequence[left] + sequence[right]
        if tmp == x:
            ans += 1
            left += 1
        elif tmp < x:
            left += 1
        else:
            right -= 1

    return ans


if __name__ == '__main__':
    n = input()
    sequence = input()
    x = input()

    ans = solve(n, sequence, x)
    print(ans)
