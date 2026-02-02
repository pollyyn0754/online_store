from abc import ABC, abstractmethod
from typing import Self, Union


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs) -> Union[Self, list]:
        pass
