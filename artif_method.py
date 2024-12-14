from copy import deepcopy
from instruments import Instr
from prog import Prog

class ArtifMethod(Prog):

    infty = 10000000

    def __init__(self, *args):
        super().__init__(*args)

    def solve(self):
        self.is_solve = False
        self.size = self.sz_aim + self.sz_coeffs
        self.create_table()
        self.aim = self.create_aim()
        self.cur_basis = self.create_basis()
        self.delts = self.calc_delts()
        if not self.is_max and all(x for x in self.signs):
             self.all_zero()
             return
        self.tetas = self.calc_tetas()
        self.count = 0
        self.show_table()
        while self.is_correct():
            self.table = self.calc_table()
            self.delts = self.calc_delts()
            if self.is_max:
                if all(x >= 0 for x in self.delts[:self.size - self.artif]):
                    self.is_solve = True
                    self.show_table()
                    break
            else:
                if all(x <= 0 for x in self.delts[:self.size - self.artif]):
                    self.is_solve = True
                    self.show_table()
                    break
            self.tetas = self.calc_tetas()
            self.show_table()
        else:
            print("\nЗадача нерешаема")
        self.end()
        
    def create_ans(self):
        answer = [0 for i in range(self.size)]
        for i in range(self.sz_coeffs):
            answer[self.cur_basis[i] - 1] = self.free_members[i]
        answer = [Instr.to_str(x) for x in answer]
        return answer
        
    def all_zero(self):
        answer = self.create_ans()
        print(f'\nОптимальное решение:\n F = {Instr.to_str(self.answer)} \n({" ".join(answer)})')
    
    def end(self):
        if any(self.cur_basis[i] in range(self.sz_aim + self.sz_coeffs + 1, self.size + 1) for i in range(len(self.cur_basis))):
            print("\nТ.к. в оптимальном решении присутствует искусственная переменная, то задача не решаема\n")
        elif self.is_correct():
            answer = self.create_ans()
            print(f'\nОптимальное решение:\n F = {Instr.to_str(self.answer)} \n({" ".join(answer)})')
    
    def create_aim(self):
        aim = [0] + self.aim + [0] * self.sz_coeffs
        if self.is_max:
            aim += [-self.infty] * self.artif
        else:
            aim += [self.infty] * self.artif
        return aim
    
    def create_basis(self):
        basis = []
        for i in range(self.sz_coeffs):
            for j in range(self.sz_aim, self.size):
                if self.table[i][j] == 1:
                    basis.append(j + 1)
        return basis
        
    def is_correct(self):
        flag = False
        for i in range(self.sz_coeffs):
            flag |= self.table[i][self.mn_delta] >= 0
        return flag

    def calc_table(self):
        table = deepcopy(self.table)
        new_table = deepcopy(self.table)
        free_cop = deepcopy(self.free_members)
        self.cur_basis[self.mn_teta] = self.mn_delta + 1

        for i in range(self.sz_coeffs):
            if i == self.mn_teta:
                free_cop[i] = self.free_members[self.mn_teta] / table[self.mn_teta][self.mn_delta]
            else:
                free_cop[i] = self.free_members[i] - \
                    (self.free_members[self.mn_teta] * table[i][self.mn_delta]) / table[self.mn_teta][self.mn_delta]
        self.free_members = free_cop

        for i in range(self.sz_coeffs):
            for j in range(self.size):
                if i == self.mn_teta:
                    new_table[i][j] = table[self.mn_teta][j] / table[self.mn_teta][self.mn_delta]
                else:
                    new_table[i][j] = table[i][j] - \
                        ((table[self.mn_teta][j] * table[i][self.mn_delta]) / table[self.mn_teta][self.mn_delta])
        return new_table

    def calc_tetas(self):
        if self.is_max:
            self.mn_delta = self.delts.index(min([x for x in self.delts if x < 0]))
        else:
            self.mn_delta = self.delts.index(max([x for x in self.delts if x > 0]))
        direct_vector = [self.table[i][self.mn_delta] for i in range(self.sz_coeffs)]
        tetas = []
        for i in range(self.sz_coeffs):
            if direct_vector[i] == 0:
                tetas.append(self.infty)
            else:
                cal = self.free_members[i] / direct_vector[i]
                if cal > 0:
                    tetas.append(self.free_members[i] / direct_vector[i])
                else:
                    tetas.append(self.infty)
        self.mn_teta = tetas.index(min(tetas))
        return tetas

    def calc_delts(self):
        c_basis = [self.aim[i] for i in self.cur_basis]
        self.answer = Instr.sumproduct(c_basis, self.free_members) - self.aim[0]
        delts = [[self.table[j][i]
                  for j in range(self.sz_coeffs)] for i in range(self.size)]
        delts = [Instr.sumproduct(delts[i], c_basis) - self.aim[i + 1]
                 for i in range(self.size)]
        return delts

    def change_signs(self):
        for i, sign in enumerate(self.signs):
            if not sign:
                for j in range(self.sz_aim):
                    self.table[i][j] = -self.table[i][j]
                self.free_members[i] = -self.free_members[i]
                self.signs[i] = True

    def create_table(self):
        for i in range(self.sz_coeffs):
            for j in range(self.sz_coeffs):
                if i == j:
                    self.table[i].append(1 if self.signs[i] else -1)
                else:
                    self.table[i].append(0)
        self.artif = sum(1 for i in self.signs if i == False)
        for i in range(self.sz_coeffs):
            for j in range(self.artif):
                self.table[i].append(0)
        ind = 0
        for i in range(len(self.signs)):
            if not self.signs[i]:
                self.table[i][self.sz_coeffs + self.sz_aim + ind] = 1
                ind += 1
        self.size += self.artif

    def show_table(self):
        print(f'\n{self.count} итерация:')
        self.count += 1
        indent = max(max([len(Instr.to_str(y)) for y in x + self.free_members + self.delts + self.tetas])
                     for x in self.table) + 2

        out = "Cj" + (indent - 2) * " "  + (indent) * " "
        for elem in self.aim:
            elem = Instr.to_str(elem)
            out += elem + " " * (indent + 1 - len(elem))
        print(out)

        out = " " * (indent) + "Bx" + " " * (indent - 2)
        for i in range(self.size + 1):
            symbol = f'A{Instr.to_down_index(i)}'
            out += symbol + " " * (indent + 1 - len(symbol))
        if not self.is_solve:
            out += "θ"
        print(out)

        cnst = (indent) * " "

        for i in range(self.sz_coeffs):
            c = f'{Instr.to_str(self.aim[self.cur_basis[i]])}'
            b = f'x{Instr.to_down_index(int(Instr.to_str(self.cur_basis[i])))}'
            out = c + " " * (indent - len(c)) + b + " " * (indent - len(b))
            for elem in [self.free_members[i], *self.table[i]]:
                cur = Instr.to_str(elem)
                out += cur + " " * (indent + 1 - len(cur))
            if not self.is_solve:
                teta = Instr.to_str(self.tetas[i])
                if teta == str(self.infty):
                    out += "∞"
                else:
                    out += teta
            print(out)

        delta = Instr.to_str(self.answer)
        out = (indent) * " " + "Δj" + (indent - 2) * \
            " " + delta + (indent - len(delta) + 1) * " "
        for elem in self.delts:
            cur = Instr.to_str(elem)
            out += cur + (indent - len(cur) + 1) * " "
        print(out)

        if not self.is_solve:
            print(f"Вводим A{Instr.to_down_index(self.mn_delta + 1)}, Выводим A{Instr.to_down_index(self.cur_basis[self.mn_teta])}")
