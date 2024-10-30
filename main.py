from selector import Solution
from tester import Test
from inputer import Input


def main():
    print("Добро пожаловать в решение задачи ЗЛП!")
    choose = input("1 - Самостоятельный ввод, 2 - Тестовые данные: ")
    args = []
    if choose == "1":
        args = Input.input()
    else:
        args = Test.test()
    solution = Solution(*args)
    solution()


if __name__ == "__main__":
    main()
