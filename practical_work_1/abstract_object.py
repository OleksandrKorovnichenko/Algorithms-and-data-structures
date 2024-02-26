from abc import ABC, abstractmethod


class AbstractObject(ABC):

    @abstractmethod
    def get_info(self) -> str:
        pass

    def __repr__(self):
        pass
