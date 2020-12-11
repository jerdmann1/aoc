in_file = open('C:\\Users\\Lea\\Desktop\\Code\\aoc\\day3\\input.txt')
lines = in_file.readlines()
slope = []
for line in lines:
   slope.append(line.strip('\n'))

cnt = 0
ind = 0
for line in slope:
    if(line[ind % len(line)] == '#'):
        cnt += 1
    ind += 3

print(cnt)

trees = []
trees.append(cnt)
cnt = ind = 0

for line in slope:
    if(line[ind % len(line)] == '#'):
        cnt += 1
    ind += 1
trees.append(cnt)
cnt = ind = 0
for line in slope:
    if(line[ind % len(line)] == '#'):
        cnt += 1
    ind += 5
trees.append(cnt)
cnt = ind = 0
for line in slope:
    if(line[ind % len(line)] == '#'):
        cnt += 1
    ind += 7
trees.append(cnt)
cnt = ind = 0
for i in range(0, len(slope), 2):
    if(slope[i][ind % len(line)] == '#'):
        cnt += 1
    ind += 1
trees.append(cnt)
res = 1
for num in trees:
    res *= num
print(res)


