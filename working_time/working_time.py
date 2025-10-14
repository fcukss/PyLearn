# сделать прграмму, которая будет считать количество отработанных часов в месяц, 
# и выводить на экран зарплату с учетом почасовой ставки и доплат за выходные и праздники
# пользователь вводить месяц, количество часов в субботу, воскресенье и праздничные дни

def calculate_bonus_after_tax():
    base_salary = 3674  # евро
    saturday_rate = 18   # евро за час
    sunday_holiday_rate = 21  # евро за час
    tax_rate = 0.35  # 35%

    month = input("Введите месяц: ")
    
    try:
        saturday_hours = float(input("Введите количество часов, отработанных в субботу: "))
        sunday_hours = float(input("Введите количество часов, отработанных в воскресенье: "))
        holiday_hours = float(input("Введите количество часов, отработанных в праздничные дни: "))
    except ValueError:
        print("Пожалуйста, вводите только числа для часов.")
        return

    # Расчет доплаты
    saturday_bonus = saturday_hours * saturday_rate
    sunday_bonus = sunday_hours * sunday_holiday_rate
    holiday_bonus = holiday_hours * sunday_holiday_rate

    total_bonus = saturday_bonus + sunday_bonus + holiday_bonus

    # Вычитаем налог
    tax_amount = total_bonus * tax_rate
    total_bonus_after_tax = total_bonus - tax_amount
    total_salary_after_tax = base_salary + total_bonus_after_tax

    # Вывод результатов
    print(f"Доплата за субботу: {saturday_bonus:.2f} €")
    print(f"Доплата за воскресенье: {sunday_bonus:.2f} €")
    print(f"Доплата за праздничные дни: {holiday_bonus:.2f} €")
    print(f"Суммарная доплата: {total_bonus:.2f} €")
    print(f"Налог (35%): {tax_amount:.2f} €")
    print(f"Доплата после налога: {total_bonus_after_tax:.2f} €")
    print(f"Общая зарплата с бонусами после налога: {total_salary_after_tax:.2f} €")

# Запуск программы
calculate_bonus_after_tax()

