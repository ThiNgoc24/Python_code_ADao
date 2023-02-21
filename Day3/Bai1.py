n = int(input("n = "))
while(n < 5 or n > 80):
    n = int(input("n = "))

lst = [int(i) for i in input().split(' ')]
#1
def dem_so_lanxh(x,lst):
    dem = 0
    for i in lst:
        if x == i:
            dem += 1
    return dem

x = int(input("x = "))
print("Số lần xuất hiện {} trong dãy số: {}".format(x, dem_so_lanxh(x, lst)))

#2
lst[2:5] = [2,-9,1]
print(lst)

#3
print("Số lớn nhất: {}, Số nhỏ nhất: {}".format(max(lst), min(lst)))

#4
lst[:0] = [1]
print(lst)

#5
def test_lst(lst):
    td = True
    gd = True
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            td = False
        else:
            gd = False
    if(td):
        print("Mảng tăng dần")
    elif (gd):
        print("Mảng giảm dần")
    else:
        print("Mảng không theo thứ tự")

#6
def lst_Fibo(n):
    lst = [0]*n
    lst[0] = lst[1] = 1
    for i in range(2,n):
        lst[i] = lst[i-1] + lst[i-2]
    return lst
print(lst_Fibo(5))

#7
def sort_decrease(lst):
    lst.sort(reverse=True)
    return lst
 #C2: return sorted(lst2, reverse=True)
lst2 = [2, -1, -5, 3, -9, -12, -3, -8]
print(sort_decrease(lst2))
   
#8
def sort_tang(lst):
    return sorted(lst, key=lambda x: abs(x))
print(sort_tang(lst2))
