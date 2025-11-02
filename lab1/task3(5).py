import hashlib

users = {
    "yuliiaivs": {
        "password": hashlib.md5("atober5".encode()).hexdigest(),
        "full_name":  "Іванова Юлія Романівна"
    },
    "riritag": {
        "password": hashlib.md5("rypters".encode()).hexdigest(),
        "full_name": "Шевченко Андрій Олегович"
    },
    "olenamel": {
        "password": hashlib.md5("mirter4".encode()).hexdigest(),
        "full_name": "Мельник Олена іванівна"
    }
}

def authenticate_user():
    login = input("Введіть логін: ")
    password = input("Введіть пароль: ")

    if login in users:
        hashed_password_input = hashlib.md5(password.encode()).hexdigest()
        if users[login]["password"] == hashed_password_input:
            full_name = users[login]["full_name"]
            print(f"\n Вхід успішний. Вітаємо, {users[login]['full_name']}.")
        else:
            print("\n Невірний пароль")
    else:
        print("\n Користувача з таким логіном не знайдено")

if __name__ == "__main__":
    authenticate_user()