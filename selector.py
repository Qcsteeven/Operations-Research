from artif_method import ArtifMethod


class Solution:
    def __init__(self, is_max, *args):
        self.__is_max = is_max
        self.args = args

    def __call__(self):
        solution = None
        solution = ArtifMethod(self.__is_max, *self.args)
        solution.solve()
