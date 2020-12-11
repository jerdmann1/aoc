def validate(fields):
    for key, val in fields.items():
        if key == 'byr':
            if int(val) < 1920 or int(val) > 2002:
                return False
        elif key == 'iyr':
            if int(val) < 2010 or int(val) > 2020:
                return False
        elif key == 'eyr':
            if int(val) < 2020 or int(val) > 2030:
                return False
        elif key == 'hgt':
            if val[-2:] == 'cm':
                if(int(val[:-2]) < 150 or int(val[:-2]) > 193):
                    return False
            elif val[-2:] == 'in':
                if(int(val[:-2]) < 59 or int(val[:-2]) > 76):
                    return False
            else:
                return False
        elif key == 'hcl':
            if val[0] != '#':
                return False
            for i in range(1, len(val)):
                if(val[i] not in '0123456789abcdef'):
                    return False
            if len(val) != 7:
                return False
        elif key == 'ecl':
            cols = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
            if val not in cols:
                return False
        elif key == 'pid':
            if len(val) != 9:
                return False
    return True

in_file = open('C:\\Users\\Lea\\Desktop\\Code\\aoc\\day4\\input.txt')
lines = in_file.readlines()

fields = set()

cnt = 0

for line in lines:
    if line != "\n":
        passport = line.split(' ')
        for passport_field in passport:
            label = passport_field.split(':')
            fields.add(label[0])
    else:
        if len(fields) == 8:
            cnt += 1
        elif len(fields) == 7 and 'cid' not in fields:
            cnt += 1
        fields.clear()

if len(fields) == 8:
    cnt += 1
elif len(fields)  == 7 and 'cid' not in fields:
    cnt += 1

print(cnt)

fields = {}
cnt = 0

for line in lines:
    if line != "\n":
        passport = line.split(' ')
        for passport_field in passport:
            label = passport_field.split(':')
            fields[label[0]] = label[1].strip('\n')
    else:
        if len(fields) == 8:
            if(validate(fields)):
                cnt += 1
        elif len(fields) == 7 and 'cid' not in fields:
            if(validate(fields)):
                cnt += 1
        fields.clear()
            
if len(fields) == 8:
    if(validate(fields)):
        print(fields)
        cnt += 1
elif len(fields) == 7 and 'cid' not in fields:
    if(validate(fields)):
        print(fields)
        cnt += 1

print(cnt)