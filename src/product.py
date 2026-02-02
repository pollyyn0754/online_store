from typing import Optional, Self, Union

from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс для представления товара"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Метод для инициализации экземпляра класса"""

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    @property
    def cost_product(self) -> float:
        """Вычисляемое свойство для общей стоимости товара на складе"""
        return self.price * self.quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Self) -> float:
        """Сложение объектов по общей стоимости товара на складе"""
        if type(other) is type(self):
            return self.cost_product + other.cost_product
        raise TypeError("Можно складывать только товары одного класса")

    @classmethod
    def new_product(cls, product_data: dict, products_list: Optional[list] = None) -> Union['Product', list]:
        """Класс-метод, который будет принимать на вход параметры товара в словаре
        и возвращать созданный объект или обновляет существующий в списке current_products"""

        # Извлекаем параметры из словаря
        name = product_data.get("name", "")
        description = product_data.get("description", "")
        price = product_data.get("price", 0.0)
        quantity = int(product_data.get("quantity", 0))

        if products_list:
            for prod in products_list:
                if prod["name"] == name:
                    # Складываем количество
                    prod["quantity"] += quantity
                    # Выбираем максимальную цену
                    prod["price"] = max(prod["price"], price)
                    return products_list

        # Если товар не найден в списке или список пуст, создаем новый
        return cls(name, description, price, quantity)

    @property  # type: ignore[no-redef]
    def price(self) -> float:
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для цены с проверками"""
        # проверка введения некорректной цены
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        # если цена товара понижается, пользователь вручную дает согласие через ввод
        # 'y' (значит yes) или 'n' (значит no)
        if new_price < self.__price:
            choice_price = input(f"Цена товара {self.name} понижается. Вы уверены? (y/n): ").lower()
            if choice_price == "y":
                self.__price = new_price
                print("Цена успешно понижена")
            else:
                print("Действие отменено")
        else:
            self.__price = new_price
