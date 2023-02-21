#Bai 4
def S1(n):
    S = 0
    for i in range(n+1):
        S += i
    return S
def S2(n):
    S = 0
    for i in range(1,n+1):
        S += 1/(2*n+1)
    return S
def S3(n):
    S = 0
    for i in range(1,n+1):
        S += i/(i+1)
    return S
def S4(n, x):
    S = 0
    for i in range(1, n+1):
        S += x**i
    return S

#1,2,3,4
n = int(input("n = "))
print("S1 =", S1(n))
print("S2 =", S2(n))
print("S3 = ", S3(n))
x = float(input("x = "))
print("S4 =", S4(n,x))

#5  Viết chương trình giải và biện luận phương trình bậc nhất ax + b = 0
a, b = (int(i) for i in input("Moi nhap hệ số a, b của pt: ").split(" "))
if (a == 0):
    print("Phương trình không phải phương trình bậc nhất")
else:
    x = -b/a
    print("Nghiệm của phương trình là:",x )

#6
def tim_n():
    S = 0
    n = 0
    while(S <= 10000):
        n += 1
        S += n
    return n
print(tim_n())

#7
for i in range(ord('A'), ord('Z')+1):
    print(chr(i))

#8
import math
def snt(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        i = 2
        while(i <= math.sqrt(n)):
            if n % i == 0:
                return False
            i += 1
    return True

n = int(input("n = "))
if(snt(n)):
    print("n là SNT")
else: 
    print("n không là SNT")

