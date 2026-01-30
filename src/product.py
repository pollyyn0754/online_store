from typing import Optional, Self, Union


class Product:
    """Класс для представления товара"""

    name: str  # название
    description: str  # описание
    price: float  # цена
    quantity: int  # количество в наличии
    cost_product = 0.0

    def __init__(self, name: str, description: str, price: float, quantity: int = 0) -> None:
        """Метод для инициализации экземпляра класса"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.cost_product = price * quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return self.cost_product + other.cost_product

    @classmethod
    def new_product(cls, product_data: dict, products_list: Optional[list] = None) -> Union[Self, list]:
        """Класс-метод, который будет принимать на вход параметры товара в словаре
        и возвращать созданный объект или обновляет существующий в списке current_products"""

        # Извлекаем параметры из словаря
        name = product_data.get("name", "")
        description = product_data.get("description", "")
        price = round(product_data.get("price", 0.0))
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
