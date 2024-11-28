from fogel_method import Fogel
from copy import deepcopy
from instruments import Instr


class Transport:
    def __init__(self, m, a, n, b, matrix):
        self.m = m
        self.a = a
        self.n = n
        self.b = b
        self.matrix = matrix

    def solve(self):
        self.build_math_model()
        self.method = Fogel()
        self.matrix = self.method.create(self.m, self.a, self.n, self.b, self.matrix)
        self.method.show()
        self.count = 1
        print(f"{self.count} итерация:")
        
        while not self.is_optimal():
            self.count += 1
            self.build_cycle()
            self.show()
            print(f"{self.count} итерация:")
            
        print("Оптимальный план:")
        self.show()
        
    
        
    def build_cycle(self):
        rows = [True for _ in range(self.m)]
        cols = [True for _ in range(self.n)]
        flag = True
        while flag and (any(x for x in rows) and any(x for x in cols)):
            flag = False
            for i in range(self.m):
                cnt1 = 0
                if rows[i]:
                    for j in range(self.n):
                        if cols[j] and self.matrix[i][j].is_base or (i, j) == self.idx_min:
                            cnt1 += 1
                    if cnt1 <= 1 and i != self.idx_min[0]:
                        rows[i] = False
                        flag = True
            
            for j in range(self.n):
                cnt2 = 0
                if cols[j]:
                    for i in range(self.m):
                        if rows[i] and self.matrix[i][j].is_base or (i, j) == self.idx_min:
                            cnt2 += 1
                    if cnt2 <= 1 and j != self.idx_min[1]:
                        cols[j] = False
                        flag = True

        cycle = []
        for i in range(self.m):
            for j in range(self.n):
                if rows[i] and cols[j]:
                    cycle.append((i, j))
        
        signs = []
        for i in range(len(cycle)):
            if i % 2 == 0: signs += ["+"]
            else: signs += ["-"]
        
        vector_cycle = [self.idx_min]
        cycle.remove(self.idx_min)
        cur = self.idx_min
        direction = True
        while cycle:
            if direction: cnst = cur[0]
            else: cnst = cur[1]
            nxt = None
            dif = 0
            for elem in cycle:
                if direction:
                    if elem[0] == cnst:
                        cur_diff = abs(elem[1] - cur[1])
                        if cur_diff > dif:
                            dif = cur_diff
                            nxt = elem
                else:
                    if elem[1] == cnst:
                        cur_diff = abs(elem[0] - cur[0])
                        if cur_diff > dif:
                            dif = cur_diff
                            nxt = elem
            cycle.remove(nxt)
            vector_cycle.append(nxt)
            direction = not direction
            cur = nxt
        return vector_cycle
            

    def is_optimal(self):
        v = [None for _ in range(self.n)]
        u = [None for _ in range(self.m)]
        u[0] = 0
        basis = self.method.get_basis()

        while any(v[i] is None for i in range(self.n)) or any(u[i] is None for i in range(self.m)):
            for x in range(len(basis)):
                tariff, qua, is_base, i, j = basis[x][0].tariff, basis[x][0].qua, basis[x][0].is_base, *basis[x][1]
                if (not u[i] is None) and (v[j] is None):
                    v[j] = tariff + u[i]
                elif (u[i] is None) and (not v[j] is None):
                    u[i] = v[j] - tariff
                    
        eval_matrix = [[0 for _ in range(self.n)] for i in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                eval_matrix[i][j] = self.matrix[i][j].tariff - (v[j] - u[i])
        
        print("Проверка на оптимальность: ")
        for i in range(self.m):
            print(f"u{Instr.to_down_index(i + 1)} = {u[i]}")
        for j in range(self.n):
            print(f"v{Instr.to_down_index(j + 1)} = {v[j]}")
        
        print("Оценочная матрица:")
        indent = max(max(len(Instr.to_str(j)) for j in i) for i in eval_matrix) + 1
        for i in range(self.m):
            out = ""
            for j in range(self.n):
                cur = Instr.to_str(eval_matrix[i][j])
                out += cur + " " * (indent + 1 - len(cur))
            print(out)
        
        fnd_min = float("inf")
        self.idx_min = (0, 0)
        for i in range(self.m):
            for j in range(self.n):
                if eval_matrix[i][j] < fnd_min:
                    fnd_min = eval_matrix[i][j]
                    self.idx_min = (i, j)
        return fnd_min >= 0
                 

    def build_math_model(self):
        print()
        sma, smb = sum(self.a), sum(self.b)
        dif = abs(sma - smb)
        if sma > smb:
            print("Σa > Σb")
            self.b.append(dif)
            for i in range(self.m):
                self.matrix[i].append(0)
            self.n += 1
            print(f"Вводим фиктивного потребителя B{Instr.to_down_index(self.n + 1)} с запросом {dif}")
        elif sma < smb:
            print("Σa < Σb")
            self.a.append(dif)
            self.matrix.append([0 for _ in range(self.n)])
            self.m += 1
            print(f"Вводим фиктивного поставщика A{Instr.to_down_index(self.m + 1)} с товаром {dif}")
        else:
            print("Σa == Σb")
            print("Фиктивный поставщик/потребитель не требуется")
        print("Получаем начальную таблицу:")
        self.show_start()
        print("\nМатематическая модель задачи:")
        out = "L = "
        for i in range(self.m):
            for j in range(self.n):
                if i == self.m - 1 and j == self.n - 1:
                    out += Instr.to_str(self.matrix[i][j]) + f"x{Instr.to_down_index(i + 1)}{Instr.to_down_index(j + 1)}"
                else:
                    out += Instr.to_str(self.matrix[i][j]) + f"x{Instr.to_down_index(i + 1)}{Instr.to_down_index(j + 1)} + "
        out += " → min"
        print(out)
        for i in range(self.m):
            out = ""
            for j in range(self.n):
                if j == self.n - 1:
                    out += f"x{Instr.to_down_index(i + 1)}{Instr.to_down_index(j + 1)}"
                else:
                    out += f"x{Instr.to_down_index(i + 1)}{Instr.to_down_index(j + 1)} + "
            out += f" = {self.a[i]}"
            print(out)
            
        for j in range(self.n):
            out = ""
            for i in range(self.m):
                if i == self.m - 1:
                    out += f"x{Instr.to_down_index(i + 1)}{Instr.to_down_index(j + 1)}"
                else:
                    out += f"x{Instr.to_down_index(i + 1)}{Instr.to_down_index(j + 1)} + "
            out += f" = {self.b[j]}"
            print(out)

    def show_start(self):
        indent = max([max(max([len(Instr.to_str(x)) + 4 for x in self.matrix[i]]) for i in range(self.m)), 9])
        out = "Ai \ Bj" + (indent - 6) * " "
        for j in range(len(self.b)):
            symbol = f'B{Instr.to_down_index(j + 1)} = {self.b[j]}'
            out += symbol + " " * (indent + 1 - len(symbol))
        print(out)
        
        for i in range(self.m):
            out = ""
            symbol = f'A{Instr.to_down_index(i + 1)} = {self.a[i]}'
            out += symbol + " " * (indent + 1 - len(symbol))
            for j in range(self.n):
                cur = Instr.to_str(self.matrix[i][j])
                out += cur + " " * (indent + 1 - len(cur))
            print(out)
            
    def show(self):
        indent = max([max(max([len(Instr.to_str(x.tariff)) + 4 for x in self.matrix[i]]) for i in range(self.m)), 9]) * 2
        out = indent * " "
        for j in range(len(self.b)):
            symbol = f'B{Instr.to_down_index(j + 1)} = {self.b[j]}'
            out += symbol + " " * (indent + 1 - len(symbol))
        print(out)
        
        for i in range(len(self.a)):
            out = ""
            symbol = f'A{Instr.to_down_index(i + 1)} = {self.a[i]}'
            out += symbol + " " * (indent + 1 - len(symbol))
            for j in range(len(self.matrix[i])):
                cur = Instr.to_str(self.matrix[i][j].tariff) + " | "
                if self.matrix[i][j].is_base:
                    cur += Instr.to_str(self.matrix[i][j].qua) + " ✔"
                else:
                    cur += "0"
                out += cur + " " * (indent + 1 - len(cur))
            print(out)
        
        aim = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.matrix[i][j].is_base:
                    aim += self.matrix[i][j].qua * self.matrix[i][j].tariff
        
        print(f"Значение целевой функции: {aim}")
        input()
       