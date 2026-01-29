
from typing import Optional

from src.product import Product


class Category:
    """Класс для представления категорий товаров"""

    name: str  # название
    description: str  # описание
    products: list  # список товаров категории
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: Optional[list]=None) -> None:
        """Метод для инициализации категорий товаров"""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products) if products else 0

    def add_product(self, product: Product) -> None:
        """Метод для добавления товара в приватный список"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        products_str = ''
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    @property
    def products_in_list(self) -> list:
        return self.__products

    def __repr__(self) -> str:
        """Метод для отображения информации о категориях товаров"""
        return f"Category(name='{self.name}', products_count={len(self.__products)})"
