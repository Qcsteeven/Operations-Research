from instruments import Instr


class OptimumUsing:
    def __init__(self, cnt_products, cnt_ventures, matrix, products, ventures):
        self.cnt_products = cnt_products
        self.cnt_ventures = cnt_ventures
        self.matrix = matrix
        self.products = products
        self.ventures = ventures

        self.table = [[0 for i in range(
            cnt_ventures * (cnt_products - 1) + cnt_products)] for _ in range(cnt_ventures + 2)]
       
        for k in range(cnt_products - 1):
            for i in range(cnt_ventures):
                for j in range(cnt_ventures):
                    if i == j:
                        self.table[i][j + k * cnt_ventures] = 1
        
        for i in range(cnt_ventures):
            self.table[i][-1] = ventures[i]
        
        for j in range(1, cnt_products):
            for i in range(cnt_ventures):
                self.table[cnt_ventures][i + (j - 1) * cnt_ventures] = matrix[0][i] + matrix[j][i] * (products[0] / products[j]) 

        cur = (cnt_products - 1) * cnt_ventures
        for i in range(cur, cur + cnt_products - 1):
            self.table[cnt_ventures][i] = -(products[0] / products[i - cur + 1]) 
        
        for j in range(1, cnt_products):
            for i in range(cnt_ventures):
                self.table[cnt_ventures + 1][i + (j - 1) * cnt_ventures] = - matrix[j][i] / products[j]
                
        for i in range(cur, cur + cnt_products - 1):
            self.table[cnt_ventures + 1][i] = 1 / products[i - cur + 1]
        
            
        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                self.table[i][j] = round(self.table[i][j], 3)


    def solve(self):
        self.show()

    def show(self):
        for i in range(len(self.table)):
            print(*self.table[i])
