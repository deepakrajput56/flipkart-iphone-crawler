a=[8,2,3,4,4,1,2,5,6,6,11,7]
b={}
for i in a:
    counter = 0
    for j in a:
        if i==j:
            counter+=1

    b[i]=[counter]
print(b)
max_occurrence = max(b.values())
max_keys = [key for key, value in b.items() if value == max_occurrence]
print(max_keys, max_occurrence)










