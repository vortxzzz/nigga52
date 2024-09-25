def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Ошибка: Пожалуйста, введите корректное число.")


def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Ошибка: Пожалуйста, введите целое число.")


def main():
    while True:
        print("\nВыберите действие:")
        print("1. число в степени")
        print("2. x,z,b")
        print("3. число n")
        print("0. Выход")

        choice = input("Введите номер вашего выбора: ")

        if choice == '0':
            print("Выход из программы.")
            break

        if choice in ('1', '2', '3'):
            if choice == '1':
                a = get_float("Введите число: ")
                a2 = a * a
                a3 = a * a2
                a5 = a2 * a3
                a10 = a5 * a5
                a13 = a10 * a3
                print('Ваше число в степени 13:', a13)

            elif choice == '2':
                x = get_float("Введите первое число (x): ")
                b = get_float("Введите второе число (b): ")
                z = get_float("Введите третье число (z): ")

                if x + b + z < 1:
                    if x < b and x < z:
                        x = (b + z) / 2
                    elif b < x and b < z:
                        b = (x + z) / 2
                    else:
                        z = (x + b) / 2
                else:
                    if x < b:
                        x = (z + b) / 2
                    else:
                        b = (x + z) / 2

                print("Измененные значения:")
                print("x =", x)
                print("b =", b)
                print("z =", z)

            elif choice == '3':
                n = get_int("Введите число n: ")
                s = 0
                for k in range(1, n + 1):
                    s += (1 / k)
                print("Сумма гармонического ряда для n =", n, ":", s)

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

main()
