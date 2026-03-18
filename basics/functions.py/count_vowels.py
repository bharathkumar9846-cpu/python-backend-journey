def count_vowels(a):
    count = 0
    for i in a:
        if i in "aeiou" and i.isalpha():
           count += 1
    return count
a = str(input("enter a text"))
a= a.lower()
result=count_vowels(a)
print(result)