from print_data import print_file


def copy_file_number():
    print_file()
    number_from = int(input("Выберит файл, от куда Вы хотите копировать\n"
                       "Введите цифру 1 или 2: "))
    number_where = int(input("Выберит файл,куда Вы хотите копировать\n"
                       "Введите цифру 1 или 2: "))
    while number < 1 or number > 2:
        number = int(input("Ошибка!!!\n"
                           "Введите цифру 1 или 2: "))
    return number
