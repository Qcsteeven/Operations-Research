class Test:
    @classmethod
    def test(cls):
        start, end = 1, 6
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
                case _:
                    print(f"Неверный ввод! Введите число от {
                          start} до {end}: ")
                    case = input(f"Какой тест({start} - {end}): ")
