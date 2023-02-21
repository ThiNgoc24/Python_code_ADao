lst = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
result = []
for i in set(lst):
    item = []
    for j in lst:
        if j == i:
            item.append(j)
    result.append(item)

print(result)