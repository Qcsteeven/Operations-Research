from instruments import Instr
from tabulate import tabulate
from copy import deepcopy

class OptimumUsing:
    def __init__(self, cnt_products, cnt_ventures, matrix, products, ventures):
        self.cnt_products = cnt_products
        self.cnt_ventures = cnt_ventures
        self.matrix = matrix
        self.products = products
        self.ventures = ventures
        self.plan = matrix
        
        # Заполнение жордановой таблицы
        self.table = [[0 for i in range(
            cnt_ventures * (cnt_products) + 2)] for _ in range(cnt_ventures + cnt_products + 1)]

        cnt = 0
        for i in range(cnt_products):
            for j in range(cnt_ventures):
                self.table[i][j + cnt] = -matrix[i][j]
            cnt += cnt_ventures
            
        for i in range(cnt_products):
            self.table[i][cnt_ventures * cnt_products] = products[i]
        
        for k in range(cnt_products):
            for i in range(cnt_products, cnt_products + cnt_ventures):
                for j in range(cnt_ventures):
                    if (i - cnt_products) == j:
                        self.table[i][j + k * cnt_ventures] = 1
                        
        for i in range(cnt_ventures):
            self.table[cnt_products + i][-1] = ventures[i]
            
        self.table[cnt_products + cnt_ventures][cnt_products * cnt_ventures] = -1

        self.basis = []
        self.not_basis = []

        for i in range(cnt_products):
            self.basis.append(f"y{i + 1}")
        for i in range(cnt_ventures):
            self.basis.append(f"0")
        self.basis.append("z")
        
        for i in range(cnt_products):
            for j in range(cnt_ventures):
                self.not_basis.append(f"x{j + 1}{i + 1}")
        self.not_basis.append("ξ")
        self.not_basis.append("1")
        

    def solve(self):
        print("Начальная жордановая таблица:")
        self.show()
        cnt = 1
        # Избавление от 0 - строк
        for i in range(self.cnt_ventures):
            print(f"{cnt} итерация избавления от 0-строк:")
            if all(x <= 0 for x in self.table[i + self.cnt_products]):
                print("Система несовместна")
                return 0
            cnt += 1
            self.basis[i + self.cnt_products] = self.not_basis[0]
            col = 0
            row = self.cnt_products + i
            self.mje(row, col)
            self.not_basis = self.not_basis[1:]
            for i in range(len(self.table)):
                self.table[i] = self.table[i][1:]
            self.show()
        
        free = []
        for i in range(len(self.table)):
            free.append(self.table[i][-1])
        while any(x < 0 for x in free):
            for i in range(len(self.table)):
                if self.table[i][-1] < 0:
                    if all(x >= 0 for x in self.table[i]):
                        print("Система несовместна")
                        return 0
                    else:
                        self.mje(*self.find())
                        break
                        
        cnt = 1
        while any(x < 0 for x in self.table[-1]):
            print(f"{cnt} итерация решения:")
            cnt += 1
            # Запуск метода модифицированных жордановых исключений
            self.mje(*self.find())
            self.basis[row], self.not_basis[col] = self.not_basis[col], self.basis[row]
            self.show()
        
        print(f"Оптимальное решение:")
        print(f"z = {self.table[-1][-1]}")
        solution = [(self.basis[i], self.table[i][-1]) for i in range(len(self.basis) - 1)]
        solution += [(self.not_basis[i], 0) for i in range(len(self.not_basis) - 1)]
        for i in range(len(solution)):
            if solution[i][0][0] == "x":
                print(f"{solution[i][0]} = {round(solution[i][1], 4)}")

    # Поиск разрешающего элемента
    def find(self):
        col = self.table[-1].index(min(self.table[-1]))
        mn = float("inf")
        row = None
        for i in range(len(self.table)):
            cur = self.table[i][col]
            div = 0
            if cur > 0:
                div = self.table[i][-1] / cur
            if div >= 0 and div < mn and cur > 0:
                mn = div
                row = i
        return row, col
    
    def mje(self, row, col):
        per_elem = self.table[row][col]
        
        table = deepcopy(self.table)
        
        # 1) Разрешающий элемент заменяется единицей
        table[row][col] = 1

        # 2) Остальные элементы (кроме разрешающего) элементы разрешающей строки остаются без изменений
            
        # 3) Остальные элементы разрешающего столбца меняют лишь свои знаки
        for i in range(len(self.table)):
            if i != row:
                table[i][col] = -self.table[i][col]

        # 4) Обыкновенные элементы вычисляются по формуле bij = aij * ars - ais * arj
        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                if i != row and j != col:
                    table[i][j] = self.table[i][j] * per_elem - self.table[i][col] * self.table[row][j]            

        # 5) Все элементы новой таблицы делятся на разрешающий элемент
        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                table[i][j] /= per_elem
                
        self.table = table

    def show(self):
        not_basis = ["-" + x for x in self.not_basis[:-1]] + [1]
        table = deepcopy(self.table)
        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                table[i][j] = round(self.table[i][j], 3)
                if table[i][j] == 0:
                    table[i][j] = 0
        print(tabulate(table, tablefmt="grid", headers=not_basis, showindex=self.basis))
