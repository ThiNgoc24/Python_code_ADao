#Bai6
import math
x = float(input())
Fx = (x**2 + math.exp(x) + math.sin(x)) / math.sqrt(x**2 + 1)
print(Fx)

#Bai7
statusText = input()
print(statusText.strip())

#Bai9
length = 7.8
width = 3.5
print("Area: {}\nPerimeter: {}".format(length*width, (length+width)*2))

#Bai10
s = input()
if 'A' not in s:
    print("Trong chuỗi không tồn tại kí tự 'A'")
else:
    s = s.replace('A', 'a')
    print(s[-1::-1])