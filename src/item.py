import pytest
import csv

file_csv = 'items.csv'


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """


        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
        super().__init__()

    def __str__(self) -> str:
        return f'{self.__name}'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __add__(self, other):
        if issubclass(other.__class__, Item) == False:
            raise TypeError('Складывать можно только объекты Phone и Item')
        return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        all_sum = self.price * self.quantity

        return all_sum

    def apply_discount(self, ) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        # return self.price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) <= 10 and name.isdigit() is not True:
            self.__name = name
        else:
            print("False name or invalid")

    @classmethod
    def instantiate_from_csv(cls):

        file = '../src/items.csv'
        cls.all.clear()
        with open(file) as csvfile:
            reader = csv.DictReader(csvfile)
            count = 0  # Счетчик подсчета строк и вывода заголовков столбцов
            # print(reader)
            for row in reader:
                # if count == 0:
                # Вывод строки, содержащей заголовки для столбцов
                # print(f'Файл содержит столбцы: {", ".join(row)}')
                # Вывод строк
                # print(f' {row["name"]} - {row["price"]},  {row["quantity"]}', end=' \n')
                Item(row['name'], row['price'], row['quantity'])

                count += 1
            # print(f'Всего в файле {count + 1} строк.')

    @staticmethod
    def string_to_number(data):
        return int(float(data))
