import copy

in_file = open('C:\\Users\\Lea\\Desktop\\Code\\aoc\\day7\\input.txt')
lines = in_file.readlines()

relations = {}
cnt = 0

for line in lines:
    bags = line.split(' contain')
    containers = set()
    for bag in bags[1].split(','):
        build = ""
        for splits in bag.split(' '):
           if(not splits.isnumeric()):
               build = ' '.join([build, splits.strip(' \n.')])
        build = build.strip(' ')
        build = build[:-1] if build[-1] == 's' else build
        containers.add(build)
    relations[bags[0][:-1]] = copy.deepcopy(containers)
    containers.clear()

found = set()
new_found = set()
seen = set()
found.add('shiny gold bag')

while True:
    for k,v in relations.items():
        for search in found:
            if search in v and k not in seen:
                new_found.add(k)
                seen.add(k)
    if len(new_found) == 0:
        break
    else:
        cnt += len(new_found)
        found = copy.deepcopy(new_found)
        new_found.clear()

relations.clear()

for line in lines:
    bags = line.split(' contain')
    containers = {}
    for bag in bags[1].split(','):
        build = ""
        num = 0
        for splits in bag.split(' '):
            if(not splits.isnumeric()):
                build = ' '.join([build, splits.strip(' \n.')])
            else:
                num = int(splits)
        build = build.strip(' ')
        build = build[:-1] if build[-1] == 's' else build
        containers[build] = num
    relations[bags[0][:-1]] = copy.deepcopy(containers)
    containers.clear()

found.clear()
new_found.clear()
seen.clear()

found = set()
new_found = set()
seen = set()
found.add('shiny gold bag')

cnt = 0

while True:
    for word in found:
        if word != 'no other bag':
            for k,v in relations[word].items():
                if k not in seen:
                    cnt += v
                    new_found.add(k)
                    seen.add(k)
    if len(new_found) == 0:
        break
    else:
        found = copy.deepcopy(new_found)
        new_found.clear()

print(cnt)
