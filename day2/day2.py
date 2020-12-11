in_file = open('C:\\Users\\Lea\\Desktop\\Code\\aoc\\day2\\input.txt')
filelines = in_file.readlines()
nums = []
num_set = set()

for line in filelines:
    nums.append(line)

cnt = 0

for num in nums:
    arr = num.split('-')
    first_ind = arr[0]
    arr2 = arr[1].split(' ')
    second_ind = arr2[0]
    letter = arr2[1].strip(':')
    word = arr2[2].strip('\n')
    char_inds = [pos for pos, char in enumerate(word) if char == letter]
    if(len(char_inds) < int(first_ind) or len(char_inds) > int(second_ind)):
        cnt += 1

print(len(nums) - cnt)

cnt = 0

for num in nums:
    arr = num.split('-')
    first_ind = arr[0]
    arr2 = arr[1].split(' ')
    second_ind = arr2[0]
    letter = arr2[1].strip(':')
    word = arr2[2].strip('\n')
    f = word[int(first_ind)-1] == letter
    s = word[int(second_ind)-1] == letter
    cnt += (f ^ s)

print(cnt)
    
    
