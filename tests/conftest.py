# mypy: disable-error-code="no-untyped-def"
import pytest

from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator


@pytest.fixture
def sample_product():
    """Фикстура для создания тестового экземпляра товара"""
    return Product("Samsung Galaxy S23", "256GB, Gray", 95000.0, 5)


@pytest.fixture
def product_no_quantity():
    """Фикстура товара без указания количества"""
    return Product("Case for iPhone", "Silicone, Black", 500.0)


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
    # Обнуляем счетчики перед тестом, чтобы они не накапливались от предыдущих запусков
    Category.category_count = 0
    Category.product_count = 0
    return Category("Книги", "Художественная литература")


@pytest.fixture
def sample_data():
    return [
        {
            "name": "Смартфоны",
            "description": "Техника",
            "products": [{"name": "Iphone 15", "description": "128gb", "price": 90000.0, "quantity": 5}],
        }
    ]


@pytest.fixture
def product_iterator(sample_category):
    return ProductIterator(sample_category)


@pytest.fixture
def product_cost1():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

@pytest.fixture
def product_cost2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)