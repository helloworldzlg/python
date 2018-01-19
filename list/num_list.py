#!/usr/bin/env python

nums = range(0, 10)
print(nums)

print(max(nums))
print(min(nums))
print(sum(nums))

scores = [value**2 for value in range(1, 11)]
print(scores)

print(nums[1:3])
print(nums[1:7])

t_num = nums
print(nums)
print(t_num)

nums[0] = 100
print(nums)
print(t_num)

nums_2 = nums[:]
print(nums)
print(nums_2)

nums[0] = 0
print(nums)
print(nums_2)
