A = {1,2,3,4}
B = {1,2,4,5}
#1
print(len(A))
print(len(B))
#2
print("Những phần tử giống nhau trong 2 set: " , A & B)
#3
print(A|B)
#4

def check(n,A,B):
    if n in (A & B):
        return 3
    elif n in A:
        return 1
    elif n in B:
        return 2
    else:
        return -1
# n = int(input("Nhập n bất kì: "))
# print(check(n, A, B))

#5
print("Những số có ở set 1 mà không có ở set 2:", (A-B))
print("Những số có ở set 2 mà không có ở set 1:", (B-A))

#6
def XoaPhanGiao(A, B):
    return ((A|B)-(A&B))
print(XoaPhanGiao(A,B))


