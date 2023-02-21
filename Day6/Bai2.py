def BCNN(a : int,b : int):
    def UCLN(a: int, b: int):
       if b == 0:
           return a
       else:
           return UCLN(b, a%b)
    return (a*b)/UCLN(a,b)

print(BCNN(4,6)) 