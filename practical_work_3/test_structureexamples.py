import pytest
from practical_work_3.structureexamples import StructureExample, ArrayParts, ArrayWithoutListMethods


class TestStructureExample:
    @pytest.fixture
    def sample_structure(self):
        return StructureExample([1, 2, 3, 4, 5])

    def test_len(self, sample_structure):
        assert len(sample_structure) == 5

    def test_getitem(self, sample_structure):
        assert sample_structure[2] == 3
        with pytest.raises(IndexError):
            sample_structure[10]

    def test_setitem(self, sample_structure):
        sample_structure[2] = 10
        assert sample_structure[2] == 10
        with pytest.raises(IndexError):
            sample_structure[10] = 100

    def test_append(self, sample_structure):
        sample_structure.append(6)
        assert len(sample_structure) == 6
        assert sample_structure[-1] == 6

    def test_insert(self, sample_structure):
        sample_structure.insert(2, 100)
        assert sample_structure[2] == 100
        assert len(sample_structure) == 6

    def test_index(self, sample_structure):
        assert sample_structure.index(3) == 2
        with pytest.raises(ValueError):
            sample_structure.index(10)

    def test_remove(self, sample_structure):
        sample_structure.remove(3)
        assert len(sample_structure) == 4
        with pytest.raises(ValueError):
            sample_structure.remove(10)

    def test_iter(self, sample_structure):
        iter_obj = iter(sample_structure)
        assert next(iter_obj) == 1
        assert next(iter_obj) == 2
        assert next(iter_obj) == 3
        assert next(iter_obj) == 4
        assert next(iter_obj) == 5
        with pytest.raises(StopIteration):
            next(iter_obj)

    def test_delitem(self, sample_structure):
        del sample_structure[2]
        assert len(sample_structure) == 4
        with pytest.raises(IndexError):
            del sample_structure[10]

    def test_extend(self, sample_structure):
        sample_structure.extend([6, 7])
        assert len(sample_structure) == 7
        assert sample_structure[-1] == 7

    def test_clear(self, sample_structure):
        sample_structure.clear()
        assert len(sample_structure) == 0

    def test_pop(self, sample_structure):
        popped_value = sample_structure.pop()
        assert len(sample_structure) == 4
        assert popped_value == 5

    def test_copy(self, sample_structure):
        copied_structure = sample_structure.copy()
        assert len(copied_structure) == len(sample_structure)
        for item1, item2 in zip(copied_structure, sample_structure):
            assert item1 == item2

    def test_reverse(self, sample_structure):
        sample_structure.reverse()
        assert sample_structure[0] == 5
        assert sample_structure[-1] == 1

    def test_count(self, sample_structure):
        assert sample_structure.count(2) == 1
        assert sample_structure.count(10) == 0

    def test_add(self, sample_structure):
        other_structure = StructureExample([6, 7, 8])
        combined_structure = other_structure + sample_structure
        assert len(combined_structure) == 8

    def test_mul(self, sample_structure):
        multiplied_structure = sample_structure * 2
        assert len(multiplied_structure) == 10
        assert multiplied_structure[-1] == 5
        with pytest.raises(TypeError):
            multiplied_structure * 'abc'

    def test_min(self, sample_structure):
        assert sample_structure.min() == 1

    def test_max(self, sample_structure):
        assert sample_structure.max() == 5

    def test_deepcopy(self, sample_structure):
        deep_copied_structure = sample_structure.deepcopy()
        assert len(deep_copied_structure) == len(sample_structure)
        for item1, item2 in zip(deep_copied_structure, sample_structure):
            assert item1 == item2


class TestArrayParts:
    @pytest.fixture
    def array_parts(self):
        return ArrayParts([1, 2, 3])

    def test_len(self, array_parts):
        assert len(array_parts) == 3

    def test_repr(self, array_parts):
        assert repr(array_parts) == "[1, 2, 3]"

    def test_getitem(self, array_parts):
        assert array_parts[0] == 1
        assert array_parts[1] == 2
        assert array_parts[2] == 3
        with pytest.raises(IndexError):
            _ = array_parts[3]

    def test_setitem(self, array_parts):
        array_parts[0] = 10
        assert array_parts[0] == 10
        with pytest.raises(IndexError):
            array_parts[3] = 4

    def test_append(self, array_parts):
        array_parts.append(4)
        assert array_parts[3] == 4

    def test_insert(self, array_parts):
        array_parts.insert(1, 5)
        assert array_parts[1] == 5

    def test_index(self, array_parts):
        assert array_parts.index(3, 0, 3) == 2

    def test_remove(self, array_parts):
        array_parts.remove(2)
        assert len(array_parts) == 2


class TestArrayWithOutList:
    @pytest.fixture
    def array_without_list_methods(self):
        return ArrayWithoutListMethods(1, 2, 3)

    def test_init(self, array_without_list_methods):
        assert len(array_without_list_methods) == 3
        assert array_without_list_methods[0] == 1
        assert array_without_list_methods[1] == 2
        assert array_without_list_methods[2] == 3

    def test_len(self, array_without_list_methods):
        assert len(array_without_list_methods) == 3

    def test_repr(self, array_without_list_methods):
        assert repr(array_without_list_methods) == '[1, 2, 3]'

    def test_getitem(self, array_without_list_methods):
        assert array_without_list_methods[0] == 1
        assert array_without_list_methods[1] == 2
        assert array_without_list_methods[2] == 3

    def test_setitem(self, array_without_list_methods):
        array_without_list_methods[0] = 10
        array_without_list_methods[2] = 30
        assert array_without_list_methods[0] == 10
        assert array_without_list_methods[2] == 30

    def test_append(self, array_without_list_methods):
        array_without_list_methods.append(4)
        assert len(array_without_list_methods) == 4
        assert array_without_list_methods[3] == 4
