"""
Для следующего задания нам потребуется знать основы даты и времени, чтобы получить текущий год.
В этом задании создайте две функции:
get_current_year, которая возвращает текущий год
get_year_days_ago, которая принимает количество дней и возвращает год, который был столько дней назад
"""

import datetime


# def get_current_year():
#     now_date = datetime.datetime.now()
#     year = now_date.year
#     return year

#short version
def get_current_year():
    return datetime.datetime.now().year

def get_year_days_ago(num_days):
    now_date = datetime.datetime.now()
    year_ago = now_date - datetime.timedelta(days=num_days)
    return year_ago.year



if __name__ == '__main__':
    print('Текущий год:', get_current_year())
    print('Год 720 дней назад:', get_year_days_ago(720))