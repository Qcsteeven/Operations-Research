from copy import deepcopy
from math import floor, ceil

from instruments import Instr
from prog import Prog

from scipy.optimize import linprog

class LinProg(Prog):
    
    def __init__(self, *args):
        super().__init__(*args)
        if self.is_max:
            self.aim = [-x for x in self.aim]
        for i in range(self.sz_coeffs):
            for j in range(self.sz_aim):
                self.table[i][j] = self.table[i][j] if self.signs[i] else -self.table[i][j]
            self.free_members[i] = self.free_members[i] if self.signs[i] else -self.free_members[i]
        self.limits = [(0, float("inf")) for _ in range(self.sz_aim)]

    def solve(self):
        first_res = linprog(c=self.aim, A_ub=self.table, b_ub=self.free_members, bounds=self.limits, method="highs")
        print(first_res.fun)
        best_solves = [([first_res.x[i] for i in range(self.sz_aim)], -first_res.fun if self.is_max else first_res.fun)]
        solves = [[self.table, self.free_members]]
        optimum = None
        if self.is_max:
            optimum = float("-inf")
        else:
            optimum = float("inf")
        while any(any(not elem.is_integer() for elem in slv[0]) for slv in best_solves):
            not_ints = set()
            new_solves = []
            for i in range(len(best_solves)):
                cur = best_solves[i][0]
                if (self.is_max and best_solves[i][1] > optimum) or ((not self.is_max) and best_solves[i][1] < optimum):
                    for j in range(len(cur)):
                        if not cur[j].is_integer():
                            not_ints.add(i)
                            new_str_left = [1 if k == j else 0 for k in range(self.sz_aim)]
                            new_str_right = [-1 if k == j else 0 for k in range(self.sz_aim)]
                            new_solves.append([solves[i][0] + [new_str_left], solves[i][1] + [floor(cur[j])]])
                            new_solves.append([solves[i][0] + [new_str_right], solves[i][1] + [-ceil(cur[j])]])
                else:
                    not_ints.add(i)
                
            best_solves = [best_solves[i] for i in range(len(best_solves)) if i not in not_ints]
            solves = [solves[i] for i in range(len(solves)) if i not in not_ints]
            for i in range(len(new_solves)):
                res = linprog(c=self.aim, A_ub=new_solves[i][0], b_ub=new_solves[i][1], bounds=self.limits, method="highs")
                if res.success:
                    cur = ([res.x[i] for i in range(self.sz_aim)], -res.fun if self.is_max else res.fun)
                    if (self.is_max and cur[1] > optimum) or (self.is_max and cur[1] < optimum):
                        solves.append(new_solves[i])
                        best_solves.append(cur)
        
        answer = max(best_solves, key = lambda x : x[1])
        print(f"F = {answer[1]}") 
        for i in range(len(answer[0])):
            print(f"x{Instr.to_down_index(i + 1)} = {answer[0][i]}")
