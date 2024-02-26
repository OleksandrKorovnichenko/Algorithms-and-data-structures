from user_dataclass import User



if __name__ == "__main__":
    # Creating a list of users with different input data
    users = [
        User("Іван", "Іванов", email="ivan@yahoo.com", phone=38097123435455),
        User("Петро", "Петров", email="petro@gmail.com", phone=380971234561),
        User("Марія", "Сидорова", email="maria@ukr.net", phone=380971234786),
        User("Тарас", "Тарасов", email="", phone=380971236765),
        User("Олександ", "Олександров", email="sasha@example.com", phone=380971233343),
    ]

    # Calling the method for each user
    for user in users:
        User.send_confirmation_code(user)
