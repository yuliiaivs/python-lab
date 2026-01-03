import sqlite3
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def init_db():
    conn = sqlite3.connect('accounts.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            login TEXT PRIMARY KEY,
            password TEXT,
            full_name TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_user():
    print("\n--- Реєстрація нового користувача ---")
    login = input("Введіть логін: ")
    password = input("Введіть пароль: ")
    name = input("Введіть повне ПІБ: ")

    hashed_pass = hash_password(password)

    try:
        conn = sqlite3.connect('accounts.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users VALUES (?, ?, ?)", (login, hashed_pass, name))
        conn.commit()
        print("Користувача успішно додано!")
    except sqlite3.IntegrityError:
        print("Помилка: користувач з таким логіном вже існує.")
    finally:
        conn.close()


def update_password():
    print("\n--- Оновлення пароля ---")
    login = input("Введіть логін користувача: ")
    new_password = input("Введіть новий пароль: ")

    hashed_pass = hash_password(new_password)

    conn = sqlite3.connect('accounts.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE users SET password = ? WHERE login = ?", (hashed_pass, login))

    if cursor.rowcount > 0:
        conn.commit()
        print("Пароль успішно змінено!")
    else:
        print("Користувача з таким логіном не знайдено.")
    conn.close()


def check_auth():
    print("\n--- Вхід у систему ---")
    login = input("Логін: ")
    password = input("Пароль: ")

    hashed_input = hash_password(password)

    conn = sqlite3.connect('accounts.db')
    cursor = conn.cursor()
    cursor.execute("SELECT full_name FROM users WHERE login = ? AND password = ?", (login, hashed_input))
    user = cursor.fetchone()
    conn.close()

    if user:
        print(f"Вітаємо, {user[0]}! Вхід виконано успішно.")
        return True
    else:
        print("Помилка: неправильний логін або пароль.")
        return False

def main():
    init_db()
    while True:
        print("\nМеню управління БД:")
        print("1. Додати користувача")
        print("2. Оновити пароль")
        print("3. Перевірити вхід (Автентифікація)")
        print("4. Вийти")

        choice = input("Оберіть пункт: ")

        if choice == '1':
            add_user()
        elif choice == '2':
            update_password()
        elif choice == '3':
            check_auth()
        elif choice == '4':
            print("Завершення роботи.")
            break
        else:
            print("Неправильний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()