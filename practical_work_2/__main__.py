from generator import Generator
from practical_work_1.user_dataclass import User

if __name__ == "__main__":
    us = User("Іван", "Іванов", "ivan@yahoo.com", 38097123435455)
    print(us.get_info())
    print(us)

    g = Generator()
    print(g.generate_single)

    g1000 = g.generate_1000()
    print(g1000)

    print(g1000[100].send_confirmation_code())
    print(g1000[101].send_confirmation_code())
    print(g1000[102].send_confirmation_code())
    print(g1000[103].send_confirmation_code())
    print(g1000[104].send_confirmation_code())
    print(g1000[999].send_confirmation_code())
