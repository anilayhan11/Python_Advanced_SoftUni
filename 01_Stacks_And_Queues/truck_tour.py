from collections import deque

stations_count: int = int(input())
stations: deque = deque()

for _ in range(stations_count):
    fuel_curr, distance_curr = map(int, input().split())
    stations.append({'fuel': fuel_curr, 'dist': distance_curr})

start_index: int = 0
stations_reached: int = 0

while stations_reached < stations_count:
    fuel = 0
    for i in range(stations_count):
        fuel += stations[i]['fuel']
        dist = stations[i]['dist']

        if fuel < dist:
            stations.rotate(-1)
            start_index += 1
            stations_reached = 0
            break

        fuel -= dist
        stations_reached += 1

print(start_index)


