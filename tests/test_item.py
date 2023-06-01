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
