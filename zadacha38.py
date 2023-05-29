# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

# Примечания о моем решении:
# 1. Отдельные функции для записи файла и дозаписи в файл: чтобы была возможность перезаписать, по желанию, файл полностью.
# 2. Есть проверка введенных пользователем команд на правильность: если команды введены неверно, программа напишет об этом и прервется.
# 3. В начале есть проверка наличия файла и выбор, как поступить, при отсутствии файла.

import os.path


def tel_write(file):
    how_many_addresses = int(input("Сколько строк хотите записать? "))
    with open(file, "w", encoding = "utf-8") as fd:
        for i in range(0, how_many_addresses):
            string = input("Введите через пробелы фамилию, имя, отчество, номер телефона:")
            fd.write(f"{string};\n")


def tel_read_all(file):
    with open(file, encoding = "utf-8") as fd:
        strings = fd.readlines()
    return strings


def tel_print_all(file):
    tel_book = tel_read_all(file)
    for line in tel_book:
        new_line = line.replace(",", "")
        new_line = new_line.replace("\n", "")
        print(new_line)


def tel_add(file):
    how_many_addresses = int(input("Сколько строк хотите добавить? "))
    with open(file, "a", encoding = "utf-8") as fd:
        for i in range(0, how_many_addresses):
            string = input("Введите через пробелы фамилию, имя, отчество, номер телефона:")
            fd.write(f"{string};\n")


def tel_find(file):
    what_to_search = input("Введите или фамилию, или имя, или отчество, или номер телефона (можно только часть): ")
    tel_book = tel_read_all(file)
    for line in tel_book:
        if what_to_search in line:
            new_line = line.replace("\n", "")
            print(new_line)


def main():
    while True:
        file = "address_book.txt"
        if os.path.isfile(file) == False:
            does_file_exist = input("Не найдено данного файла в папке, к которой обращается эта программа. \n Файл существует? (Y/N): ")
            if does_file_exist.isalpha() == False or len(does_file_exist) != 1:
                raise ValueError("Введите Y или N")
            if does_file_exist.upper() == "Y":
                print("Положите файл в папку с этой программой и снова запустите программу.")
                exit()
            else:
                write_it_or_not = input("Хотите создать такой файл? (Y/N): ")
                if write_it_or_not.isalpha() == False or len(write_it_or_not) != 1:
                    raise ValueError("Введите Y или N")
                if write_it_or_not.upper() == "Y":
                    tel_write(file)
                else:
                    exit()
        what_to_do = input("Что можно сделать с файлом: записать заново (W), посмотреть (L), дополнить (A), найти запись (F). \n Выход из программы: (E). \n Введите нужную команду: ")
        if what_to_do.isalpha() == False or len(what_to_do) != 1:
            raise ValueError("Смотрите сокращения команд в начальной строке!")
        what_to_do = what_to_do.upper()
        if what_to_do == "W":
            want_a_rewrite = input("Уверены, что хотите заново заполнить файл? (Y/N): ")
            if want_a_rewrite.isalpha() == False or len(want_a_rewrite) != 1:
                raise ValueError("Введите Y или N")
            if want_a_rewrite == "Y":
                tel_write(file)
            else:
                exit()
        elif what_to_do == "L":
            tel_print_all(file)
        elif what_to_do == "A":
            tel_add(file)
        elif what_to_do == "F":
            tel_find(file)
        else:
            exit()


if __name__ == "__main__":
    main()