class Item:
    """
    Класс для учета товаров
    """
    all = list()        # список созданных объектов на основании данного класса
    discount = 20       # скидка

    def __init__(self, name: str, price: (int, float), item_count: int):
        self.name = name
        self.price = price
        self.item_count = item_count
        if all([type(self.name) == str, type(self.price) in (int, float), type(self.item_count) == int]):
            Item.all.append(self)
        else:
            print(f"Проверьте типы данных вводимых аргументов для объекта с именем '{self.name}'")

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
        self.price = self.price * (1-self.discount/100)