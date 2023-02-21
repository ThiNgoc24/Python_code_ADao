
kq = []
chose = 'YES'
while (chose == 'YES'):
    n = int(input("n = "))
    k = int(input("k = "))
    error = 0
    while(n <= k or n <= 0 or k <= 0):
        print("Vui lòng nhâp lại n > k, n, k nguyên dương")
        n = int(input("n = "))
        k = int(input("k = "))
        error += 1


    while(n > 0):
        print("Moi nhap mot so nguyen duong bat ki trong doan [1, min(n,k)]: ")
        m = int(input())
        while(m < 1 or m > min(n,k)):
            print("Vui long nhap lai: ")
            m = int(input())
            error += 1
        n = n - m
    #Làm nào để biết ai thua trước?
    print("Bạn có muốn tiếp tục chơi không?")
    chose = input("YES/NO: ")
    while(chose not in ['YES', 'NO']):
        print("Vui lòng nhập đúng cú pháp: ")
        chose = input("YES/NO: ")
        error += 1

    