from selector import Solution
from tester import Test
from inputer import Input


def main():
    print("Добро пожаловать в решение задачи ЗЛП!")
    print("Решение какой задачи вы хотите получить?")
    print("1 - Двойственная задача методом искусственных переменных")
    print("2 - Транспортная задача")
    print("3 - Задача целочисленного программирования")
    print("4 - Решение задачи об оптимальном использовании оборудования методом симплекс-таблиц ")
    task = int(input())
    choose = input("1 - Самостоятельный ввод, 2 - Тестовые данные: ")
    args = []
    if choose == "1":
        args = Input.input(task)
    else:
        args = Test.test(task)
    solution = Solution(*args)
    solution(task)


if __name__ == "__main__":
    main()
