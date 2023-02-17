import pytest
from classes import Item

def test_Item():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    item3 = Item(999, "Ноутбук", 20)
    assert len(Item.all) == 2
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000
    item1.apply_discount()
    item2.apply_discount()
    assert item1.price == 8000
    assert item2.price == 16000
    assert Item.all[0].price == 8000

