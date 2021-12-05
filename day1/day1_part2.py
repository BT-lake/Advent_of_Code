with open('day1_input') as data:
    depths = data.read().splitlines()
    data.close()

count = 0

for x in range(0, len(depths)-3):
    print((int(depths[x]) + int(depths[x+1]) + int(depths[x+2])), (int(depths[x+1]) + int(depths[x+2]) + int(depths[x+3])))
    if (int(depths[x]) + int(depths[x+1]) + int(depths[x+2])) < (int(depths[x+1]) + int(depths[x+2]) + int(depths[x+3])):
        count += 1

print(count)