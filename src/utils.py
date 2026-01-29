import json
import os
from typing import List

from src.category import Category
from src.product import Product


def read_json(file_path: str) -> List:
    """Загружает данные из JSON и создает объекты классов."""
    if not os.path.exists(file_path):
        print(f"Ошибка: Файл по пути {file_path} не найден.")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return list(data)
    except json.JSONDecodeError:
        print(f"Ошибка: Файл {file_path} содержит некорректный JSON.")
        return []
    except Exception as e:
        print(f"Непредвиденная ошибка при чтении файла: {e}")
        return []


def create_object_from_json(data: List) -> List:
    categories = []
    for category_data in data:
        try:
            # Создаем список объектов Product
            products = [
                Product(p["name"], p["description"], p["price"], p["quantity"])
                for p in category_data.get("products", [])
            ]

            # Создаем объект Category
            category = Category(
                name=category_data["name"], description=category_data["description"], products=products
            )
            categories.append(category)

        except KeyError as e:
            print(f"Ошибка: В данных отсутствует обязательное поле {e}")
            continue  # Пропускаем некорректную категорию

    return categories
