nums = [int(i) for i in input("Введите строку чисел\n").split()]
new_nums = []
nums_len = len(nums)
for i in range(nums_len):
    if i == 0:
        num = nums[-1] + nums[i+1]
    elif i == (nums_len - 1):
        num = nums[i-1] + nums[0]
    else:
        num = nums[i-1] + nums[i+1]
    new_nums.append(num)
print(" ".join(map(str, new_nums)))


