# mypy: disable-error-code="no-untyped-def"
import pytest


def test_product_laungrass_init(product_la1):
    assert product_la1.name == "Газонная трава"
    assert product_la1.description == "Элитная трава для газона"
    assert product_la1.price == 500.0
    assert product_la1.quantity == 20
    assert product_la1.country == "Россия"
    assert product_la1.germination_period == "7 дней"
    assert product_la1.color == "Зеленый"


def test_product_laungrass_add(product_la1, product_la2):
    assert product_la1 + product_la2 == 16750.0


def test_product_laungrass_add_error(product_la1):
    with pytest.raises(TypeError):
        product_la1 + 1
