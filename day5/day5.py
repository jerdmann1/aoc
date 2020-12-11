in_file = open('C:\\Users\\Lea\\Desktop\\Code\\aoc\\day5\\input.txt')
seats = in_file.readlines()

max_num = -1

for line in seats:
    mult = 64
    row = 0
    for i in range(7):
        if(line[i] == 'B'):
            row += mult
        mult /= 2
    mult = 4
    seat = 0
    for i in range(7, len(line)):
        if(line[i] == 'R'):
            seat += mult
        mult /= 2
    max_num = max(max_num, (row * 8 + seat))

print(max_num)

plane = set()

for line in seats:
    mult = 64
    row = 0
    for i in range(7):
        if(line[i] == 'B'):
            row += mult
        mult /= 2
    mult = 4
    seat = 0
    for i in range(7, len(line)):
        if(line[i] == 'R'):
            seat += mult
        mult /= 2
    plane.add(row * 8 + seat)

for i in range(int(max_num)):
    if (i - 1) in plane and (i + 1) in plane and i not in plane:
        print(i)