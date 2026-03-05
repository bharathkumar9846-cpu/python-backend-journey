a = input("enter a sentence")
a=a.split()
freq = {}
for i in a:
    if i in freq:
        freq[i] += 1 
    else:
        freq[i] = 1
    

for key, value in freq.items():
    print(key, ":" , value)