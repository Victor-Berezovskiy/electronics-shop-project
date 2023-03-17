import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, __name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param __name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = __name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        if len(new_name) > 10:
            raise Exception("Длина наименования товара превышает 10 символов.")
        self.__name = new_name

    @classmethod
    def instantiate_from_csv(cls, csv_path='../src/items.csv'):
        with open(csv_path) as file:
            file_reader = csv.DictReader(file, delimiter=',')
            for i in file_reader:
                name, price, quantity = i.get('name'), int(i.get('price')), int(i.get('quantity'))
                cls.all.append((name, price, quantity))

    @classmethod
    def set_pay_rate(cls, new_rate):

        if 0 <= new_rate:
            cls.__pay_rate = new_rate
        else:
            raise ValueError("Значение индексации не может быть отрицательным или равным '0'")

    @staticmethod
    def string_to_number(number: str) -> int:
        """Cтатический метод, возвращающий число из числа-строки
        :return: Число в нужном нам формате
        """
        return int(number.split(".")[0])

    def __str__(self):
        """Тандер для вывода информации об экземпляре"""
        return f"{self.__name}"

    def __repr__(self):
        """Тандер для вывода информации об экземпляре"""
        return f"Item{self.__name, self.price, self.quantity}"

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def item_info(self):
        return f'Общая стоимость товара {self.__name} = {self.price}'

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate
        return self.price

