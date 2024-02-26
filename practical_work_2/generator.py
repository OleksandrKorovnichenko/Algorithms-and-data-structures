from faker import Faker
from names import get_last_name, get_first_name
from phone_gen import PhoneNumber
from practical_work_1.user_dataclass import User


class Generator:

    @property
    def generate_single(self) -> User:
        """A method of automatically creating an instance of the User class
        with random or selected from a certain list values of each property of the class
        """
        name = get_first_name()
        surname = get_last_name()
        phone = int(PhoneNumber("Ukraine").get_mobile()[1:])
        email = Faker().email()

        return User(name, surname, email, phone)

    def generate_1000(self) -> list:
        """The method of generating 1000 objects of the User class"""
        plist = list()
        for i in range(1000):
            plist.append(self.generate_single)
        return plist

    def generate_10_000(self) -> list:
        """The method of generating 10,000 objects of the User class"""
        plist = [self.generate_single for _ in range(10000)]
        return plist
