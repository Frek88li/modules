from db.salary import calculate_salary
from db.people import get_employees

if __name__ == '__main__':
    get_employees('Ivan', 34)
    calculate_salary(3, 500)
