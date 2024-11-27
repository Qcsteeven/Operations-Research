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
        self.is_optimal()

    def is_optimal(self):
        v = [None for _ in range(self.n)]
        u = [None for _ in range(self.m)]
        u[0] = 0
        basis = self.method.get_basis()
        for i in range(len(basis)):
            print(basis[i][0].tariff, basis[i][0].qua, basis[i][0].is_base, basis[i][1])

        while any(v[i] is None for i in range(n)) and any(u[i] is None for i in range(m)):
            for x in range(len(basis)):
                tariff, qua, is_base, i, j = basis[i][0].tariff, basis[i][0].qua, basis[i][0].is_base, basis[i][1]
                if (not u[i] is None) and (v[j] is None):
                    v[j] = tariff + u[i]
                elif (u[i] is None) and (not v[j] is None):
                    u[i] = v[j] - tariff
            

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
        self.show()
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
                    out += Instr.to_str(self.matrix[i][j]) + f"x{Instr.to_down_index(i + 1)}{Instr.to_down_index(j + 1)} + "
            out += f" = {self.a[i]}"
            print(out)
            
        for j in range(self.n):
            out = ""
            for i in range(self.m):
                if i == self.m - 1:
                    out += f"x{Instr.to_down_index(i + 1)}{Instr.to_down_index(j + 1)}"
                else:
                    out += Instr.to_str(self.matrix[i][j]) + f"x{Instr.to_down_index(i + 1)}{Instr.to_down_index(j + 1)} + "
            out += f" = {self.b[j]}"
            print(out)
        
        

    def show(self):
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
            