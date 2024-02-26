import pytest
from practical_work_2.generator import Generator
from practical_work_1.user_dataclass import User


class TestGenerator:

    @pytest.fixture
    def init_student(self):
        """Preparation for tests
        """
        return User("Name", "Surname", "test@exeple.com", 380500823600)

    def test_gen_single_types(self):
        g = Generator()
        st = g.generate_single
        assert isinstance(st, User)
        assert isinstance(st.name, str)
        assert isinstance(st.surname, str)
        assert isinstance(st.email, str)
        assert isinstance(st.phone, int)

    def test_gen_1000_type(self):
        g = Generator()
        slist = g.generate_1000()
        assert isinstance(slist, list)
        assert isinstance(slist[0], User)
        assert len(slist) == 1000

    def test_gen_10_000_type(self):
        g = Generator()
        slist = g.generate_10_000()
        assert isinstance(slist, list)
        assert isinstance(slist[0], User)
        assert len(slist) == 10000
