def get_even(nums):
    even_nums = []
    for i in nums:
        if i % 2 == 0:
           even_nums.append(i)
    return even_nums
def get_prime(nums):
    prime_nums = []

    for num in nums:
        if num <= 1:
            continue

        for i in range(2, num):
            if num % i == 0:
                break
        else:
            prime_nums.append(num)

    return prime_nums
def analyze(nums):
    even_nums =  get_even(nums) 
    prime_nums = get_prime(nums)
    print("the even numbers is: ",even_nums)
    print("the prime numbers is: ",prime_nums)

nums = list(map(int,input().split()))
analyze(nums)
