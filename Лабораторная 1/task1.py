# TODO: Подробно описать три произвольных класса
from typing import Union


class Tree:
    def __init__(self, variety: str, height: (int, float)):
        if not isinstance(variety, (str)):
            raise TypeError("Сорт дерева должен быть типа str")
        self.variety = variety

        if not isinstance(height, (int, float)):
            raise TypeError("Высота дерева должна быть типа int или float")
        if height < 0:
            raise ValueError("Высота дерева не может быть отрицательным числом")
        self.height = height

    def is_tall_tree(self) -> bool:
        if self.height > 15:
            return (True)
        else:
            return (False)

    def trim_the_tree(self, lenght: float) -> None:
        if not isinstance(lenght, (int, float)):
            raise TypeError("Срезаемая часть дерева должна быть типа int или float")
        if lenght < 0 and lenght > self.height:
            raise ValueError("Срезаемая часть дерева должна положительным числом и меньше высоты дерева")
        self.height = self.height - lenght
        return self.height


class Car:
    def __init__(self, brand: str, speed: (int, float)):
        if not isinstance(brand, (str)):
            raise TypeError("Марка машины должна быть типа str")
        self.brand = brand

        if not isinstance(speed, (int, float)):
            raise TypeError("Скорость должна быть типа int или float")
        if speed < 0:
            raise ValueError("Скорость не может быть отрицательным числом")
        self.speed = speed

    def parking(self) -> bool:
        if self.speed == 0:
            return (True)
        else:
            return (False)

    def increase_speed(self, new_speed: float) -> None:
        if not isinstance(new_speed, (int, float)):
            raise TypeError("Добавляемая скорость должна быть типа int или float")
        if new_speed < 0:
            raise ValueError("Добавляемая скорость должна положительным числом")
        self.speed = self.speed + new_speed
        return self.speed


class Cat:
    def __init__(self, breed: str, weight: (float, int)):
        if not isinstance(breed, (str)):
            raise TypeError("Порода кота должна быть типа str")
        self.breed = breed

        if not isinstance(weight, (int, float)):
            raise TypeError("Вес кошки должен быть типа int или float")
        if weight < 0:
            raise ValueError("Вес кошки не может быть отрицательным числом")
        self.weight = weight

    def presence_of_breed(self) -> bool:
        if self.breed != None:
            return (True)
        else:
            return (False)

    def feed_the_cat(self, food: float) -> None:
        if not isinstance(food, (int, float)):
            raise TypeError("Вес еды должен быть типа int или float")
        if food < 0:
            raise ValueError("Вес еды должен быть положительным числом")
        self.weight = self.weight + food
        return self.weight
