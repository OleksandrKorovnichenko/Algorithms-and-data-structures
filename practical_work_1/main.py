"""Account registration"""


class User:
    # Defining a User class to store user information.
    def __init__(self, name, surname, email=None, phone=None):
        # Initializing user attributes: name, surname, email, and phone.
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone


class ConfirmationSystem:
    # ConfirmationSystem class to handle confirmation code sending logic.
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


# Creating a list of users with different input data
users = [
    User("Іван", "Іванов", email="ivan@yahoo.com", phone="38097123435455"),
    User("Петро", "Петров", email="petro@gmail.com", phone="380971234561"),
    User("Марія", "Сидорова", email="maria@ukr.net", phone="380971234786"),
    User("Тарас", "Тарасов", email="", phone="380971236765"),
    User("Олександ", "Олександров", email="sasha@example.com", phone="380971233343"),
]

# Calling the method for each user
for user in users:
    ConfirmationSystem.send_confirmation_code(user)
