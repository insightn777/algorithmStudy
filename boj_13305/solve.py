def solve(cities: int, distance: str, price: str) -> str:
    distance = [ int(i) for i in distance.split() ]
    price = [ int(i) for i in price.split() ]
    result = 0
    cheapest_price = 1000000000
    for i in range(cities - 1):
        cheapest_price = price[i] if price[i] < cheapest_price else cheapest_price
        result += distance[i] * cheapest_price
    return str(result)


if __name__ == '__main__':
    cities = int(input())
    distance = input()
    price = input()
    print(solve(cities, distance, price))
