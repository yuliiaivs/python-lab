import os

def analyze_log_file(log_file_path: str) -> dict:

    status_counts = {}
    try:
        with open(log_file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()

                if not line:
                    continue

                parts = line.split()

                if len(parts) >= 2:
                    status_code_str = parts[-2]
                    try:
                        int(status_code_str)
                        status_counts[status_code_str] = status_counts.get(status_code_str, 0) + 1
                    except ValueError:
                        pass

    except FileNotFoundError:
        print(f"Помилка: Файл не знайдено за шляхом '{log_file_path}'. Будь ласка, перевірте правильність шляху.")
        return {}
    except IOError as e:
        print(f"Помилка читання файлу '{log_file_path}': {e}. Можливо, відсутні права доступу або файл пошкоджено.")
        return {}
    except Exception as e:
        print(f"Виникла несподівана помилка під час аналізу файлу '{log_file_path}': {e}")
        return {}

    return status_counts

dummy_log_content = """
83.149.9.216 - - [17/May/2015:10:05:03 +0000] "GET /presentations/logstash-monitorama-2013/images/kibana-search.png HTTP/1.1" 200 203023
83.149.9.216 - - [17/May/2015:10:05:04 +0000] "GET /presentations/logstash-monitorama-2013/images/kibana-dashboard.png HTTP/1.1" 200 171717
83.149.9.216 - - [17/May/2015:10:05:06 +0000] "GET /presentations/logstash-monitorama-2013/images/kibana-dashboard3.png HTTP/1.1" 200 171717
83.149.9.216 - - [17/May/2015:10:05:07 +0000] "GET /presentations/logstash-monitorama-2013/plugin/highlight.js HTTP/1.1" 200 263185
83.149.9.216 - - [17/May/2015:10:05:08 +0000] "GET /presentations/logstash-monitorama-2013/*/mozilla.js HTTP/1.1" 404 36736
83.149.9.216 - - [17/May/2015:10:05:10 +0000] "GET /presentations/logstash-monitorama-2013/plugin/room.js HTTP/1.1" 200 7597
192.168.1.1 - - [17/May/2015:10:05:11 +0000] "GET /api/v1/status HTTP/1.1" 200 123
10.0.0.5 - - [17/May/2015:10:05:12 +0000] "POST /data HTTP/1.1" 500 0
83.149.9.216 - - [17/May/2015:10:05:13 +0000] "GET /presentations/logstash-monitorama-2013/notes.js HTTP/1.1" 200 2982
172.16.0.10 - - [17/May/2015:10:05:14 +0000] "GET /admin/dashboard HTTP/1.1" 500 0
83.149.9.216 - - [17/May/2015:10:05:15 +0000] "GET /invalid/page HTTP/1.1" 404 150
83.149.9.216 - - [17/May/2015:10:05:16 +0000] "GET /healthcheck HTTP/1.1" 200 10
"""

log_file_name = "apache_logs.txt"

with open(log_file_name, "w", encoding="utf-8") as f:
    f.write(dummy_log_content.strip())

print(f"--- Аналіз файлу '{log_file_name}' ---")
results = analyze_log_file(log_file_name)

if results:
    print("Результати аналізу HTTP-кодів:")
    for status, count in sorted(results.items()):  # Сортуємо для кращого відображення
        print(f"Код {status}: {count} входжень")
else:
    print("Аналіз не дав результатів (можливо, файл порожній або сталася помилка).")
print("-" * 30)

print("--- Тест на відсутній файл ---")
missing_file_results = analyze_log_file("non_existent_log.txt")
print(f"Результати для відсутнього файлу: {missing_file_results}")
print("-" * 30)

if os.path.exists(log_file_name):
    os.remove(log_file_name)
    print(f"Фіктивний файл '{log_file_name}' видалено.")