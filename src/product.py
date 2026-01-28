class Product:
    """Класс для представления товара"""

    name: str  # название
    description: str  # описание
    price: float  # цена
    quantity: int  # количество в наличии

    def __init__(self, name: str, description:str, price: float, quantity: int =0) -> None:
        """Метод для инициализации экземпляра класса"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self) -> str:
        """Метод для отображения информации о товарах"""
        return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"
