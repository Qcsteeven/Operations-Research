from artif_method import ArtifMethod
from transport_task import Transport
from optimum_using import OptimumUsing
from lp_scipy import LinProg
from lp_pulp import Pulp

class Solution:
    def __init__(self, *args):
        self.args = args

    def __call__(self, task):
        solution = None
        if task == 1:
            solution = ArtifMethod(*self.args)
        elif task == 2:
            solution = Transport(*self.args)
        elif task == 3:
            choose = int(input("Выбор метода: 1 - библиотека scipy; 2 - библиотека Pulp:\n"))
            match (choose):
                case 1:
                    solution = LinProg(*self.args)
                case 2:
                    solution = Pulp(*self.args)
        else:
            solution = OptimumUsing(*self.args)
        solution.solve()
