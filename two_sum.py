def two_sum(nums, target):
    i = len(nums)
    new_nums = []
    for x in range(0, i):
        if target > x:
            for y in range(x+1, i):
                if target > y:
                    if nums[x]+nums[y] == target:
                        tuple1 = (nums[x], nums[y])
                        new_nums.append(tuple1)
    return new_nums


m =[1,2,3,4,5,6,7,8]
n = two_sum(m,10)

print(n)


class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums) - i -1):
                if nums[i] + nums[j + i + 1] == target:
                    return [i,j + i + 1]



