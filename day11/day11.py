import copy

def should_change_occupied(i, j):
    if i - 1 >= 0:
        if plane[i - 1][j] == 'L':
            return False
    if i + 1 < len(plane):
        if plane[i + 1][j] == 'L':
            return False
    if j - 1 >= 0:
        if plane[i][j - 1] == 'L':
            return False
    if j + 1 < len(plane[i]):
        if plane[i][j + 1] == 'L':
            return False
    return True

def should_change_nonoccupied(i, j):
    if i - 1 >= 0:
        if plane[i - 1][j] == '#':
            return False
    if i + 1 < len(plane):
        if plane[i + 1][j] == '#':
            return False
    if j - 1 >= 0:
        if plane[i][j - 1] == '#':
            return False
    if j + 1 < len(plane[i]):
        if plane[i][j + 1] == '#':
            return False
    return True


def rules(i, j):
    if plane[i][j] == '#':
        if(should_change_occupied(i, j)):
            curr[i][j] = 'L'
            return True
    elif plane[i][j] == 'L':
        if(should_change_nonoccupied(i, j)):
            curr[i][j] = '#'
            return True
    return False



in_file = open('C:\\Users\\Lea\\Desktop\\Code\\aoc\\day11\\input.txt')
lines = in_file.readlines()
plane = []

for line in lines:
    plane.append(list(line.strip('\n')))

curr = copy.deepcopy(plane)

for _ in range(2):
    for i in range(len(plane)):
        for j in range(len(plane[i])):
            rules(i,j)
    plane = copy.deepcopy(curr)

for row in curr:
    print(row)