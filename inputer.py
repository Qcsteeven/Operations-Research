class Input:
    @classmethod
    def input(cls, task):
        if task in (1, 3):
            is_max = input(
                "Задача на поиск максимума или минимума? (max/min):\n")
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
        elif task == 2:
            m = int(input("Кол-во поставщиков: "))
            a = [int(x) for x in input(
                "Введите товары у поставщиков в формате 1 2 3:  ").split()]
            n = int(input("Кол-во потребителей: "))
            b = [int(x) for x in input(
                "Введите товары у потребителей в формате 1 2 3:  ").split()]
            print("Ввод матрицы тарифов:")
            matrix = [[int(x) for x in input(
                f"{i + 1} строка: ").split()] for i in range(m)]
            return m, a, n, b, matrix
        else:
            cnt_products = int(input("Кол-во видов изделий: "))
            cnt_ventures = int(input("Кол-во видов предприятий: "))
            print("Ввод матрицы производительности:")
            matrix = [[int(x) for x in input(
                f"Вектор {i + 1} изделия: ").split()] for i in range(cnt_products)]
            products = [int(x) for x in input("Вектор числа изделий в каждом комплекте").split()]
            ventures = [int(x) for x in input("Вектор числа предприятий  каждого вида").split()]
            return cnt_products, cnt_ventures, matrix, products, ventures
