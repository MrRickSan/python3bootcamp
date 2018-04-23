def max_magnitude(nums):
    return max(abs(num) for num in nums)


print(max_magnitude([300, 20, -900]))