n = int(input("n = "))
lst = []
for i in range(n):
    a = input().split(' ')
    lst.append(a)
    
lst_diem = []
for i in lst:
    lst_diem.append(float(i[3]))

def search_diemMax(lst):
    for i in lst:
        if i[3] == max(lst_diem):
            return i

def search_top3(lst):
    top3 = []
    for i in range(3):
        for j in lst:
            if float(j[3]) == max(lst_diem):
                top3.append(j)
                lst_diem.remove(float(j[3]))
                break
    return top3

print(search_top3(lst))

#Tại sao không làm được kiểu này?
# def search_diemMax(lst, lst_diem):
#     for i in lst:
#         if i[3] == max(lst_diem):
#             return i

# def search_top3(lst):
#     top3 = []
#     for i in range(3):
#         top3.append(search_diemMax(lst, lst_diem))
#         lst_diem.remove(max(lst_diem))
#     return top3

# print(search_top3(lst))



