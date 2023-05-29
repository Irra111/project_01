months = {
    1: ["январь", 31],
    2: ["февраль", 28],
    3: ["март", 31],
    4: ["апрель", 30],
    5: ["май", 31],
    6: ["июнь", 30],
    7: ["июль", 31],
    8: ["август", 31],
    9: ["сентябрь", 30],
    10: ["октябрь", 31],
    11: ["ноябрь", 30],
    12: ["декабрь", 31]
}

def get_month():
    month_number = int(input("Введите номер месяца: "))
    if month_number not in months:
        print("Такого месяца нет!")
    else:
        month_name, month_length = months[month_number]
        print(f"Вы ввели {month_name}. {month_length} дней")


get_month()