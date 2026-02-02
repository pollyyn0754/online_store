# mypy: disable-error-code="no-untyped-def"
import pytest


def test_product_smartphone_init(product_smartphone_sample1):
    assert product_smartphone_sample1.name == "Iphone 15"
    assert product_smartphone_sample1.description == "512GB, Gray space"
    assert product_smartphone_sample1.price == 210000.0
    assert product_smartphone_sample1.quantity == 8
    assert product_smartphone_sample1.efficiency == 98.2
    assert product_smartphone_sample1.model == "15"
    assert product_smartphone_sample1.memory == 512
    assert product_smartphone_sample1.color == "Gray space"


def test_product_smartphone_add(product_smartphone_sample1, product_smartphone_sample2):
    assert product_smartphone_sample1 + product_smartphone_sample2 == 2114000.0


def test_product_smartphone_add_error(product_smartphone_sample1):
    with pytest.raises(TypeError):
        product_smartphone_sample1 + 1
