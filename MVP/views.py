import presenters

if __name__ == '__main__':
    while True:
        coming = input("1 - Створити людину\n"
                       "2 - Вивести список існуючих людей\n"
                       "3 - Вийти\n")
        if int(coming) == 1:
            name = input("Введіть ім'я: ")
            surname = input("Введіть прізвище: ")
            age = input("Введіть вік: ")
            print(presenters.add_person(name, surname, int(age)))

        elif int(coming) == 2:
            print(presenters.show_all_persons())

        else:
            break
