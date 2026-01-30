# mypy: disable-error-code="no-untyped-def"
import pytest


def test_product_iterator_sample(product_iterator):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "iPhone"
    assert next(product_iterator).name == "Samsung"

    with pytest.raises(StopIteration):
        next(product_iterator)
