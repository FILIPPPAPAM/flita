set1 = set()
set2 = set()


# Функция для преобразования к целому числу
def preob_k_int(string):
    count = 0
    for i in string:
        if i in '1234567890':
            count += 1
        else:
            return string
    if count == len(string):
        return int(string)


# Функция для ввода элементов в множество
def input_set(s, name):
    try:
        items = input("Введите элементы множества {} через пробел: ".format(name))
        array_of_items = items.split(' ')
        for i in array_of_items:
            item = preob_k_int(i)
            s.add(item)
    except:
        print("Ошибка ввода, попробуйте еще раз\n")
    a = input('Вывести элементы множества? y/n: ')
    if a == 'y':
        print_set(s, name)


# Функция для вывода элементов множества
def print_set(s, name):
    if len(s) == 0:
        print("Множество пусто\n")
    else:
        print("Элементы множества {}\n:".format(name))
        for elem in s:
            print(elem)


# Функция для добавления элемента в множество
def add_to_set(s, name):
    elem = preob_k_int(input("Введите элемент, который нужно добавить в множество {}: ".format(name)))
    if elem not in s:
        s.add(elem)
        print("Элемент ", elem, " успешно добавлен\n")
    else:
        print("Элемент ", elem, " уже есть в множестве {}\n".format(name))
    a = input('Вывести элементы множества? y/n: ')
    if a == 'y':
        print_set(s, name)


# Функция для удаления элемента из множества
def remove_from_set(s, name):
    elem = preob_k_int(input("Введите элемент, который нужно удалить из множества {}: ".format(name)))
    if elem in s:
        s.remove(elem)
        print("Элемент ", elem, " успешно удален из множества\n")
    else:
        print("Элемент ", elem, " не найден в множестве\n")
    a = input('Вывести элементы множества? y/n: ')
    if a == 'y':
        print_set(s, name)


def main():
    try:
        print('Программа для работы с множествами. Есть два множества: множество 1 и множество 2.')
        while True:
            flag = True
            print('Выберите, с каким множеством будете работать:')
            print('Множество 1 - 1. множество 2 - 2')
            r = int(input('Введите ваш ответ: '))
            if r == 1:
                while True:
                    print('\nВот команды, которые я могу исполнить:')
                    print('Ввести элементы в множество - 1')
                    print('Вывести все элементы множества - 2')
                    print('Добавить один элемент в множество - 3')
                    print('Удалить один элемент из множества - 4')
                    print('Сменить множество - 5')
                    print('Завершить выполнение - 6\n')
                    comand = int(input('Введите номер команды: '))
                    match comand:
                        case 1:
                            input_set(set1, '1')
                        case 2:
                            print_set(set1, '1')
                        case 3:
                            add_to_set(set1, '1')
                        case 4:
                            remove_from_set(set1, '1')
                        case 5:
                            break
                        case 6:
                            flag = False
                            break
                        case _:
                            print('Такой команды нет')
            elif r == 2:
                while True:
                    print('\nВот команды, которые я могу исполнить:')
                    print('Ввести элементы в множество - 1')
                    print('Вывести все элементы множества - 2')
                    print('Добавить один элемент в множество - 3')
                    print('Удалить один элемент из множества - 4')
                    print('Сменить множество - 5')
                    print('Завершить выполнение - 6\n')
                    comand = int(input('Введите номер команды: '))
                    match comand:
                        case 1:
                            input_set(set2, '2')
                        case 2:
                            print_set(set2, '2')
                        case 3:
                            add_to_set(set2, '2')
                        case 4:
                            remove_from_set(set2, '2')
                        case 5:
                            break
                        case 6:
                            flag = False
                            break
                        case _:
                            print('Такой команды нет\n')
                if flag == False:
                    break
            else:
                print('Такого множества нет\n')
    except:
        print('Похоже это не число, попробуйте позже.\n')
        main()


main()
