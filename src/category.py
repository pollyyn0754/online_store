from typing import Optional

from src.base_entity import BaseEntity
from src.product import Product


class Category(BaseEntity):
    """Класс для представления категорий товаров"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: Optional[list] = None) -> None:
        """Метод для инициализации категорий товаров"""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products) if products else 0

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        """Метод для добавления товара в приватный список"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products_in_list(self) -> list:
        return self.__products

    @property  # type: ignore[no-redef]
    def products(self) -> str:
        """Геттер, который будет выводить список товаров в виде строк"""
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str
