# mypy: disable-error-code="no-untyped-def"
import pytest


from src.order import Order


def test_order_product(sample_product):
    order = Order(sample_product)
    assert order.quantity == 1
    assert order.final_price == 95000.0
    assert str(order) == "Заказ: Samsung Galaxy S23, количество: 1 шт., итоговая стоимость: 95000.00"


def test_order_lawngrass(product_la1):
    order = Order(product_la1, quantity=3)
    assert order.quantity == 3
    assert order.final_price == 1500.0
    assert str(order) == "Заказ: Газонная трава, количество: 3 шт., итоговая стоимость: 1500.00"


def test_order_smartphone(product_smartphone_sample1):
    order = Order(product_smartphone_sample1, quantity=2)
    assert order.quantity == 2
    assert order.final_price == 420000.0
    assert str(order) == "Заказ: Iphone 15, количество: 2 шт., итоговая стоимость: 420000.00"


def test_order_value_error(sample_product):
    with pytest.raises(ValueError):
        Order(sample_product, -1)


def test_order_attribute_error(sample_product):
    with pytest.raises(AttributeError):
        Order.add_product(sample_product, 1)
