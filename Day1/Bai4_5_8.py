#Bài 4
print("Mời nhập thông tin: ")
age = int(input("age: "))
gender = input("gender: ")
fullname = input("Fullname: ")
print(" Tên: {}\n Tuổi: {}\n Giới tính: {}".format(fullname, age, gender))

#Bai5
import sys
print(sys.version)

#Bai8
def min(n):
    c2 = n // 3 #Chia lấy phần nguyên
    c1 = n - 2*c2
    return abs(c1-c2)

n = int(input("n = "))
print("Độ lệch số tờ 2 loại tiền:", min(n))
