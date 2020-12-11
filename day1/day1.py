in_file = open('C:\\Users\\Lea\\Desktop\\Code\\aoc\\input.txt')
filelines = in_file.readlines()
nums = []
num_set = set()

for line in filelines:
    nums.append((int(line)))

for num in nums:
    if(2020 - num not in num_set):
        num_set.add(num)
    else:
        print(num * (2020-num))
        break 

for num in nums:
    goal = 2020 - num
    num_set.clear()
    for i in range(len(nums)):
        if(nums[i] != num):
            if(goal - nums[i] not in num_set):
                num_set.add(nums[i])
            else:
                print(num * nums[i] * (goal - nums[i]))
                exit()
