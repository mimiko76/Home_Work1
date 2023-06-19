import io
#___________________
file_path = "/Users/alinalevina/Desktop/Phyton_work/GBWork/Seminars/L.8 working with files/file.txt"

def show_all_records():
    i = 1
    with(open(file_path,"r",encoding="utf-8")) as _data:
        for line in _data:
            PhoneBook_data = line.replace(";", " ")
            print(f"{i}:{PhoneBook_data}",end="")
            i+=1

def search_record(name):
    end = False
    with io.open(file_path, encoding='utf-8') as file:
        for line in file:
            if name.lower() in line.split(";")[0].lower():
                line = line.replace(";", " ")
                fam,name,surname,num = line.split()
                print (f"Фамилия: {fam}")
                print (f"Имя: {name}")
                print (f"Отчество: {surname}")
                print (f"Номер телефона: {num}")
                end = True
    if end == False:
        print("Не существует такого контакта")


def add_contact(name,num):
    with open(file_path, "a", encoding="utf-8") as f:
        f.write("\n")
        f.write(name.replace(" ",";"))
        f.write(";")
        f.write(num)

def del_contact(name):
        change = int(input("Если хотите удалить контакт нажмите 1, если нет нажмите 2"))
        if change == 1:
            with open(file_path, 'r') as file:
                lines = file.readlines()
            with open(file_path, 'w') as file:
                for line in lines:
                    if name not in line.lower():
                        file.write(line)
        if change == 2:
            print("контакт не удален")


def change_contact(word_to_replace, new_word):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    with open(file_path, 'w') as file:
        for line in lines:
            if word_to_replace in line:
                line = line.replace(word_to_replace, new_word)
            file.write(line)

def main():
    print("Выберите действие: 1 - показать справочник, " 
          "2 - найти контакт, " 
          "3 - добавить контакт, "
          "4 - удалить контакт"
          "5 - изменить контакт")
    select = int(input())
    if select == 1:
        show_all_records()
    elif select == 2:
        name = input("Введите фамилию: ")
        search_record(name)
    elif select == 3:
        name = input("Введите ФИО через пробел: ")
        num = input("Введите номер: ")
        add_contact(name,num)
    elif select == 4:
        name = input("Введите фамилию: ")
        del_contact(name)
    elif select == 5:
        word_to_replace =input("Введите ФИО или номер телефона которые нужно заменить: ")
        new_word = input("Введите новое значение: ")
        change_contact(word_to_replace, new_word)
main()