def remove_duplicate(list1):
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2 
list1 = list(map(int,input().split()))
result = remove_duplicate(list1)
print(result)