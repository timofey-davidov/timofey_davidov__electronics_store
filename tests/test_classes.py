import pytest
from classes import Item


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def item2():
    return Item("Ноутбук", 20000, 5)


@pytest.fixture
def item3():
    return Item(999, "Ноутбук", 20)


@pytest.fixture
def item4():
    return Item("СуперПуперНоутбук", 20000, 5)


def test_Item(item1, item2):
    assert len(Item.all) == 2
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000
    item1.apply_discount()
    item2.apply_discount()
    assert item1.price == 8000
    assert item2.price == 16000
    assert Item.all[0].price == 8000


def test_instantiate_from_csv():
    assert len(Item.all) == 2
    Item.instantiate_from_csv()
    assert len(Item.all) == 7


def test_is_integer():
    assert Item.is_integer(5) == True
    assert Item.is_integer(5.0) == True
    assert Item.is_integer(7.5) == False
