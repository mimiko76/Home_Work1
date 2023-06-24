# print("task 1(2)")
# digit = str(input("Введите цифру: "))
# length = len(digit)
# digit = int(digit)
# if length < 3 or length > 3:
#     print("Число не трехзначное")
# else:
#     sot = digit // 100
#     des = digit % 100 // 10
#     ed = digit % 10
#     print(ed + des + sot)
#     print(des)

# print("task 2(4)")
# origami = int(input("Сколько всего журавликов сделали дети"))
# sum = origami // 6
# jenya = sum
# petya = sum
# seredja = (sum+sum) * 2
# print(jenya, petya, seredja)
# print(jenya+petya+seredja)

# print("task 3(6)")
# digit = str(input("Введите номер билета: "))
# length = len(digit)
# digit = int(digit)
# if length < 6 or length > 6:
#     print("Число не верное")
# else:
#     a = digit
#     b = a//1000
#     one = b//100
#     two = b % 11
#     three = b % 10
#     c = a % 1000
#     four = c//100
#     five = c % 11
#     six = c % 10
#     if (one + two + three) == (four+five+six):
#         print("Счастливый")
#     else:
#         print("Обычный")

# print("task 4(8)")
# n = int(input("Введите ширину шоколадки:"))
# m = int(input("Введите длину шоколадки"))
# k = int(input("Сколько долек отломить:"))
# if k < n * m and ((k % n == 0) or (k % m == 0)):
#     print('YES')
# else:
#     print('NO')
