from artif_method import ArtifMethod
from transport_task import Transport

class Solution:
    def __init__(self, *args):
        self.args = args

    def __call__(self, task):
        solution = None
        if task == 1:
            solution = ArtifMethod(*self.args)
        else:
            solution = Transport(*self.args)
        solution.solve()
