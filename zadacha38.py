# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

# Примечания о моем решении:
# 1. Отдельные функции для записи файла и дозаписи в файл: чтобы была возможность перезаписать, по желанию, файл полностью.
# 2. Есть проверка введенных пользователем команд на правильность: если команды введены неверно, программа напишет об этом и прервется.
# 3. В начале есть проверка наличия файла и выбор, как поступить, при отсутствии файла.
# 4. За изменение и удаление отвечает одна и та же функция.
# 5. Изменить можно, на выбор, или строку целиком, или одну из ее частей.

import os.path


def tel_write(file):
    how_many_addresses = int(input("Сколько строк хотите записать? "))
    with open(file, "w", encoding = "utf-8") as fd:
        for i in range(0, how_many_addresses):
            string = input("Введите через пробелы фамилию, имя, отчество, номер телефона:")
            fd.write(f"{string}\n")


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
            fd.write(f"{string}\n")


def tel_find(file):
    what_to_search = input("Введите или фамилию, или имя, или отчество, или номер телефона (можно только часть): ")
    tel_book = tel_read_all(file)
    how_many_found = 0
    for line in tel_book:
        if what_to_search in line:
            new_line = line.replace("\n", "")
            print(new_line)
            how_many_found += 1
    if how_many_found == 0:
        print("Нет такой строки в справочнике.")


def tel_change(file, what_to_do):
    what_to_search = input("Введите (можно только частично) или фамилию, или имя, или отчество, или номер телефона: ")
    tel_book = tel_read_all(file)
    indexes_of_found_strings = []
    for i in range(0, len(tel_book)):
        if what_to_search in tel_book[i]:
            print(i, tel_book[i])
            indexes_of_found_strings.append(i)
    if len(indexes_of_found_strings) == 0:
        print("Нет такой строки в справочнике.")
    else:
        index_of_changing_string = indexes_of_found_strings[0]
        if len(indexes_of_found_strings) > 1:
            chosen_index = int(input("Введите индекс нужной из найденных записей: "))
            if chosen_index in set(indexes_of_found_strings):
                index_of_changing_string = chosen_index
            else:
                raise ValueError("Введенный индекс не соответствует найденным строкам.")
        if what_to_do == "C":
            whole_or_part = input("Заменить строку целиком? (Y/N): ")
            if whole_or_part.isalpha() == False or len(whole_or_part) != 1:
                raise ValueError("Введите Y или N")
            if whole_or_part.upper() == "Y":
                del tel_book[index_of_changing_string]
                with open(file, "w", encoding = "utf-8") as fd:
                    for address in tel_book:
                        fd.write(f"{address}\n")
                with open(file, "a", encoding = "utf-8") as fd:
                    new_address = input("Введите через пробелы фамилию, имя, отчество, номер телефона:")
                    fd.write(f"{new_address}\n")
            else:
                what_to_change = input("Введите (целиком) тот элемент записи, который хотите изменить: ")
                to_what_we_change = input("Введите элемент на замену: ")
                how_many_found = 0
                changed_string = tel_book[index_of_changing_string].split()
                for j in range(0, len(changed_string)):
                    if what_to_change == changed_string[j]:
                        changed_string[j] = to_what_we_change
                        how_many_found += 1
                if how_many_found == 0 or how_many_found > 1:
                    raise ValueError("Введите правильно заменяемый элемент.")
                tel_book[index_of_changing_string] = changed_string
                with open(file, "w", encoding = "utf-8") as fd:
                    for address in tel_book:
                        surn, name, patr, number = address
                        fd.write(f"{surn} {name} {patr} {number}\n")
        else:
            print(tel_book)
            del tel_book[index_of_changing_string]
            print(tel_book)
            with open(file, "w", encoding = "utf-8") as fd:
                fd.writelines(tel_book)


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
        what_to_do = input("Что можно сделать с файлом:\n записать заново (W), посмотреть (L), дополнить (A),\n найти запись (F), изменить запись (C), удалить запись (D)\n Выход из программы: (E).\nВведите нужную команду: ")
        if what_to_do.isalpha() == False or len(what_to_do) != 1:
            raise ValueError("Смотрите сокращения команд в начальной строке!")
        what_to_do = what_to_do.upper()
        if what_to_do == "W":
            want_a_rewrite = input("Уверены, что хотите заново заполнить файл? (Y/N): ")
            if want_a_rewrite.isalpha() == False or len(want_a_rewrite) != 1:
                raise ValueError("Введите Y или N")
            if want_a_rewrite.upper() == "Y":
                tel_write(file)
            else:
                exit()
        elif what_to_do == "L":
            tel_print_all(file)
        elif what_to_do == "A":
            tel_add(file)
        elif what_to_do == "F":
            tel_find(file)
        elif what_to_do == "C":
            want_a_change = input("Уверены, что хотите изменить запись? (Y/N): ")
            if want_a_change.isalpha() == False or len(want_a_change) != 1:
                raise ValueError("Введите Y или N")
            if want_a_change.upper() == "Y":
                tel_change(file, what_to_do)
            else:
                exit()
        elif what_to_do == "D":
            want_to_del = input("Уверены, что хотите удалить запись? (Y/N): ")
            if want_to_del.isalpha() == False or len(want_to_del) != 1:
                raise ValueError("Введите Y или N")
            if want_to_del.upper() == "Y":
                tel_change(file, what_to_do)
            else:
                exit()
        else:
            exit()



if __name__ == "__main__":
    main()