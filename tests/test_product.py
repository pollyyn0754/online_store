# mypy: disable-error-code="no-untyped-def"
import pytest

from src.product import Product


def test_product_init(sample_product):
    """Тест инициализации атрибутов"""
    assert sample_product.name == "Samsung Galaxy S23"
    assert sample_product.description == "256GB, Gray"
    assert sample_product.price == 95000.0
    assert sample_product.quantity == 5


def test_product_str(sample_product):
    """Тест строкового представления"""
    assert str(sample_product) == "Samsung Galaxy S23, 95000.0 руб. Остаток: 5 шт."


def test_price_setter_increase(sample_product):
    """Тест повышения цены (без подтверждения)"""
    sample_product.price = 100000.0
    assert sample_product.price == 100000.0


def test_price_setter_negative(sample_product, capsys):
    """Тест попытки установить некорректную цену"""
    sample_product.price = -10000
    captured = capsys.readouterr()
    assert captured.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"

    assert sample_product.price == 95000.0


def test_price_setter_decrease_confirm(sample_product, monkeypatch):
    """Тест снижения цены с подтверждением 'y'"""
    monkeypatch.setattr("builtins.input", lambda _: "y")
    sample_product.price = 80000.0
    assert sample_product.price == 80000.0


def test_price_setter_decrease_cancel(sample_product, monkeypatch):
    """Тест отмены снижения цены 'n'"""
    monkeypatch.setattr("builtins.input", lambda _: "n")
    sample_product.price = 80000.0
    assert sample_product.price == 95000.0


def test_new_product_creation():
    """Тест создания нового продукта через classmethod"""
    data = {"name": "Samsung", "description": "Android", "price": 80000.0, "quantity": 10}
    new_obj = Product.new_product(data)
    assert isinstance(new_obj, Product)
    assert new_obj.name == "Samsung"


def test_new_product_update_existing():
    """Тест обновления существующего продукта (сложение количества и выбор макс. цены)"""
    data = {"name": "Samsung Galaxy S23", "description": "128gb", "price": 120000.0, "quantity": 5}
    new_data = [
        {
            "name": "Samsung Galaxy S23",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    ]
    updated_product = Product.new_product(data, new_data)

    assert updated_product == [
        {
            "name": "Samsung Galaxy S23",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 10,
        }
    ]


def test_product_add_sample(product_cost1, product_cost2):
    assert (product_cost1 + product_cost2) == 2580000.0


def test_product_add_error(product_cost1):
    with pytest.raises(TypeError):
        product_cost1 + 1
