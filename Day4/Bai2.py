import random
n = int(input("n = "))

lst_sv = {}
mk = ["CNTT","KHMT", "KTPM", "HTTT"]
msv = 2021600001
for i in range(n):
    lst_c = {}
    lst_c["Username"] = str(msv)
    lst_c["Password"] = random.choice(mk) + str(msv)
    lst_sv["Account"+str(i+1)] = lst_c
    msv += 1

print(lst_sv)

