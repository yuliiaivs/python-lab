import hashlib
import os

def generate_file_hashes(file_paths: list) -> dict:

    file_hashes = {}
    for file_path in file_paths:
        try:
            if not os.path.exists(file_path):
                print(f"Помилка: Файл не існує за шляхом '{file_path}'. Пропущено.")
                continue
            with open(file_path, 'rb') as f:
                hasher = hashlib.sha256()
                block_size = 4096
                while True:
                    buffer = f.read(block_size)
                    if not buffer:
                        break
                    hasher.update(buffer)
                file_hashes[file_path] = hasher.hexdigest()
        except FileNotFoundError:
            print(f"Помилка: Файл не знайдено за шляхом '{file_path}'. Пропущено.")
        except IOError as e:
            print(f"Помилка читання файлу '{file_path}': {e}. Пропущено.")
        except Exception as e:
            print(f"Виникла несподівана помилка під час обробки файлу '{file_path}': {e}. Пропущено.")
    return file_hashes

files_to_hash = []

my_screenshot_path = r"C:\Users\julie\OneDrive\Изображения\Screenshots\Screen.png"

if os.path.exists(my_screenshot_path):
    files_to_hash.append(my_screenshot_path)
    print(f"Додано скріншот для хешування: '{my_screenshot_path}'")
else:
    print(f"Попередження: Скріншот за шляхом '{my_screenshot_path}' не знайдено. Будь ласка, перевірте правильність шляху та існування файлу.")

dummy_dir = "test_files_for_hash"
if not os.path.exists(dummy_dir):
    os.makedirs(dummy_dir)

file1_name = "report.txt"
with open(os.path.join(dummy_dir, file1_name), "w", encoding="utf-8") as f:
    f.write("Це текст звіту.\nРядок 2.\n")
files_to_hash.append(os.path.join(dummy_dir, file1_name))

non_existent_file = os.path.join(dummy_dir, "non_existent_file.pdf")
files_to_hash.append(non_existent_file)

print(f"\n--- Генерація хешів для {len(files_to_hash)} файлів ---")
hashes = generate_file_hashes(files_to_hash)

if hashes:
    print("\nЗгенеровані хеші SHA-256:")
    for path, hx in hashes.items():
        print(f"'{path}': {hx}")
else:
    print("\nНе вдалося згенерувати хеші для жодного файлу.")
print("-" * 30)

print("\n--- Очищення тимчасових файлів ---")
for file_path in files_to_hash:

    if file_path.startswith(dummy_dir) and os.path.exists(file_path):
        os.remove(file_path)
        print(f"Видалено: '{file_path}'")
if os.path.exists(dummy_dir) and not os.listdir(dummy_dir):
    os.rmdir(dummy_dir)
    print(f"Видалено тимчасову директорію: {dummy_dir}")
elif os.path.exists(dummy_dir):
    print(f"Тимчасова директорія '{dummy_dir}' не порожня або не вдалося її видалити.")