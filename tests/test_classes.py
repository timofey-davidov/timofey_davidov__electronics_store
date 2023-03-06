import pytest
from classes import Item, Phone


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

@pytest.fixture
def item5():
    return Phone("iPhone 14", 120_000, 5, 2)

@pytest.fixture
def item6():
    return Phone("Xiaomi 12t", 38_000, 11, 1)


def test_Item(item1, item2):
    assert len(Item.all) == 2
    assert item1.calculate_total_price() == 200_000
    assert item2.calculate_total_price() == 100_000
    item1.apply_discount()
    item2.apply_discount()
    assert item1.price == 8_000
    assert item2.price == 16_000
    assert Item.all[0].price == 8_000

def test_Item_repr_str(item1):
    assert item1.__repr__() == 'Item(Смартфон, 10000, 20)'
    assert item1.__str__() == "Смартфон"


def test_instantiate_from_csv():
    assert len(Item.all) == 3
    Item.instantiate_from_csv()
    assert len(Item.all) == 8


def test_is_integer():
    assert Item.is_integer(5) == True
    assert Item.is_integer(5.0) == True
    assert Item.is_integer(7.5) == False

def test_Phone(item5, item6):
    assert item5.__str__() == "iPhone 14"
    assert item6.__repr__() == "Phone(Xiaomi 12t, 38000, 11, 1)"
    assert item5 + item6 == 16
    assert item6 + 100 == None
