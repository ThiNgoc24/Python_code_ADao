# lst = set([int(x) for x in input().split(' ')])
lst = list(set(int(x) for x in input().split(' ')))
for i in lst:
    if i % 2 == 0:
        lst.remove(i)
print(' '.join([str(i) for i in lst]))