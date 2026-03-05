coords = []
for _ in range(5): 
    point = tuple(map(int, input().split())) 
    coords.append(point) 

freq = {} 
for point in coords: 
    if point in freq: 
        freq[point] += 1 
    else: 
        freq[point] = 1 
result = [] 
for point in freq: 
    if freq[point] == 1: 
       result.append(point)
       
print(result)