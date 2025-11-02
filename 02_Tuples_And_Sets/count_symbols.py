nums: tuple = tuple([float(x) for x in input().split()])
data: dict = {}

for i in nums:
    data[i] = nums.count(i)

for key, value in data.items():
    print(f'{key:.1f} - {value} times')