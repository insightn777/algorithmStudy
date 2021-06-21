def solve(n, data: str) -> str:
    data = data.split()
    stack = []
    result = [ '0' for i in range(n) ]
    while n:
        tower = int(data[n-1])
        while stack and stack[-1]['value'] <= tower:
            result[stack[-1]['index']] = str(n)
            stack.pop()
        stack.append({'index': n-1, 'value': tower})
        n -= 1

    return ' '.join(result)



if __name__ == '__main__':
    n = int(input())
    print(solve(n, input()))
