"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


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
    assert len(Item.all)==5

