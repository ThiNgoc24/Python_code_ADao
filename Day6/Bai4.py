from functools import reduce
n = int(input())
lst = [int(i) for i in input().split(' ')]
while len(lst) != n:
    lst = [int(i) for i in input().split(' ')]
t = int(input())
result = []
for i in range(t):
    i = int(input())
    result.append(reduce(lambda x,y: x+y, lst[:(i+1)]))

print(result)