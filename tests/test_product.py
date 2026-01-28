# mypy: disable-error-code="no-untyped-def"


def test_product_init(sample_product):
    """Тест инициализации атрибутов"""
    assert sample_product.name == "Samsung Galaxy S23"
    assert sample_product.description == "256GB, Gray"
    assert sample_product.price == 95000.0
    assert sample_product.quantity == 5

def test_product_repr(sample_product):
    """Тест строкового представления"""
    assert repr(sample_product) == "Product(name='Samsung Galaxy S23', price=95000.0, quantity=5)"