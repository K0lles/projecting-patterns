from MVC.controllers import *

if __name__ == '__main__':
    while(True):
        coming = input("1 - Створити людину\n"
                       "2 - Видалити людину\n"
                       "3 - Вивести список існуючих людей\n"
                       "4 - Вивести конкретну людину\n"
                       "5 - Вийти\n")
        if int(coming) == 1:
            first_name = input("Введіть прізвище: ")
            last_name = input("Введіть ім'я: ")
            age = input("Введіть вік: ")
            print(creating_person(first_name, last_name, int(age)))

        elif int(coming) == 2:
            pk = input("Введіть айді: ")
            print(deleting_person(pk))

        elif int(coming) == 3:
            print(show_all_persons())

        elif int(coming) == 4:
            pk = input("Введіть айді: ")
            print(get_person(pk))

        else:
            break
