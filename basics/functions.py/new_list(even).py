def get_even(nums):
    new_list = []
    for i in nums:
        if i %2 == 0:
           new_list.append(i)
    return new_list
nums = list(map(int,input().split()))
result = get_even(nums)
print(result) 