# def log_action(func):
#     def wrapper(*args, **kwargs):
#         print(f"--- LOG: Запуск функции {func.__name__} ---")
#         res = func(*args, **kwargs)
#         print(f"--- LOG: Функция {func.__name__} завершена ---")
#         return res
#     return wrapper
#
# @log_action
# def process_dna(sequence):
#     print(f"Анализируем последовательность: {sequence}")
#     return True
#
# process_dna("ACTG")

"""
Твое задание: "Аудит доступа"
Представь, что у нас есть база данных DNA. 
Мы хотим, чтобы перед выполнением любой функции печаталось: 
    Security Check: [Имя пользователя] Access Granted.

Задача:
Напиши декоратор security_check.

Он должен принимать аргумент user_name 
(можно просто передать его в функцию через args).

Создай функцию delete_sample(user_name, sample_id), 
которая просто печатает "Sample [ID] deleted".

Оберни её декоратором так, чтобы при вызове delete_sample("Admin", 111) 
в консоли сначала появлялась надпись о проверке безопасности."""

# def security_check(func):
#     def wrapper(*args, **kwargs):
#         print(f"--- LOG: Security Check: [{args[0]}] Access Granted")
#         res = func(*args, **kwargs)
#         return res
#     return wrapper
#
# @security_check
# def delete_sample(user_name, sample_id):
#     print(f"Sample [{sample_id}] deleted")
#
#
# delete_sample("Admin", 111)


"""Твоё финальное задание по декораторам: "Таймер производительности"

В HealthTech расчёты (например, обработка снимка МРТ) могут быть долгими. 
Инженерам важно знать, сколько времени занимает функция.

Задача:

Напиши декоратор benchmark.

Внутри него используй модуль time (функция time.time()), 
чтобы замерить время до и после выполнения функции.

Декоратор должен печатать: Function [название] took [время] seconds.

Примени его к функции heavy_computation(), 
в которой используй time.sleep(1.5) (имитация долгой работы)."""

import time
def benchmark(func):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        res = func(*args, **kwargs)
        time_finish = time.time()
        total_time = time_finish-time_start
        print(f"Function [{func.__name__}] took [{total_time:.4f}] seconds.")
        return res
    return wrapper

@benchmark
def heavy_computation():
    time.sleep(1.5)

heavy_computation()