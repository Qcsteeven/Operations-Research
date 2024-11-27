from copy import deepcopy
from instruments import Instr

class Cell:
    def __init__(self, tariff):
        self.tariff = tariff
        self.qua = tariff
        self.is_base = False
        
class Fogel:
    def __init__(self):
        pass

    def create(self, m, a, n, b, matrix):
        self.plan = matrix
        self.a = [[] for _ in range(m)]
        for i in range(m):
            self.a[i].append(a[i])
        self.b = [[] for _ in range(n)]
        for i in range(n):
            self.b[i].append(b[i])
        matrix = deepcopy(matrix)
        for i in range(m):
            for j in range(n):
                matrix[i][j] = Cell(matrix[i][j])
        matrix_t = [[] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                matrix_t[i].append(matrix[j][i])
        difs_a = [[] for _ in range(m)]
        difs_b = [[] for _ in range(n)]
        self.difs_a = difs_a
        self.difs_b = difs_b
        self.basis = []
        
        while True:
        
            for i in range(m):
                cur = []
                for j in range(n):
                    if matrix[i][j].qua != -1 and not matrix[i][j].is_base:
                        if matrix[i][j].tariff >= 0:
                            cur.append(matrix[i][j].tariff)
                cur.sort()
                if cur:
                    if len(cur) == 1:
                        difs_a[i].append(cur[0])
                    else:
                        difs_a[i].append(cur[1] - cur[0])
                else:
                    difs_a[i].append("-")
            
            for i in range(n):
                cur = []
                for j in range(m):
                    if matrix_t[i][j].qua != -1 and not matrix_t[i][j].is_base:
                        if matrix_t[i][j].tariff >= 0:
                            cur.append(matrix_t[i][j].tariff)
                cur.sort()
                if cur:
                    if len(cur) == 1:
                        difs_b[i].append(cur[0])
                    else:
                        difs_b[i].append(cur[1] - cur[0])
                else:
                    difs_b[i].append("-")


            mx_a = 0
            for i in range(m):
                if difs_a[i][-1] != "-":
                    mx_a = max(mx_a, difs_a[i][-1])

            mx_b = 0
            for i in range(n):
                if difs_b[i][-1] != "-":
                    mx_b = max(mx_b, difs_b[i][-1])

            
            mn_tarifs = []
            
            for i in range(m):
                if difs_a[i][-1] == mx_a:
                    mn = float('inf')
                    idx = ()
                    for j in range(n):
                        if matrix[i][j].qua != -1 and not matrix[i][j].is_base:
                            if matrix[i][j].tariff < mn:
                                idx = i, j
                                mn = matrix[i][j].tariff
                    mn_tarifs.append([mx_a, mn, *idx, "row"])

            for i in range(n):
                if difs_b[i][-1] == mx_b:
                    mn = float('inf')
                    idx = ()
                    for j in range(m):
                        if matrix_t[i][j].qua != -1 and not matrix_t[i][j].is_base:
                            if matrix_t[i][j].tariff < mn:
                                idx = j, i
                                mn = matrix_t[i][j].tariff
                    mn_tarifs.append([mx_b, mn, *idx, "col"])
            
            mx = max(mx_a, mx_b)
            cur_elem = [0, float("inf"), 0, 0, 0]
            mn_tarifs.sort(key=lambda x: 0 if x[4] == "col" else 1)
            for i in range(len(mn_tarifs)):
                if mn_tarifs[i][0] == mx:
                    if mn_tarifs[i][1] < cur_elem[1]:
                        cur_elem = mn_tarifs[i]
            
            i_o, j_o = cur_elem[2], cur_elem[3]
            matrix[i_o][j_o].is_base = True
            self.basis.append([matrix[i_o][j_o], (i_o, j_o)])
            if self.a[i_o][-1] == 0 or self.b[j_o][-1] == 0:
                matrix[i_o][j_o].qua = max(self.a[i_o][-1], self.b[j_o][-1])
                self.a[i_o].append(0)
                self.b[j_o].append(0)
            elif self.a[i_o][-1] < self.b[j_o][-1]:
                matrix[i_o][j_o].qua = self.a[i_o][-1]
                self.a[i_o].append(0)
                self.b[j_o].append(self.b[j_o][-1] - matrix[i_o][j_o].qua)
            else:
                matrix[i_o][j_o].qua = self.b[j_o][-1]
                self.b[j_o].append(0)
                self.a[i_o].append(self.a[i_o][-1] - matrix[i_o][j_o].qua)
            
            
            if self.a[i_o][-1] == 0:
                for i in range(n):
                    if not matrix[i_o][i].is_base:
                        matrix[i_o][i].qua = -1
            
            if self.b[j_o][-1] == 0:
                for i in range(m):
                    if not matrix_t[j_o][i].is_base:
                        matrix_t[j_o][i].qua = -1
            
            flag = True
            for i in range(m):
                flag &= self.a[i][-1] == 0
            for j in range(n):
                flag &= self.b[j][-1] == 0
            
            self.plan = matrix
            if flag:
                break
            
        return self.plan

    def get_basis(self):
        return self.basis

    def show(self):
        print("Опорный план методом Фогеля:")
        indent = 27
        out = indent * " "
        for j in range(len(self.b)):
            symbol = f'B{Instr.to_down_index(j + 1)} = {" | ".join([Instr.to_str(x) for x in self.b[j]])}'
            out += symbol + " " * (indent + 1 - len(symbol))
        print(out)
        
        for i in range(len(self.a)):
            indent = 27
            out = ""
            symbol = f'A{Instr.to_down_index(i + 1)} = {" | ".join([Instr.to_str(x) for x in self.a[i]])}'
            out += symbol + " " * (indent + 1 - len(symbol))
            for j in range(len(self.plan[i])):
                cur = Instr.to_str(self.plan[i][j].tariff) + " | "
                if self.plan[i][j].is_base:
                    cur += Instr.to_str(self.plan[i][j].qua) + " ✔"
                else:
                    cur += "0"
                out += cur + " " * (indent + 1 - len(cur))
            indent = 5
            for j in range(len(self.difs_a[i])):
                cur = self.difs_a[i][j]
                if isinstance(cur, int):
                    cur = Instr.to_str(cur)
                
                out += cur + " " * (indent + 1 - len(cur))
            print(out)
        
       
                

        for i in range(len(self.difs_b[i])):
            indent = 27
            out = (indent + 1) * " "
            for j in range(len(self.difs_b)):
                cur = self.difs_b[j][i]
                if isinstance(cur, int):
                    cur = Instr.to_str(cur)
                
                out += cur + " " * (indent + 1 - len(cur))
            print(out)