from abc import ABC, abstractmethod
from instruments import Instr

class Prog(ABC):
    
    def __init__(self, is_max, sz_aim, aim, sz_coeffs, table, signs, free_members):
        self.is_max = is_max
        self.sz_aim = sz_aim
        self.aim = aim
        self.sz_coeffs = sz_coeffs
        self.table = table
        self.signs = signs
        self.free_members = free_members
        self.show_task()
        
    @abstractmethod
    def solve(self):
        pass
    
    def show_task(self):
        aim = [Instr.to_str(self.aim[i]) + "x" + Instr.to_down_index(i + 1) + " +" for i in range(self.sz_aim)]
        print("\n Математическая модель задачи")
        print(f' F = {" ".join(aim)[:-1]}-> {["min", "max"][self.is_max]}')
        for i in range(self.sz_coeffs):
            s = " ".join([["+ ", "- "][self.table[i][x] < 0] + Instr.to_str(abs(self.table[i][x])) + "x" + Instr.to_down_index(x + 1) for x in range(len(self.table[i]))])
            s += [" >= ", " <= "][self.signs[i]]
            s += Instr.to_str(self.free_members[i])
            print(s[1:])
        print()