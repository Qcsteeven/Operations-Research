class Input:
    @classmethod
    def input(cls):
        is_max = input("Задача на поиск максимума или минимума? (max/min):\n")
        is_max = True if is_max == "max" else False
        coefficients = [float(x) for x in input(
            "Введите вектор коэффициентов целевой функции:\n").split()]
        sz_aim = len(coefficients)
        sz_coeffs = int(input("Кол-во строк в матрице коэффицентов: "))
        print("Матрица ограничений(построчно):")
        print("Пример ввода: 1 2 3 >= 4")
        table = [input(f"Введите {i + 1} ограничение: ").split()
                for i in range(sz_coeffs)]
        signs = []
        free_members = []
        for i, elem in enumerate(table):
            table[i] = list(map(float, elem[:len(elem) - 2]))
            signs.append(elem[-2] == "<=")
            free_members.append(float(elem[-1]))
        return is_max, sz_aim, coefficients, sz_coeffs, table, signs, free_members