from _datetime import datetime


def get_employees(employe, age):
    print(datetime.now().date())
    print(f"Принят сотрудник {employe} возрастом {age}")


if __name__ == '__main__':
    get_employees("Максим", 33)