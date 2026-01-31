# mypy: disable-error-code="no-untyped-def"

import pytest

from src.category import Category
from src.product import Product


def test_category_init(sample_category):
    """Тест инициализации атрибутов категории"""
    assert sample_category.name == "Электроника"
    assert sample_category.description == "Смартфоны и гаджеты"
    assert len(sample_category.products_in_list) == 2
    assert sample_category.products == (
        "iPhone, 100000.0 руб. Остаток: 2 шт.\n" "Samsung, 80000.0 руб. Остаток: 5 шт.\n"
    )
    assert sample_category.category_count == 1
    assert sample_category.product_count == 2
    assert str(sample_category) == "Электроника, количество продуктов: 7 шт."


def test_category_empty_products(category_empty):
    """Тест инициализации без списка товаров"""

    assert category_empty.products == ""
    assert category_empty.product_count == 0


def test_add_product_increases_count(category_empty, sample_product):
    """Проверяем, что товар добавляется и счетчик Category.product_count растет"""
    initial_count = Category.product_count

    category_empty.add_product(sample_product)

    assert Category.product_count == initial_count + 1
    # Проверяем, что товар действительно в списке (через доступ к приватному полю для теста)
    assert sample_product in category_empty._Category__products


def test_add_multiple_products(category_empty):
    """Проверяем добавление нескольких товаров подряд"""
    prod1 = Product("Samsung", "S23", 100000.0, 10)
    prod2 = Product("Xiaomi", "Mi 13", 50000.0, 20)

    category_empty.add_product(prod1)
    category_empty.add_product(prod2)

    assert category_empty.product_count == 2
    assert len(category_empty.products_in_list) == 2


def test_add_multiple_products_error(category_empty):
    with pytest.raises(TypeError):
        category_empty.add_product("Не товар, а просто строка")

    with pytest.raises(TypeError):
        category_empty.add_product(12345)
