class Test:
    @classmethod
    def test(cls, task):
        if task in (1, 3):
            start, end = 1, 12
            case = int(input(f"Какой тест({start} - {end}): "))
            while True:
                match case:
                    case 1:
                        is_max = True
                        coefficients = [14, 18]
                        sz_aim = len(coefficients)
                        sz_coeffs = 3
                        table = [[10, 8], [5, 10], [6, 12]]
                        signs = [True, True, True]
                        free_members = [168, 180, 144]
                        return is_max, sz_aim, coefficients, sz_coeffs, table, signs, free_members
                    case 2:
                        is_max = True
                        coefficients = [3, 2]
                        sz_aim = len(coefficients)
                        sz_coeffs = 3
                        table = [[1, 2], [2, -1], [1, 3]]
                        signs = [True, False, False]
                        free_members = [12, 7, 14]
                        return is_max, sz_aim, coefficients, sz_coeffs, table, signs, free_members
                    case 3:
                        is_max = False
                        coefficients = [4, 1]
                        sz_aim = len(coefficients)
                        sz_coeffs = 3
                        table = [[1, 2], [2, -1], [1, 3]]
                        signs = [False, False, True]
                        free_members = [12, 12, 14]
                        return is_max, sz_aim, coefficients, sz_coeffs, table, signs, free_members
                    case 4:
                        is_max = False
                        coefficients = [4, 3, 6]
                        sz_aim = len(coefficients)
                        sz_coeffs = 2
                        table = [[3, -4, 2], [5, 2, 3]]
                        signs = [False, False]
                        free_members = [11, 16]
                        return is_max, sz_aim, coefficients, sz_coeffs, table, signs, free_members
                    case 5:
                        is_max = False
                        coefficients = [10, 20]
                        sz_aim = len(coefficients)
                        sz_coeffs = 2
                        table = [[4, 3], [5, 6]]
                        signs = [False, False]
                        free_members = [2, 3]
                        return is_max, sz_aim, coefficients, sz_coeffs, table, signs, free_members
                    case 6:
                        is_max = True
                        coefficients = [360, 240]
                        sz_aim = len(coefficients)
                        sz_coeffs = 3
                        table = [[3, 6], [8, 2], [4, 6]]
                        signs = [False, True, False]
                        free_members = [1440, 720, 960]
                        return is_max, sz_aim, coefficients, sz_coeffs, table, signs, free_members
                    case 7:
                        is_max = True
                        coefficients = [4, 5]
                        sz_aim = len(coefficients)
                        sz_coeffs = 2
                        table = [[1, 1], [1, 1]]
                        signs = [True, False]
                        free_members = [2, 5]
                        return is_max, sz_aim, coefficients, sz_coeffs, table, signs, free_members
                    case 8:
                        is_max = False
                        coefficients = [4, 5]
                        sz_aim = len(coefficients)
                        sz_coeffs = 2
                        table = [[1, 1], [1, 1]]
                        signs = [True, True]
                        free_members = [2, 5]
                        return is_max, sz_aim, coefficients, sz_coeffs, table, signs, free_members
                    case 9:
                        is_max = False
                        coefficients = [168, 180, 144]
                        sz_aim = len(coefficients)
                        sz_coeffs = 2
                        table = [[10, 5, 6], [8, 10, 12]]
                        signs = [False, False]
                        free_members = [14, 18]
                        return is_max, sz_aim, coefficients, sz_coeffs, table, signs, free_members
                    case 10:
                        is_max = False
                        coefficients = [1, 10, 100, 1000, 10000]
                        sz_aim = len(coefficients)
                        sz_coeffs = 5
                        table = [[1, 2, 3, 4, 5], [5, 6, 7, 8, 9], [9, 10, 11, 12, 13], [13, 14, 15, 16, 17], [17, 18, 19, 20, 21]]
                        signs = [True, False, False, False, True]
                        free_members = [2, 4, 8, 16, 32]
                        return is_max, sz_aim, coefficients, sz_coeffs, table, signs, free_members
                    case 11:
                        is_max = True
                        coefficients = [50000, 48000]
                        sz_aim = len(coefficients)
                        sz_coeffs = 5
                        table = [[30, 6], [16, 12], [1, 2], [2.5, 7], [1.4, 1]]
                        signs = [True, True, True, True, True]
                        free_members = [2900, 1800, 170, 490, 110]
                        return is_max, sz_aim, coefficients, sz_coeffs, table, signs, free_members
                    case 12:
                        is_max = True
                        coefficients = [0 for _ in range(15)] + [1]
                        sz_aim = len(coefficients)
                        sz_coeffs = 8
                        table = [[100, 400, 20, 200, 600, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2], 
                                 [0, 0, 0, 0, 0, 15, 200, 25, 50, 250, 0, 0, 0, 0, 0, -1], 
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 150, 200, 25, 350, -3], 
                                 [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
                                 [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                                 [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                                 [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0]]
                        signs = [False, False, False, True, True, True, True, True]
                        free_members = [0, 0, 0, 5, 3, 40, 9, 2]
                        return is_max, sz_aim, coefficients, sz_coeffs, table, signs, free_members
                    case _:
                        print(f"Неверный ввод! Введите число от {start} до {end}: ")
                        case = int(input(f"Какой тест({start} - {end}): "))
        elif task == 2:
            start, end = 1, 5
            case = int(input(f"Какой тест({start} - {end}): "))
            while True:
                match case:
                    case 1:
                        a = [101, 46, 38]
                        b = [11, 21, 42, 32]
                        matrix = [
                            [6, 20, 4, 2],
                            [4, 6, 20, 8],
                            [10, 16, 14, 6]
                        ]
                        return len(a), a, len(b), b, matrix
                    case 2:
                        a = [160, 650, 190]
                        b = [500, 200, 300, 100]
                        matrix = [
                            [10, 12, 2, 8],
                            [16, 20, 12, 10],
                            [10, 8, 6, 20]
                        ]
                        return len(a), a, len(b), b, matrix
                    case 3:
                        a = [45, 23, 33]
                        b = [30, 20, 15, 8]
                        matrix = [
                            [10, 2, 4, 8],
                            [4, 10, 20, 6],
                            [20, 4, 4, 10]
                        ]
                        return len(a), a, len(b), b, matrix
                    case 4:
                        a = [20, 30, 50]
                        b = [30, 20, 40, 10]
                        matrix = [
                            [6, 4, 1, 5],
                            [3, 8, 7, 3],
                            [4, 6, 8, 2],
                        ]
                        return len(a), a, len(b), b, matrix
                    case 5:
                        a = [220, 420, 320]
                        b = [220, 220, 420, 220]
                        matrix = [
                            [60, 52, 56, 40],
                            [80, 32, 28, 12],
                            [40, 72, 80, 48],
                        ]
                        return len(a), a, len(b), b, matrix
        else:
            start, end = 1, 2
            case = int(input(f"Какой тест({start} - {end}): "))
            while True:
                match case:
                    case 1:
                        cnt_products = 2
                        cnt_ventures = 5
                        matrix = [[100, 400, 20, 200, 600],
                                  [15, 200, 2.5, 50, 250]]
                        products = [2, 1]
                        ventures = [5, 3, 40, 9, 2]
                        return cnt_products, cnt_ventures, matrix, products, ventures
                    case 2:
                        cnt_products = 3
                        cnt_ventures = 5
                        matrix = [[100, 400, 20, 200, 600],
                                  [15, 200, 25, 50, 250],
                                  [100, 150, 200, 25, 350]]
                        products = [2, 1, 3]
                        ventures = [5, 3, 40, 9, 2]
                        return cnt_products, cnt_ventures, matrix, products, ventures
                    