import pytest
from practical_work_1.user_dataclass import User


class TestStudentClass:
    """Checking the basic actions of the User class
    """

    @pytest.fixture
    def init_student(self):
        """Preparation for tests
        """
        return User("Name", "Surname", "test@exeple.com", 380500823600)

    def test_data_type(self, init_student):
        """Class compliance check"""
        assert isinstance(init_student, User)

    def test_check_init(self, init_student):
        """Verification of initiation and data entry
        """

        s = init_student
        assert s.name == "Name"
        assert s.surname == "Surname"
        assert s.email == "test@exeple.com"
        assert s.phone == 380500823600

    @pytest.mark.skip("For demonstration purposes")
    def test_get_info(self, init_student):
        """Checking the get_info() method
        """
        assert init_student.get_info() == "User(Name, Surname, test@exeple.com, 380500823600)"

    values_to_try = [User("User", "test1", "test1@exeple.com", 380500823601),
                     User("User", "test2", "test2@exeple.com", 380500823602),
                     User("User", "test3", "test3@exeple.com", 380500823603),
                     User("User", "test4", "test4@exeple.com", 380500823604),
                     User("User", "test5", "test5@exeple.com", 380500823605),
                     User("User", "test6", "test6@exeple.com", 380500823606),
                     User("User", "test7", "test7@exeple.com", 380500823607),
                     User("User", "test8", "test8@exeple.com", 380500823608)]

    @pytest.mark.parametrize('user', values_to_try)
    def test_get_message(self, user):
        """Checking send_confirmation_code() for correct values
        """
        assert user.send_confirmation_code()


class TestStudentErrors:
    """Basic class error checking User
    """

    @pytest.fixture
    def student(self):
        return User("User", "test7", "test7@exeple.com", 380500823607)

    @pytest.mark.xfail
    def test_wrong_name_type(self, user):
        user.name = 5645
        assert type(user.name) == str

    @pytest.mark.xfail
    def test_wrong_disc_type(self, user):
        user.email = True
        assert isinstance(user.email, str)

    def test_mark_type_error(self):
        """We expect a TypeError error when running the test
        """
        with pytest.raises(TypeError):
            User("User", "test1", "test1@exeple.com", "380500823601")

    values_to_try = [
        ("User", "test1", "test1@exeple.com", -380500823601),
        ("User", "test2", "test2@exeple.com", 380500823602),
        ("User", "test3", "test3@exeple.com", 380500823603),
        ("User", "test4", "test4@exeple.com", 380500823604),
        ("User", "test5", "test5@exeple.com", 380500823605),
        ("User", "test6", "test6@exeple.com", 380500823606),
        ("User", "test7", "test7@exeple.com", 380500823607),
        ("User", "test8", "test8@exeple.com", 380500823608)
    ]

    @pytest.mark.xfail
    @pytest.mark.parametrize('name, surname, email, phone', values_to_try)
    def test_mark_value_error(self, name, surname, email, phone):
        with pytest.raises(ValueError):
            User(name, surname, email, phone)


class TestStudentComparison:

    @pytest.fixture
    def user(self):
        """Preparation for tests
        """
        return [User("User", "test1", "test1@exeple.com", 380500823601),
                User("User", "test2", "test2@exeple.com", 380500823602),
                User("User", "test3", "test3@exeple.com", 380500823603)]

    def test_repr(self, user):
        """Checking __repr__
        """
        assert str(user[0]) == "User(User, test1, test1@exeple.com, 380500823601)"

    def test_equals(self, user):
        """Checking the equality of objects
        """
        assert user[0] == User("User", "test1", "test1@exeple.com", 380500823601)

    def test_less(self, user):
        """Check if the first object is not equal to the second
        """
        assert user[0] != user[1]

    def test_greater(self, user):
        """Check if the first object is not equal to the third
        """
        assert user[0] != user[2]
