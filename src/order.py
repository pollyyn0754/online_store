from src.base_entity import BaseEntity
from src.product import Product


class Order(BaseEntity):

    def __init__(self, product: Product, quantity: int = 1) -> None:
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным")
        self.__ordered_product = Product(
            name=product.name, description=product.description, price=product.price, quantity=quantity
        )
        self.__final_price = self.__ordered_product.price * quantity

    @property
    def product(self) -> Product:
        """Геттер для получения товара из заказа."""
        return self.__ordered_product

    @property
    def quantity(self) -> int:
        """Геттер для получения количества товара в заказе."""
        return self.__ordered_product.quantity

    @property
    def final_price(self) -> float:
        """Геттер для итоговой стоимости."""
        return self.__final_price

    def __str__(self) -> str:
        """Строковое представление заказа."""
        return (
            f"Заказ: {self.product.name}, "
            f"количество: {self.product.quantity} шт., "
            f"итоговая стоимость: {self.final_price:.2f}"
        )

    def add_product(self, product: Product) -> None:
        raise AttributeError("Невозможно добавить товар в существующий заказ")
