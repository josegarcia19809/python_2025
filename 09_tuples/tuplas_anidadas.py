nums = (1, 2, 3, (4, 5), 6, 7)
print(nums)

print("-" * 100)
for num in nums:
    print(num)

print("-" * 100)
print(nums[0])
print(nums[2])
print(nums[3])

print("-" * 100)
print(nums[3][0])  # 4
print(nums[3][1])  # 5

print("-" * 100)
print(nums[1:4])
