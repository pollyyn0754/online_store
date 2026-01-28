import pytest


from src.product import Product
from src.category import Category

@pytest.fixture
def sample_product():
    """Фикстура для создания тестового экземпляра товара"""
    return Product(
        name="Samsung Galaxy S23",
        description="256GB, Gray",
        price=95000.0,
        quantity=5
    )

@pytest.fixture
def sample_category():
    """Фикстура для создания категории с товарами"""
    # Обнуляем счетчики перед тестом, чтобы они не накапливались от предыдущих запусков
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("iPhone", "Apple", 100000.0, 2)
    p2 = Product("Samsung", "Android", 80000.0, 5)

    return Category("Электроника", "Смартфоны и гаджеты", [p1, p2])


@pytest.fixture
def category_empty():
    """Фикстура для пустой категории"""
    return Category("Книги", "Художественная литература")