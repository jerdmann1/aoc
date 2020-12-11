import copy

in_file = open('C:\\Users\\Lea\\Desktop\\Code\\aoc\\day6\\input.txt')
lines = in_file.readlines()

cnts = 0
yes = set()

for i in range(len(lines)):
    if(lines[i] != '\n'):
        for c in lines[i].strip('\n'):
            if(c not in yes):
                yes.add(c)
    else:
        cnts += len(yes)
        yes.clear()

cnts += len(yes)
yes.clear()

print(cnts)

cnts = 0

yes = {}
curr = 0

for line in lines:
    if line != '\n':
        curr += 1
        for c in line.strip('\n'):
            if c not in yes:
                yes[c] = 1
            else:
                yes[c] += 1
    else:
        for k,v in yes.items():
            if v == curr:
                cnts += 1
        yes.clear()
        curr = 0

for k,v in yes.items():
    if v == curr:
        cnts += 1
yes.clear()
curr = 0

print(cnts)