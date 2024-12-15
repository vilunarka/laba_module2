class Tree:
    """
       >>> tree = Tree("Pine", 30)
       >>> tree.trim_the_tree(12)
       '18'
       >>> tree.get_variety_tree()
       'Pine'
       >>> tree.hybridization("Larch")
       'Гибридизация исходного дерева и Larch'
    """

    def __init__(self, variety: str, height: [int, float]):
        """
        Создаёт объект дерева.
        :param variety: Сорт дерева.
        :param height: Высота дерева.
        """
        self.variety = variety
        self.height = height

    def get_variety_tree(self) -> str:
        """
        Возвращает сорт дерева.
        """
        return f"{self.variety}"

    def hybridization(self, add_tree: str) -> str:
        """
        Гибридизация дерева.
        :param add_tree: Название дерева, соединенного с исходным.
        :return: Уведомление, сообщающее об гибридизации.
        """
        return f"Гибридизация исходного дерева и {add_tree}"

    def trim_the_tree(self, lenght: float) -> None:
        """
        Проверяет высоту дерева со срезом.
        :param lenght: срезаемая часть .
        :return: остаток дерева.
        """
        if lenght < 0:
            raise ValueError("Размер файла должен быть положительным числом")
        if lenght < self.height:
            return f"{self.height - lenght}"
        return f"{self.height}"


class Car:
    """
        >>> car = Car("Opel", 0)
        >>> car.parking()
        True
        >>> car.increase_speed(20)
        '20'
    """

    def __init__(self, brand: str, speed: [int, float]):
        """
        Создаёт объект машины.
        :param brand: Марка машины.
        :param speed: Скорость машины.
        """
        self.brand = brand
        self.speed = speed

    def parking(self) -> bool:
        """
        Проверяет стоит ли машина.
        :return: True или False.
        """
        if self.speed == 0:
            return (True)
        else:
            return (False)

    def increase_speed(self, new_speed: [int, float]) -> None:
        """
        Увеличение скорости.
        :param new_speed: Добавляемая скорость.
        :return: Итоговая скорость.
        """
        if not isinstance(new_speed, (int, float)):
            raise TypeError("Добавляемая скорость должна быть типа int или float")
        if new_speed < 0:
            raise ValueError("Добавляемая скорость должна положительным числом")
        self.speed = self.speed + new_speed
        return f"{self.speed}"

class Cat:
    """
    >>> cat = Cat("Sphinx", 5)
    >>> cat.presence_of_breed()
    True
    >>> cat.feed_the_cat(0.2)
    '5.2'
    """

    def __init__(self, breed: str, weight: [float, int]):
        """
        Создаёт объект кота.
        :param breed: Порода кота.
        :param weight: Вес кота.
        """
        if not isinstance(breed, str):
            raise TypeError("Порода кота должна быть типа str")
        self.breed = breed

        if not isinstance(weight, (int, float)):
            raise TypeError("Вес кошки должен быть типа int или float")
        if weight < 0:
            raise ValueError("Вес кошки не может быть отрицательным числом")
        self.weight = weight

    def presence_of_breed(self) -> bool:
        """
        Проверяет есть ли порода у кота.
        :return: True или False.
        """
        if self.breed != None:
            return (True)
        else:
            return (False)

    def feed_the_cat(self, food: float) -> None:
        """
        Кормление кота.
        :param food: Количество корма.
        :return: Итоговый вес кота.
        """
        if not isinstance(food, (int, float)):
            raise TypeError("Вес еды должен быть типа int или float")
        if food < 0:
            raise ValueError("Вес еды должен быть положительным числом")
        self.weight = self.weight + food
        return f"{self.weight}"
