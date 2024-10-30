class Instr:
    @staticmethod
    def sumproduct(lst1, lst2):
        return sum([x * y for x, y in zip(lst1, lst2)])
    
    @staticmethod
    def to_str(number):
        if int(number) == number:
            out = str(int(number))
        else:
            out = str(round(number, 3))
        return out