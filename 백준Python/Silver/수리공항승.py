n, l = map(int, input().split())
locations = list(map(int, input().split()))
locations.sort()

start = locations[0]
end = start + l - 0.5
tape = 1

for location in locations:
    if end >= location:
        continue
    else:
        tape += 1
        end = location + l - 0.5

print(tape)
