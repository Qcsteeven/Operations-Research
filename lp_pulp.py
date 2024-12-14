from copy import deepcopy
from math import floor, ceil

from instruments import Instr
from prog import Prog

from pulp import LpMaximize, LpMinimize, LpProblem, LpStatus, lpSum, LpVariable, LpStatus

class Pulp(Prog):
    
    def __init__(self, *args):
        super().__init__(*args)
        
    def solve(self):
        model = LpProblem(name="IntTask", sense=LpMaximize if self.is_max else LpMinimize)
        x = [LpVariable(name=f"x{Instr.to_down_index(i + 1)}", lowBound=0, cat="Integer") for i in range(self.sz_aim)]
        model += lpSum(self.aim[i] * x[i] for i in range(self.sz_aim)), "Objective"
        for i in range(self.sz_coeffs):
            model += (lpSum(self.table[i][j] * x[j] for j in range(self.sz_aim)) <= self.free_members[i])
        status = model.solve()
        if model.status: 
            print(f"F = {model.objective.value()}")
            for var in x:
                print(f"{var.name} = {var.value()}")
        else:
            print("No optimal solution found.")
            