from functools import reduce

def MyMultiple(*arg):
    return reduce(lambda x, y: x * y, arg)

print(MyMultiple(1,2,3))
