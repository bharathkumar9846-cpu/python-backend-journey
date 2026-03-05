def check_even(a):
    if a % 2 == 0:
        return True
    return False
a = int(input("Enter Number: "))
result=check_even(a)
print(result)