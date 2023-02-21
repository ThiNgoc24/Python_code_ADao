lst = list(map(int, input().split(' ')))
sum = 0
for i in range(len(lst)):
    if i == 0:
        continue
    if lst[i] % i == 0:
        sum += lst[i]
print(sum)