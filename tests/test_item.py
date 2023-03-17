import pytest
from src.item import Item


item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)
Item.pay_rate = 0.8
"""Здесь надо написать тесты с использованием pytest для модуля item."""
def test_calculate_total_price():

    assert item1.__name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20

    assert item2.__name == "Ноутбук"
    assert item2.price == 20000
    assert item2.quantity == 5

def test_apply_discount():
    item1.price = item1.price * Item.pay_rate
    assert item1.price == 8000.0
    item2.price = item2.price * Item.pay_rate
    assert item2.price == 16000

    