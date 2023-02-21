import csv, pprint


class Item:
    """
    Класс для учета товаров
    """
    all = list()  # список созданных объектов на основании данного класса
    discount = 20  # скидка

    def __init__(self, name: str, price: (int, float),
                 item_count: int):

        # часть кода конструктора, проверяющая, что длина имени товара, вводимая в первый раз, не превышает 10 символов
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception(
                "Длина наименования товара превышает 10 символов.")

        self.__name = name
        self.price = price
        self.item_count = item_count
        if all([type(self.__name) == str,
                type(self.price) in (int, float),
                type(self.item_count) == int]):
            Item.all.append(self)
        else:
            print(
                f"Проверьте типы данных вводимых аргументов для объекта с именем '{self.__name}'")

    def calculate_total_price(self):
        """
        Функция, которая возвращает общую стоимость товара
        :return:    (int, float)
        """
        return self.price * self.item_count

    def apply_discount(self):
        """
        Функция, которая применяет скидку к товару
        :return:    (int, float)
        """
        self.price = self.price * (1 - self.discount / 100)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self.__name = value
        else:
            raise Exception(
                "Длина наименования товара превышает 10 символов.")

    @classmethod
    def instantiate_from_csv(cls,
                             path="database/items.csv"):
        with open(path) as file:
            file = csv.DictReader(file)
            for row in file:
                item = cls(name=row["name"],
                           price=float(row["price"]),
                           item_count=int(row["quantity"]))

    @staticmethod
    def is_integer(value):
        if all([type(value) in (int, float),
                value % 1 == 0]):
            return True
        return False
