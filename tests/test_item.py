"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone
from src.item import InstantiateCSVError


@pytest.fixture
def item_fixture():
    return Item('Ноутбук', 1000, 20)


def test_calculate_total_price():
    object_ = Item('Name', 10, 2)

    assert object_.calculate_total_price() == 20


def test_apply_discount():
    Item.pay_rate = 0.5
    object_ = Item('Name', 10, 50)
    object_.apply_discount()
    assert object_.price == 5


def test_set_name():
    object_ = Item('Бур', 5, 10)
    object_.name = 'Тур'
    assert object_.name == 'Тур'
    object_.name = 'Суперсмартфон'
    assert object_.name == 'Тур'
    object_.name = '141'
    assert object_.name == 'Тур'
    object_.name = 150
    assert object_.name == 'Тур'


def test_string_to_number():
    assert Item.string_to_number('15.6') == 15


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_FileNotFoundError_errors(item_fixture):
    with pytest.raises(FileNotFoundError):
        item_fixture.instantiate_from_csv(
            file='C:/Users/Денис/Desktop/Курс разработчик Python/Project_4_kurs/electronics-shop-project/src/it.csv')


def test_InstantiateCSVError_errors(item_fixture):
    """Убрал поле с данными"""
    with pytest.raises(InstantiateCSVError):
        item_fixture.instantiate_from_csv(
            file='C:/Users/Денис/Desktop/Курс разработчик '
                 'Python/Project_4_kurs/electronics-shop-project/src/uncorrect_items.csv')


def test_InstantiateCSVError_errors_data(item_fixture):
    """Добавил новое поле"""
    with pytest.raises(InstantiateCSVError):
        item_fixture.instantiate_from_csv(
            file='C:/Users/Денис/Desktop/Курс разработчик '
                 'Python/Project_4_kurs/electronics-shop-project/src/uncorrect_items_data.csv')



def test_repr_str():
    """ Test repr and str method"""
    item = Item("Телефон", 10, 50)
    assert repr(item) == "Item('Телефон', 10, 50)"
    assert str(item) == 'Телефон'


def test_add_item():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
