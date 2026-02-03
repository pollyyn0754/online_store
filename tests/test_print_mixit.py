# mypy: disable-error-code="no-untyped-def"
from src.lawngrass_product import LawnGrass
from src.product import Product
from src.smartphone_product import Smartphone


def test_print_mixit(capsys):
    Product("Samsung Galaxy S23", "256GB, Gray", 95000.0, 5)
    massage = capsys.readouterr()
    assert massage.out.strip() == "Product(Samsung Galaxy S23, 256GB, Gray, 95000.0, 5)"

    LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    massage = capsys.readouterr()
    assert massage.out.strip() == "LawnGrass(Газонная трава 2, Выносливая трава, 450.0, 15)"

    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    massage = capsys.readouterr()
    assert massage.out.strip() == "Smartphone(Iphone 15, 512GB, Gray space, 210000.0, 8)"
