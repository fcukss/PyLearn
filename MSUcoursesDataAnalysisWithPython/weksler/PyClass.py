class User:
    def __init__(self, username, first_name, last_name):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.is_logged_in = False

    def login(self):
        print(f"User {self.username} is ligged in system")
        self.is_logged_in = True

    def __str__(self):
        return f"{self.username} - {self.last_name}"

new_user = User("fcukss", "Stas", "Kaplia")
new_user.login()
print(new_user.is_logged_in)

print(new_user.username)
print(new_user)                 #fcukss - Kaplia