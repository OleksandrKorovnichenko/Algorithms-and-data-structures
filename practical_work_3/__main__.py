from practical_work_2.generator import Generator
from practical_work_3.structureexamples import StructureExample
from practical_work_1.user_dataclass import User
from practical_work_1.abstract_object import AbstractObject

if __name__ == "__main__":
    # Створення 5 об'єктів Student
    g = Generator()
    g5 = [g.generate_single() for i in range(5)]
    lst = g5
    tpl = tuple(g5)

    # Створення структур з list/tuple і відображення змісту
    slst1 = StructureExample(tpl)
    print(slst1.__repr__())

    slst2 = StructureExample(lst)
    print(slst2)

    # Перевірка типів даних
    print(type(slst2[0]))
    print(isinstance(slst2[0], User))
    print(isinstance(slst2[0], AbstractObject))

    # Приклад роботи видалення
    print(len(slst1))
    slst1.remove(g5[0])
    print(len(slst1))
