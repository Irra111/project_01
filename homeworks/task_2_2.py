def quarter_of(month):
    quarter_data = {
        1: {1: "январь", 2: "февраль", 3: "март"},
        2: {4: "апрель", 5: "май", 6: "июнь"},
        3: {7: "июль", 8: "август", 9: "сентябрь"},
        4: {10: "октябрь", 11: "ноябрь", 12: "декабрь"},
    }
    for quarter_num, quarter_months in quarter_data.items():
        if month in quarter_months:
            print(f"месяц {month} ({quarter_months[month]}) является частью {quarter_num}-го квартала")
            break
    else:
        print("Такого месяца нет!")