from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from practical_work_1.abstract_object import AbstractObject


@dataclass(order=True)
class User(AbstractObject):
    name: str
    surname: str
    email: str
    phone: int
    __phone: int = field(init=False)

    def get_info(self) -> str:
        """A method for extracting concise information"""
        return f"User({self.name}, {self.surname}, {self.email}, {self.__phone})"

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

    def send_confirmation_code(self):
        # Class method to send confirmation code to users based on their information.
        service = self.get_service(self.email)
        if service:
            nickname, _ = self.email.split('@')
            nick = self.format_nickname(nickname)
            return f"{self.name} {self.surname}, дякуєм за реєстрацію. " \
                   f"Код підтвердження відправлено на пошту {service}: {nick}"
        elif self.email:
            formatted_email = self.format_email(self.email)
            return f"{self.name} {self.surname}, дякуєм за реєстрацію. " \
                   f"Код підтвердження відправлено на пошту {formatted_email}"
        elif self.phone:
            formatted_phone = self.format_phone(self.phone)
            return f"{self.name} {self.surname}, дякуєм за реєстрацію. " \
                   f"Код підтвердження відправлено в смс по номеру {formatted_phone}"

    @property
    def phone(self):
        """Getter for the phone attribute"""
        return self.__phone

    @phone.setter
    def phone(self, value):
        """Setter for the phone attribute with no false values"""
        if type(value) != int:
            raise TypeError("Phone must be an integer")
        else:
            self.__phone = value

    def __repr__(self):
        """The method of presenting an object when displayed as a string with attribute values"""
        return self.get_info()
