# text = str(input("Введите стих мишки"))
# words = text.split()
# result = ""
# for word in words:
#     if word[-1] in ",.!?":
#         result += "Парам "
#     else:
#         result += "пам "
# print(result.strip())

def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows+1):
        for j in range(1, num_columns+1):
            print(operation(i, j), end="\t")
        print()


print_operation_table(lambda x, y: x * y)
