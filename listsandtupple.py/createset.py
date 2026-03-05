a ={5, 10, 15, 20}
b=[]
for i in a:
    if i not in b:
        b.append(i)
b=sorted(b) 
print(b)
print(b[0])
print(b[-1])
print(len(b))