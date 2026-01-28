from typing import Optional


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
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.products) if products else 0

    def __repr__(self) -> str:
        """Метод для отображения информации о категориях товаров"""
        return f"Category(name='{self.name}', products_count={len(self.products)})"
