from typing import Union


class ZeroQuantityProduct(Exception):
    def __init__(self, message=None) -> None:
        super().__init__(message)
