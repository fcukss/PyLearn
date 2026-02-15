users_db = {}

class User:
    def __init__(self, login, password):
        self._login = login
        self.__password = password


    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, new_login):
        self._login = new_login

    @property
    def password(self):
        return '************(скрыто в целях безопасности)'

    @password.setter
    def password(self, new_password):
        if len(new_password)<6:
            print("Ошибка: Пароль должен быть не менее 8 символов!")
        elif new_password.isdigit():
            print("Ошибка: Пароль не может состоять только из цифр!")
        else:
            print("Пароль успешно обновлен.")
            self.__password = new_password

    def get_real_password(self):
        """Метод для сохранения в БД (опционально)"""
        return self.__password

    def check_password(self, input_password):
        return self.__password == input_password

    def __repr__(self):
        return f"User(login='{self._login}')"

def register_user(user:User):
    if user.login in users_db:
        print(f"Ошибка: Пользователь {user.login} уже существует!")
    else:
        users_db[user.login] = user
        print(f"Пользователь {user.login} зарегистрирован.")


def login_to_system(login, password):
    # 1. Ищем пользователя по ключу в словаре
    user = users_db.get(login)

    if user:
        # 2. Если нашли, вызываем метод проверки пароля
        if user.check_password(password):
            print(f"Добро пожаловать, {user.login}! Вы успешно вошли.")
            return True
        else:
            print("Ошибка: Неверный пароль.")
    else:
        print("Ошибка: Пользователь не найден.")

    return False


user1 = User('fcuk', 'fcuk1234')
user2 = User('Tom', 'voldemort')
register_user(user1)
register_user(user2)

print(users_db)

user_to_find = 'Tom'
if user_to_find in users_db:
    found_user = users_db[user_to_find]
    print(f"Пользователь {found_user.login} найден! настоящий пароль: {found_user.get_real_password()}")