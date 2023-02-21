#Bài 1
def xeploai(diem):
    if(diem >= 8.00):
        return "Giỏi"
    elif(diem >= 7):
        return "Khá"
    elif(diem >= 5):
        return "TB"
    else:
        return "Yếu"
    
diem = float(input("Moi nhap diem tong ket: "))
print("Xếp loại của học sinh:", xeploai(diem))

#Bài 2
import math
def F(n):
    F = 0
    if (n % 2 == 0):
        for i in range(0, n+1):
            F += 1/(2**i)
    else:
        F = math.sqrt(n**2 + 1)
    return F

n = int(input("n = "))
print("Gia tri cua F =", F(n))