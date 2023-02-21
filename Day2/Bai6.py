
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
tc = 0 
tl = 0
for i in lst:
    if i % 2 == 0:
        tc += i
    else:
        tl += 1
if(tc > tl):
    print("even")
elif(tc < tl):
    print("odd")
else:
    print("equal")

#Cách 2: Nhập các phần tử trên cùng một dòng
lst = [int(i) for i in input().split(' ')]
