import pytest
import csv

file_csv = 'C:/Users/Денис/Desktop/Курс разработчик Python/Project_4_kurs/electronics-shop-project/src/items.csv'


class InstantiateCSVError(Exception):
    """Файл поврежден"""

    def __str__(self):
        return 'Файл item.csv поврежден'


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
    def instantiate_from_csv(cls, file=file_csv):

        cls.all.clear()
        try:
            with open(file) as csvfile:
                reader = csv.DictReader(csvfile)
                count = 0  # Счетчик подсчета строк и вывода заголовков столбцов
                for row in reader:
                    if list(row.keys()) == ['name', 'price', 'quantity']:
                        Item(row['name'], row['price'], row['quantity'])
                        count += 1
                    else:
                        raise InstantiateCSVError
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')
        except InstantiateCSVError:
            raise InstantiateCSVError

    @staticmethod
    def string_to_number(data):
        return int(float(data))
