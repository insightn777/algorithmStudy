def solve(_input: str) -> str:
    left = []
    right = []

    for i in _input:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)

    result = left + right[::-1]

    return ''.join(result)


if __name__ == '__main__':
    n = input()
    for i in range(int(n)):
        print(solve(input()))
