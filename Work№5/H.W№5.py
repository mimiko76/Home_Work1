# Задача 26
# def recurs_erection(arg1, arg2):
#     if (arg2 == 1):
#         return arg1
#     if (arg2 != 1):
#         return (arg1 * recurs_erection(arg1, arg2 - 1))


# base = int(input("Введите число: "))
# exp = int(input("Введите его степень: "))
# print("Результат возведения в степень равен:", recurs_erection(base, exp))

# Задача 28
def sum(a, b):
    if b == 0:
        return a
    else:
        return sum(a ^ b, (a & b) << 1)


base = int(input("Введите число: "))
exp = int(input("Введите второе число: "))
print("Сумма равна:", sum(base, exp))
