# Задача 1(10)
# n = int(input("Введите количество монет:"))
# orel = int(input("Введите количество монет вверх орлом:"))
# gerb = int(input("Введите количество монет вверх гербом:"))
# if orel+gerb != n:
#     print("Вы ввели не правильное количество перевернутых монет")
# else:
#     if orel < gerb:
#         print(str(orel) + " монет нужно перевернуть")
#     else:
#         print(str(gerb) + " монет нужно перевернуть")

# Задача2(12)
# print("Загадайте два числа и введите сумму этих чисел и их произведение")
# sum = int(input("Введите сумму чисел: "))
# pro = int(input("Введите их произведение: "))
# i=0
# sum2 = sum // 2
# sum3 = sum // 2
# while True:
#      if i ==1000:
#          print("числа не совместимы:")
#          break
#      if (sum2 * sum3) == pro:
#          print("загаданные числа " + str(sum2) + " и " + str(sum3))
#          break
#      if ((sum2-1) * sum3) == pro:
#           sum2-=1
#      if (sum2* (sum3+1))==pro:
#           sum3+=1
#      else: 
#          sum2-=1
#          sum3+=1
#      i+=1

# Задача 3(14)
# n = int(input())
# i = 0
# while 2 ** i <= n:
#     print(2 ** i)
#     i += 1