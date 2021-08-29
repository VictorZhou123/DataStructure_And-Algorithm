def twoSum(numbers, target):
    n = len(numbers)
    for i in range(n):
        val = target - numbers[i]
        left = i + 1
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if numbers[mid] == val:
                return [i,mid]
            elif numbers[mid] > val:
                right = mid - 1
            else:
                left = mid + 1

numbers = [1,2,4,6,10]
target = 8
print(twoSum(numbers, target))