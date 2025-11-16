clothes: list[int] = [int(x) for x in input().split()]
rack_capacity: int = int(input())
sum_rack: int = 0
rack_count = 1

while clothes:
    temp: int = clothes.pop()

    if rack_capacity < sum_rack + temp:
        rack_count += 1
        sum_rack = 0

    sum_rack += temp

print(rack_count)
