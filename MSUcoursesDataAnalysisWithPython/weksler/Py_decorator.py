def my_decorator(*args, my_param1=None, my_param2=None):
    # my_param1 и my_param2 - это опциональные параметры, которые может принимать декоратор
    def _my_decorator(f):
        def wrap(*args, **kwargs):
            print('my_param1', my_param1)
            print('my_param2', my_param2)

            # Дополнительная логика ДО выполнения функции
            result = f(*args, **kwargs)
            # Дополнительная логика ПОСЛЕ выполнения функции
            return result
        return wrap
    if len(args) == 1 and callable(args[0]):
        return _my_decorator(args[0])    # случай когда декорируем без параметров
    else:
        return _my_decorator             # декорируем с параметрами

#Такой декоратор можно применять как без параметров:
@my_decorator
def add_two_numbers(a, b):
     return a + b


#Так и с параметрами:
@my_decorator(my_param1='test', my_param2='passed')
def divide_two_numbers(a, b):
    return a / b


def parametrize(*args, list_of_params):
    def _parametrize(f):
        def wrap(*args, **kwargs):
            for params in list_of_params:
                print(f'Вызываем функцию {f} с параметрами {params}')
                result = f(**params)
                print(f'Результат: {result}')
        return wrap
    return _parametrize

@parametrize(list_of_params=[{'a': 5, 'b': 10}, {'a': 6, 'b': 10}, {'a': 7, 'b': 1}])
def divide_two_numbers(a, b):
    return a / b

divide_two_numbers(5, 5)