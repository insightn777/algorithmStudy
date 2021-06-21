"""
n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다. 
ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다. 
자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수열의 크기 n이 주어진다. 다음 줄에는 수열에 포함되는 수가 주어진다. 셋째 줄에는 x가 주어진다. (1 ≤ n ≤ 100000, 1 ≤ x ≤ 2000000)

input ex)
9
5 12 7 10 9 1 2 3 11
13

output ex)
3
"""
from solve import solve
test_data = [{
    'n': '9',
    'sequence': '5 12 7 10 9 1 2 3 11',
    'x': '13',
    'ans': 3
}]

if __name__ == '__main__':   
    for data in test_data:
        if data.pop('ans') == solve(**data):
            print('success')
        else:
            print(data)