#a
print(len("Welcome To Python World"))
#b
print('We are the so-called "Vikings" from the north.')
#c
s = "Hello World"
print(s[:6])
#e
print(s.upper())
print(s.lower())
#f
s1 = "Welcome To Python World"
print(s1.replace('o','a'))
#g
A = int(input())
B = int(input())
print("Tổng của {} và {} là {}".format(A,B,A+B))
#h
s2 = "The best things in life are free !" #có cách nào để ! ghi liền với Free nó vẫn duyệt cho không??
print("No" if "free" not in s2.split(' ') else "YES")
#i
s3 = 'Python'
s4 = 'is Good'
print(s3 + ' ' + s4)
#k
s5 = "Hello My Name Is PETER"
kq = []
for i in s5:
    if i >= 'a' and i <= 'z':
        i = i.upper()
    elif i >= 'A' and i <= 'Z':
        i = i.lower()
    kq.append(i)
print(''.join(kq))