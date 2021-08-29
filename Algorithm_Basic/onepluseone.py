def opo(nums, target):
    n = len(nums)
    ave = target // 2
    nums.sort()
    for index in range(n):
        if nums[index] <= ave and nums[index+1] >= ave:
            for i in range(index+1):
                for j in range(index+1, n):
                    if nums[i] + nums[j] == target:
                        return [i,j]

nums = [3,2,4]
target = 6
print(opo(nums, target))