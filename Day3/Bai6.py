a, b, n = map(int, input().split())
while(b < a):
    print("Mời nhập lại a <= n <= b: ")
    a, b, n = map(int, input().split())
result = []
for i in range(a, b+1):
    if i % n == 0:
        result.append(i)
print(result)

