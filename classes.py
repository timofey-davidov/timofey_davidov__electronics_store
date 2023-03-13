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
            self._name = name
        else:
            raise Exception(
                "Длина наименования товара превышает 10 символов.")

        self.price = price
        self.item_count = item_count
        if all([type(self._name) == str,
                type(self.price) in (int, float),
                type(self.item_count) == int]):
            Item.all.append(self)
        else:
            print(
                f"Проверьте типы данных вводимых аргументов для объекта с именем '{self._name}'")

    def __repr__(self):
        return f"Item({self._name}, {self.price}, {self.item_count})"

    def __str__(self):
        return self._name

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
        return self._name

    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self._name = value
        else:
            raise Exception("Длина наименования товара превышает 10 символов.")

    @classmethod
    def instantiate_from_csv(cls, path="database/items.csv"):
        try:
            with open(path) as file:
                file = csv.DictReader(file)
                for row in file:
                    item = cls(name=row["name"], price=float(row["price"]), item_count=int(row["quantity"]))
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл базы данных (item.csv)")
        except KeyError:
            raise InstantiateCSVError('Файл item.csv поврежден')

    @staticmethod
    def is_integer(value):
        if all([type(value) in (int, float),
                value % 1 == 0]):
            return True
        return False

    def __add__(self, other):
        if isinstance(self, Item) and isinstance(other, Item):
            return self.item_count + other.item_count


class Phone(Item):
    def __init__(self, name: str, price: (int, float), item_count: int, number_of_sim: int = 1):
        super().__init__(name, price, item_count)
        if self.check_numbers_of_sim(number_of_sim):
            self._number_of_sim = number_of_sim

    @staticmethod
    def check_numbers_of_sim(value):
        if not isinstance(value, int) or value < 1:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        return True

    def __repr__(self):
        return f"Phone({self._name}, {self.price}, {self.item_count}, {self._number_of_sim})"

    def __str__(self):
        return super().__str__()

    def __add__(self, other):
        if isinstance(self, (Phone, Item)) and isinstance(other, (Phone, Item)):
            return self.item_count + other.item_count

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value: int):
        self.check_numbers_of_sim(value)
        self._number_of_sim = value

class MixinKeyBoard:
    def __init__(self, name, price, item_count):
        self._language = "EN"
        super().__init__(name, price, item_count)

    @property
    def language(self):
        return self._language

    @staticmethod
    def check_language(value):
        if value.lower() not in ("ru", "en"):
            raise AttributeError("Язык должен быть EN или RU")
        return True

    def change_lang(self):
        if self._language == "EN":
            self._language = "RU"
        else:
            self._language = "EN"
class KeyBoard(MixinKeyBoard, Item):
    def __init__(self, name: str, price: (int, float), item_count: int):
        super().__init__(name, price, item_count)

class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Файл item.csv поврежден'

if __name__ == '__main__':
    print(type(Exception))