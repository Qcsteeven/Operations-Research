from selector import Solution
from tester import Test
from inputer import Input


def main():
    print("Добро пожаловать в решение задачи ЗЛП!")
    task = int(input("Решение какой задачи вы хотите получить?\n 1 - Двойственная задача методом искусственных переменных\n 2 - Транспортная задача\n"))
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
