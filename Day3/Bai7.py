n = int(input("n = "))
while(n < 1):
    n = int(input("n = "))
lst = [0]*n
for i in range(n):
    lst[i] = i*i

print(lst)