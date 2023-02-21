chuoi = input()
dictt = {}
for i in chuoi:
    dem = 0
    for j in chuoi:
        if j == i:
            dem += 1
    dictt[i] = dem
print(dictt)