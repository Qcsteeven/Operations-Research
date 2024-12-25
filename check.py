from itertools import product

# Исходные данные переменных и их округлений
variables = [
    {"original": 5.0, "down": 5, "up": 5},       # x11
    {"original": 0.0, "down": 0, "up": 0},       # x12
    {"original": 0.0, "down": 0, "up": 0},       # x13
    {"original": 3.0, "down": 3, "up": 3},       # x21
    {"original": 0.0, "down": 0, "up": 0},       # x22
    {"original": 0.0, "down": 0, "up": 0},       # x23
    {"original": 19.2264, "down": 19, "up": 20},  # x31
    {"original": 20.7736, "down": 20, "up": 21},  # x32
    {"original": 0.0, "down": 0, "up": 0},       # x33
    {"original": 9.0, "down": 9, "up": 9},       # x41
    {"original": 0.0, "down": 0, "up": 0},       # x42
    {"original": 0.0, "down": 0, "up": 0},       # x43
    {"original": 0.783, "down": 0, "up": 1},     # x51
    {"original": 1.217, "down": 1, "up": 2},     # x52
    {"original": 0.0, "down": 0, "up": 0}        # x53
]

# Проверка равенств
def check_equalities(x):
    return (
        x[0] + x[1] + x[2] == 5 and
        x[3] + x[4] + x[5] == 3 and
        x[6] + x[7] + x[8] == 40 and
        x[9] + x[10] + x[11] == 9 and
        x[12] + x[13] + x[14] == 2
    )

# Проверка неравенств
def check_inequalities(x, xi):
    y1 = 100 * x[0] + 400 * x[3] + 20 * x[6] + 200 * x[9] + 600 * x[12]
    y2 = 15 * x[1] + 200 * x[4] + 25 * x[7] + 50 * x[10] + 250 * x[13]
    y3 = 100 * x[2] + 150 * x[5] + 200 * x[8] + 25 * x[11] + 350 * x[14]
    return y1 >= 2 * xi and y2 >= xi and y3 >= 3 * xi

# Поиск оптимального округления
def find_optimal_rounding(variables):
    optimal_solution = None
    optimal_xi = float('inf')

    # Перебор всех комбинаций округлений
    for rounding in product(["down", "up"], repeat=len(variables)):
        x = [variables[i][rounding[i]] for i in range(len(variables))]

        # Проверяем, выполняются ли равенства
        if check_equalities(x):
            # Находим минимально возможное ξ, при котором выполняются неравенства
            y1 = 100 * x[0] + 400 * x[3] + 20 * x[6] + 200 * x[9] + 600 * x[12]
            y2 = 15 * x[1] + 200 * x[4] + 25 * x[7] + 50 * x[10] + 250 * x[13]
            y3 = 100 * x[2] + 150 * x[5] + 200 * x[8] + 25 * x[11] + 350 * x[14]
            m = min(y1, y2, y3)
            p = [2, 1, 3]
            y = [y1, y2, y3]
            for i in range(len(y)):
                if y[i] == m:
                    xi = y[i] / p[i]
            if check_inequalities(x, xi):
                print(xi, x)

    return optimal_solution, optimal_xi

# Основной код
optimal_solution, optimal_xi = find_optimal_rounding(variables)

# Вывод результата
if optimal_solution:
    print("Оптимальное округление:")
    for i, value in enumerate(optimal_solution):
        print(f"x{i + 1} = {value}")
    print(f"Минимальное значение ξ: {optimal_xi:.2f}")
else:
    print("Не удалось найти подходящее решение.")
