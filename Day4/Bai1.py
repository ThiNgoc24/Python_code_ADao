championLOL = ["Yasuo", "Lee Sin", "Zed", "Master Yi", "Garen", "Tryndamere"]
dataLOL = [
    {"price": 6300, "Ulti": "Trăn trối"},
    {"price": 4800, "Ulti": "Nộ Long Cước"},
    {"price": 4800, "Ulti": "Dấu Ấn Tử Thần"},
    {"price": 450, "Ulti": "Chiến Binh Sơn Cước"},
    {"price": 450, "Ulti": "Công Lý Demacia"},
    {"price": 1350, "Ulti": "Từ Chối Tử Thần"}	
]
d = {}
j = 0
for i in championLOL:
    d[i] = dataLOL[j]
    j += 1

minPrice = int(input("minPrice = "))
maxPrice = int(input("maxPrice=  "))

new_d = {}
for i in d.keys():
    if d[i]['price'] >= minPrice and d[i]['price'] <= maxPrice:
        new_d[i] = d[i]
print(new_d)
