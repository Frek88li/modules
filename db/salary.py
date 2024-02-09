from datetime import datetime



def calculate_salary(hours, rate):
    print(datetime.now().date())
    print(f"Сотрудник отработал {hours} часов и получил {rate} рублей")

if __name__ == '__main__':
    calculate_salary(3, 300)
