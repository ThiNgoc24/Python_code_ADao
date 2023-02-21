
n, m = (map(int, input().split(' ')))
print(n, m)
lst = []
for i in range(n):
    a = input().split(' ')
    while(len(a) != m):
        a = input().split(' ')
    lst.append(a)
    
def reverse_lst(lst):
    lst2 = [i for i in lst]
    lst2.reverse()
    for i in lst2:
        i.reverse()
    return lst2
print(reverse_lst(lst))
print("Mang ban dau la:", lst) #Tại sao vẫn bị đảo ngược trong các phần tử?


