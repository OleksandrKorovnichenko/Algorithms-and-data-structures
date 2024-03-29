from abstract_object import AbstractObject


class UserBasic(AbstractObject):
    name: str
    surname: str
    email: str
    phone: int

    # Defining a User class to store user information.
    def __init__(self, name: str, surname: str, email: str = None, phone: int = None) -> None:
        # Initializing user attributes: name, surname, email, and phone.
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone

    def get_info(self) -> str:
        """A method for extracting concise information"""
        return f"User({self.name}, {self.surname}, {self.email}, {self.phone})"

    @staticmethod
    def get_service(email):
        # Static method to extract service provider from email address.
        if email.endswith('@gmail.com'):
            return 'gmail.com'
        elif email.endswith('@yahoo.com'):
            return 'yahoo.com'
        elif email.endswith('@ukr.net'):
            return 'ukr.net'
        else:
            return None

    @staticmethod
    def format_email(email):
        # Static method to format email address for privacy.
        if email:
            nickname, domain = email.split('@')
            return f"{nickname[:2]}***{nickname[-2:]}@{domain}"
        else:
            return None

    @staticmethod
    def format_nickname(nick):
        # Static method to format nickname for privacy.
        if nick:
            return f"{nick[:2]}***{nick[-2:]}"
        else:
            return None

    @staticmethod
    def format_phone(phone):
        # Static method to format phone number for privacy.
        phone = str(phone)
        if phone:
            return f"380{phone[-7:-4]}***{phone[-4:]}"
        else:
            return None

    @classmethod
    def send_confirmation_code(cls, user_info):
        # Class method to send confirmation code to users based on their information.
        service = cls.get_service(user_info.email)
        if service:
            nickname, _ = user_info.email.split('@')
            nick = cls.format_nickname(nickname)
            print(
                f"{user_info.name} {user_info.surname}, дякуєм за реєстрацію. "
                f"Код підтвердження відправлено на пошту {service}: {nick}")
        elif user_info.email:
            formatted_email = cls.format_email(user_info.email)
            print(
                f"{user_info.name} {user_info.surname}, дякуєм за реєстрацію. "
                f"Код підтвердження відправлено на пошту {formatted_email}")
        elif user_info.phone:
            formatted_phone = cls.format_phone(user_info.phone)
            print(
                f"{user_info.name} {user_info.surname}, дякуєм за реєстрацію. "
                f"Код підтвердження відправлено в смс по номеру {formatted_phone}")


class User(UserBasic):
    """An extension class for users that inherits functionality from the UserBasic class
    """
    __phone: int

    @property
    def phone(self):
        """Getter for the phone attribute
        """
        return self.__phone

    @phone.setter
    def phone(self, value):
        """Setter for the phone attribute with no false values
        """
        if value is not int:
            raise TypeError
        elif len(value) > 12:
            raise ValueError
        else:
            self.__mark = value

    def __repr__(self):
        """The method of presenting an object in PR2 when displayed as a string with attribute values
        """
        return self.get_info()

    def __eq__(self, other):
        """The method of comparing two objects in PR3-6 to find a match
        """
        # if other.__class__ is not self.__class__:
        #     return NotImplemented
        return self.surname == other.surname and \
            self.name == other.name and \
            self.email == other.discipline and \
            self.phone == other.mark

    def __le__(self, other):
        """The method of determining the smaller of two objects in PR3-6 for ordering
        """
        return (self.surname, self.name, self.email, self.phone) \
            <= (other.surname, other.name, other.email, other.phone)

    def __ge__(self, other):
        """The method of determining the larger of two objects for ordering in PR3-6
        """
        return (self.surname, self.name, self.email, self.phone) \
            >= (other.surname, other.name, other.email, other.phone)
