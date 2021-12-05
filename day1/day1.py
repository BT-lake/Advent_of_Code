with open('day1_input') as day1_input:
    depths = day1_input.read().splitlines()
    day1_input.close()

count = 0

for x in range(0, len(depths)-1):
    if depths[x + 1] > depths[x]:
        count += 1

print(count)