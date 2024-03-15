from copy import deepcopy
from typing import Union

from practical_work_3.abstractstructure import AbstractStructureBasic, AbstractStructureExtended
from practical_work_1.abstract_object import AbstractObject
from collections.abc import Iterable


class StructureExample(AbstractStructureExtended):
    """Класс реалізації структури на основі list і основних його методів
    """

    def __init__(self, *args: AbstractObject | Iterable[AbstractObject]):
        """Ініціалізація окремими значеннями або ітерируємою структурою (list, tuple, ...) з даними
        :param args: Кортеж аргументів змінної довжини з об'єктами або структурою (Iterable) з даними
        """
        self._list: list[AbstractObject] = []  # внутрішній масив для зберігання даних
        self.__iter_index = 0  # індекс ітератора

        if args and isinstance(args[0], AbstractObject):
            for element in args:
                self._list.append(element)  # додавання окремих перелічених об'єктів до внутрішнього масиву
        if args and isinstance(args[0], Iterable):
            self._list.extend(args[0])  # додавання елементів структури до внутрішнього масиву

    def __len__(self) -> int:
        return len(self._list)

    def __repr__(self) -> str:
        return str(self._list)

    def __getitem__(self, item):
        try:
            return self._list[item]
        except IndexError:
            raise IndexError("getitem: index out of range")  # Виключення про вихід за межі існуючих індексів

    def __setitem__(self, key, value):
        try:
            self._list[key] = value
        except IndexError:
            raise IndexError("setitem: index out of range")

    def append(self, value: AbstractObject) -> None:
        self._list.append(value)

    def insert(self, index: int, value: AbstractObject) -> None:
        self._list.insert(index, value)

    def index(self, value: AbstractObject, start: int = 0, stop: int = -1) -> int:
        if stop == -1:
            stop = len(self._list)
        try:
            return self._list.index(value, start, stop)
        except IndexError:
            raise IndexError("index: Для наочності ")

    def remove(self, value: AbstractObject) -> None:
        try:
            self._list.remove(value)
        except ValueError:
            raise ValueError("remove: value is not exists")  # Помилка за відсутності вказаного об'єкта в структурі

    def __iter__(self) -> Iterable:
        return self

    def __next__(self) -> AbstractObject:
        if self.__iter_index >= len(self._list):
            raise StopIteration("Ending elements")
        result = self._list[self.__iter_index]
        self.__iter_index += 1
        return result

    def __delitem__(self, key):
        del self._list[key]

    def extend(self, values: Iterable[AbstractObject]) -> None:
        self._list.extend(values)

    def clear(self) -> None:
        self._list.clear()

    def pop(self, index: int = -1):
        return self._list.pop(index)

    def copy(self):
        return self._list.copy()

    def reverse(self) -> None:
        self._list.reverse()

    def count(self, value: AbstractObject) -> int:
        return self._list.count(value)

    def __add__(self, other: AbstractStructureBasic) -> AbstractStructureBasic:
        if not isinstance(other, StructureExample):
            raise TypeError("Unsupported operand type for +")
        return StructureExample(self._list + other._list)

    def __mul__(self, scalar: int) -> AbstractStructureBasic:
        if not isinstance(scalar, int):
            raise TypeError("Unsupported operand type for multiplication")
        return StructureExample(self._list * scalar)

    def min(self) -> AbstractObject:
        return min(self._list)

    def max(self) -> AbstractObject:
        return max(self._list)

    def deepcopy(self) -> AbstractStructureBasic:
        return StructureExample(deepcopy(self._list))


