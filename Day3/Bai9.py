tuple1 = ('tài', 'thùy', 'thạch', 'trường', 'tiến')
tuple2 = ('hải', 'tài', 'nhật minh', 'cao minh', 'đặng anh', 'hùng', 'trường')

print("#tuple1 - tuple2")
value1 = []
for i in tuple1:
    if i not in tuple2:
        value1.append(i)
print(tuple(value1))
print("#tuple2 - tuple1")
value2 = []
for i in tuple2:
    if i not in tuple1:
        value2.append(i)
print(tuple(value2))