from task import Cat, Car, Tree

if __name__ == "__main__":
    pine = Tree("Сосна", 20)
    automobile = Car("Opel", 110)
    siamese_cat = Cat("Сиамский", 5)

    try:
        pine.height(-10)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        automobile.increase_speed(-20)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        siamese_cat.breed(10)
    except TypeError:
        print('Ошибка: неправильные данные')