class ArrayParts(AbstractStructureBasic):
    __array: list[AbstractObject | None]
    __size: int
    __reserved: int

    def __init__(self, *args: AbstractObject | Iterable[AbstractObject]):
        self.__array = [None] * 10  # [None, None, None, None, None, None, None, None, None, None]
        self.__size = 0
        self.__reserved = 10  # Загальний розмір масиву - кількість зберігаємих об'єктів + зарезервовані місця

        if len(args) == 1 and isinstance(args[0], Iterable):
            iterable = list(args[0])  # Convert the generator to a list
            if len(iterable) >= self.__reserved:
                self.__size_extending(self.__reserved + len(iterable))
            for element in iterable:
                self.append(element)

    def __size_extending(self, max_size=-1) -> None:
        new_array = [None] * max_size
        for i in range(self.__size):
            new_array[i] = self.__array[i]
        self.__array = new_array
        self.__reserved = max_size

    def __len__(self) -> int:
        return self.__size

    def __repr__(self) -> str:
        return repr(self.__array[:self.__size])

    def __getitem__(self, item):
        if isinstance(item, int) and item >= self.__size:
            raise IndexError("Out of index")

        if isinstance(item, slice):
            if item.step is None or item.step >= 0:
                if item.stop is None:
                    item = slice(item.start, self.__size, item.step)
                elif item.stop > self.__size:
                    raise IndexError("Out of index")
            else:
                if item.start is None:
                    item = slice(
                        self.__size - 1 if item.start is None else item.start, item.stop, item.step)
                elif item.start > self.__size - 1:
                    raise IndexError("Out of index")
        return self.__array[item]

    def __setitem__(self, key, value):
        if isinstance(key, int):
            if 0 <= key < self.__size:
                self.__array[key] = value
                return
        raise IndexError("Out of index")

    def append(self, value: AbstractObject) -> None:
        if self.__size >= self.__reserved - 1:
            self.__size_extending()  # розширення масива вдвічі, якщо вичерпано всі зарезервовані місця
        self.__array[self.__size] = value
        self.__size += 1

    def insert(self, index: int, value: AbstractObject):
        self.__array.insert(index, value)

    def index(self, value: AbstractObject, start: int, stop: int) -> int:
        return self.__array.index(value, start, stop)

    def remove(self, value: AbstractObject) -> None:
        if value not in self.__array:
            raise ValueError("Value not found in the array")

        index = self.__array.index(value)
        self.__array.pop(index)
        self.__size -= 1


class ArrayWithoutListMethods(AbstractStructureBasic):
    def __init__(self, *args: Union[int, Iterable[Union[int, float]]]):
        self.__array = {}
        self.__size = 0

        if len(args) == 1 and isinstance(args[0], Iterable):
            for element in args[0]:
                self.append(element)
        else:
            for element in args:
                self.append(element)

    def __getitem__(self, index: int) -> Union[int, float]:
        if isinstance(index, int) and index >= self.__size:
            raise IndexError("Out of index")
        return self.__array[index]

    def __setitem__(self, index: int, value: Union[int, float]) -> None:
        if isinstance(index, int):
            if 0 <= index < self.__size:
                self.__array[index] = value
                return
        raise IndexError("Out of index")

    def append(self, value: Union[int, float]) -> None:
        self.__array[self.__size] = value
        self.__size += 1

    def remove_duplicates(self) -> None:
        unique_elements = list(set(self.__array.values()))
        self.__array = {index: value for index, value in enumerate(unique_elements)}
        self.__size = len(unique_elements)

    def sort(self) -> None:
        values = list(self.__array.values())
        values.sort()
        self.__array = {index: value for index, value in enumerate(values)}

    def index(self, value: Union[int, float]) -> int:
        for index, val in self.__array.items():
            if val == value:
                return index
        raise ValueError(f"{value} is not in array")

    def insert(self, index: int, value: Union[int, float]) -> None:
        if index < 0 or index > self.__size:
            raise IndexError("Out of index")
        self.__array[index + 1:self.__size + 1] = self.__array[index:self.__size]
        self.__array[index] = value
        self.__size += 1

    def remove(self, value: Union[int, float]) -> None:
        for index, val in self.__array.items():
            if val == value:
                del self.__array[index]
                self.__size -= 1
                return
        raise ValueError(f"{value} is not in array")

    def __len__(self) -> int:
        return self.__size

    def __repr__(self) -> str:
        return str(list(self.__array.values()))
