import re
n = int(input("n = "))
lst = [x for x in input().split(', ')]
while len(lst) != n:
    print("Nhập lại: ")
    lst = [x for x in input().split(', ')]
count =  0
for i in lst:
    if len(i) < 6:
        continue
    else:
        ...
    if not re.search("[a-z]", i):
        continue
    elif not re.search("[0-9]", i):
        continue
    elif re.search("[@#$&^,%!()]", i):
        continue
    else:
        pass
    count += 1
print(count)

