# mypy: disable-error-code="no-untyped-def"


from src.category import Category


def test_category_init(sample_category):
    """Тест инициализации атрибутов категории"""
    assert sample_category.name == "Электроника"
    assert sample_category.description == "Смартфоны и гаджеты"
    assert len(sample_category.products) == 2


def test_category_counts(sample_category, category_empty):
    """Тест подсчета количества категорий и товаров"""
    # category_electronics создала 1 категорию и 2 товара
    # category_empty создала еще 1 категорию и 0 товаров
    assert Category.category_count == 2
    assert Category.product_count == 2


def test_category_repr(sample_category):
    """Тест строкового представления"""
    assert repr(sample_category) == "Category(name='Электроника', products_count=2)"


def test_empty_category_products(category_empty):
    """Тест инициализации без списка товаров"""
    assert category_empty.products == []
