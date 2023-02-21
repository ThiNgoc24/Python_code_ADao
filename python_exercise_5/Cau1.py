
class Matrix:
    def __init__(self):
        self.n = int(input())
        self.m = int(input())
        self.shape = (self.m, self.n)

    def inputList(self):
        for i in range(self.m):
            row = list(map(int, input().split(' ')))
            while(len(row) != self.n):
                row = list(map(int, input().split(' ')))
            self.shape.append(row)  
   
    def operatorCong(self):
        # shapekq = [[0] * self.n] * self.m
        shapekq = self.shape
        for i in range(self.m):
            for j in range(self.n):
                shapekq[i][j] = self.shape[i][j] + self.shape[i][j]
        return shapekq
    
    def operatorTru(self):
        # shapekq = [[0] * self.n] * self.m
        shapekq = self.shape
        for i in range(self.m):
            for j in range(self.n):
                shapekq[i][j] = self.shape[i][j] - self.shape[i][j]
        return shapekq
    
    def operatorNhan(self):
        # shapekq = [[0] * self.n] * self.m
        shapekq = self.shape
        for i in range(self.m):
            for j in range(self.n):
                shapekq[i][j] = self.shape[i][j] * self.shape[i][j]
        return shapekq
    
    # def operatorTich(self, matrix2):
    #     matrix2 = Matrix().inputList()
    #     while (len(matrix2) != self.n):
    #         print("Vui lòng nhập lại ma trận nhân: ")
    #         matrix2 = Matrix().inputList()
    #     matrixkq = 

    
# a = Matrix()
# a.inputList()
# print(a.shape)
# print("Cộng hai ma trận:", a.operatorCong())
# print("Trừ hai ma trận:",a.operatorTru())
# print("Nhân hai ma trận: ", a.operatorNhan())

ls = [*open(0)]
print(ls)