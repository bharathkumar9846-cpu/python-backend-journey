def sum_evennums(a):
    total = 0
    for i in a:
        if i %2 == 0:
            total = total+i
    print(total)
a = list(map(int,input().split()))
sum_evennums(a)