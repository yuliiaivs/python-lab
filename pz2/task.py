import hashlib
from datetime import datetime

#створення базового класу User

class User:

    def __init__(self, username, password):
        self.username = username
        self.password_hash = self._hash_password(password)
        self.is_active = True

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password):
        return self.password_hash == self._hash_password(password)

    def __str__(self):
        return f"Користувач(логін='{self.username}', активний={self.is_active})"

#створення підкласів

class Administrator(User):

    def __init__(self, username, password, permissions=None):
        super().__init__(username, password)
        self.permissions = permissions if permissions is not None else ["усі_дозволи"]

    def __str__(self):
        return (f"Адміністратор(логін='{self.username}', "
                f"дозволи={self.permissions})")


class RegularUser(User):

    def __init__(self, username, password):
        super().__init__(username, password)
        self.last_login_date = None

    def record_login(self):
        self.last_login_date = datetime.now()
        print(f"Дата входу для '{self.username}' оновлена: {self.last_login_date.strftime('%Y-%m-%d %H:%M:%S')}")

    def __str__(self):
        last_login = self.last_login_date.strftime('%Y-%m-%d %H:%M:%S') if self.last_login_date else "Ніколи"
        return (f"Звичайний користувач(логін='{self.username}', "
                f"останній вхід='{last_login}')")


class GuestUser(User):

    def __init__(self, username="guest"):
        super().__init__(username, "guest_password")
        self.is_active = False
        print("Створено гостьовий акаунт з обмеженим доступом.")

    def __str__(self):
        return f"Гість(логін='{self.username}', обмежений_доступ=True)"

#створення класу AccessControl

class AccessControl:

    def __init__(self):
        self.users = {}

    def add_user(self, user):
        if user.username in self.users:
            print(f"Помилка: Користувач з логіном '{user.username}' вже існує.")
            return False
        self.users[user.username] = user
        print(f"Користувач '{user.username}' (тип: {type(user).__name__}) успішно доданий.")
        return True

    def authenticate_user(self, username, password):
        user = self.users.get(username)

        if user and user.is_active:
            if user.verify_password(password):
                print(f"Аутентифікація для '{username}' успішна.")
                if isinstance(user, RegularUser):
                    user.record_login()
                return user
            else:
                print(f"Аутентифікація не вдалася: Неправильний пароль для '{username}'.")
                return None

        print(f"Аутентифікація не вдалася: Користувач '{username}' не знайдений або неактивний.")
        return None


if __name__ == "__main__":
    access_system = AccessControl()
    print("--- Створення та додавання користувачів ---")

    admin = Administrator("admin_user", "supersecret123", permissions=["читання", "запис", "видалення"])
    reg_user = RegularUser("john_doe", "password123")
    guest = GuestUser()

    access_system.add_user(admin)
    access_system.add_user(reg_user)
    access_system.add_user(guest)

    print("\n--- Тестування аутентифікації ---")

    authenticated_user_1 = access_system.authenticate_user("admin_user", "supersecret123")
    if authenticated_user_1:
        print(f"Вітаємо, {authenticated_user_1}!")

    print("-" * 20)

    authenticated_user_2 = access_system.authenticate_user("john_doe", "password123")
    if authenticated_user_2:
        print(f"Вітаємо, {authenticated_user_2}!")

    print("-" * 20)

    authenticated_user_3 = access_system.authenticate_user("john_doe", "password123")
    if authenticated_user_3:
        print(f"З поверненням, {authenticated_user_3}!")

    print("-" * 20)

    authenticated_user_4 = access_system.authenticate_user("admin_user", "wrongpassword")
    if not authenticated_user_4:
        print("Доступ заборонено, як і очікувалося.")

    print("-" * 20)

    authenticated_user_5 = access_system.authenticate_user("unknown_user", "password")
    if not authenticated_user_5:
        print("Доступ заборонено, як і очікувалося.")

    print("-" * 20)

    authenticated_user_6 = access_system.authenticate_user("guest", "guest_password")
    if not authenticated_user_6:
        print("Доступ для гостя обмежений, як і очікувалося.")