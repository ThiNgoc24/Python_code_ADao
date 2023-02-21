def demsongay(d,m,y):
    if (m in [1,3,5,7,8,10,12]):
        dem = (31-d) + 1
    elif (m in [4,6,9,11]):
        dem = (30-d) + 1
    elif m == 2:
        if (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)):
            dem = (29-d) + 1
        else:
            dem = (28-d) + 1
    else:
        print("Ngày tháng năm không hợp lệ. Vui lòng nhập lại!")
        return
    tmp = 0
    while(m < 12):
        m += 1
        if m in [1,3,5,7,8,10,12]:
            tmp += 31
        elif (m in [4,6,9,11]):
            tmp += 30
        elif m == 2:
            if (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)):
                tmp += 29
            else:
                tmp += 28
    return dem + tmp

d, m, y = (int(i) for i in input("Mời nhập vào ngày tháng năm bất kì: ").split('/'))
print(demsongay(d,m,y))