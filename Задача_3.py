nums = [int(i) for i in input("Введите строку чисел\n").split()]
new_nums = []
for num in nums:
    if nums.count(num) > 1 and num not in new_nums:
        new_nums.append(num)
for i in new_nums:
    print(i, end=" ")

