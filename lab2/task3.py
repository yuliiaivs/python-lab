import os
import re

def filter_ips(input_file_path: str, output_file_path: str, allowed_ips: list) -> bool:

    allowed_ips_set = set(allowed_ips)
    ip_counts = {}

    ip_pattern = re.compile(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

    try:
        with open(input_file_path, 'r', encoding='utf-8') as infile:
            for line_num, line in enumerate(infile, 1):
                line = line.strip()
                if not line:
                    continue

                match = ip_pattern.match(line)
                if match:
                    ip_address = match.group(1)

                    if ip_address in allowed_ips_set:
                        ip_counts[ip_address] = ip_counts.get(ip_address, 0) + 1

    except FileNotFoundError:
        print(f"Помилка: Вхідний файл не знайдено за шляхом '{input_file_path}'.")
        return False
    except IOError as e:
        print(f"Помилка читання вхідного файлу '{input_file_path}': {e}.")
        return False
    except Exception as e:
        print(f"Виникла несподівана помилка під час обробки вхідного файлу '{input_file_path}': {e}.")
        return False

    try:

        with open(output_file_path, 'w', encoding='utf-8') as outfile:
            if not ip_counts:
                outfile.write("Дозволених IP-адрес не знайдено.\n")
            else:
                # Сортуємо для кращого відображення результатів
                for ip, count in sorted(ip_counts.items()):
                    outfile.write(f"{ip} - {count} входжень\n")
        print(f"Результати успішно записано до файлу '{output_file_path}'.")
        return True

    except IOError as e:
        print(f"Помилка запису до вихідного файлу '{output_file_path}': {e}.")
        return False
    except Exception as e:
        print(f"Виникла несподівана помилка під час запису до файлу '{output_file_path}': {e}.")
        return False

if __name__ == "__main__":
    dummy_log_content = """
83.149.9.216 - - [17/May/2015:10:05:03 +0000] "GET /presentations/logstash-monitorama-2013/images/kibana-search.png HTTP/1.1" 200 203023
83.149.9.216 - - [17/May/2015:10:05:04 +0000] "GET /presentations/logstash-monitorama-2013/images/kibana-dashboard.png HTTP/1.1" 200 171717
83.149.9.216 - - [17/May/2015:10:05:08 +0000] "GET /presentations/logstash-monitorama-2013/*/mozilla.js HTTP/1.1" 404 36736
192.168.1.1 - - [17/May/2015:10:05:11 +0000] "GET /api/v1/status HTTP/1.1" 200 123
10.0.0.5 - - [17/May/2015:10:05:12 +0000] "POST /data HTTP/1.1" 500 0
83.149.9.216 - - [17/May/2015:10:05:13 +0000] "GET /presentations/logstash-monitorama-2013/notes.js HTTP/1.1" 200 2982
172.16.0.10 - - [17/May/2015:10:05:14 +0000] "GET /admin/dashboard HTTP/1.1" 500 0
83.149.9.216 - - [17/May/2015:10:05:15 +0000] "GET /invalid/page HTTP/1.1" 404 150
24.236.252.67 - - [17/May/2015:10:05:16 +0000] "GET /healthcheck HTTP/1.1" 200 10
83.149.9.216 - - [17/May/2015:10:05:17 +0000] "GET /presentations/logstash-monitorama-2013/some_other.png HTTP/1.1" 200 10000
10.0.0.5 - - [17/May/2015:10:05:18 +0000] "GET /another/data HTTP/1.1" 200 50
"""
    input_log_file = "apache_logs_for_ip_filter.txt"
    output_filtered_ips_file = "filtered_ips_results.txt"

    with open(input_log_file, "w", encoding="utf-8") as f:
        f.write(dummy_log_content.strip())
    print(f"Створено фіктивний лог-файл: '{input_log_file}'")

    allowed_ips_for_test = [
        "83.149.9.216",
        "10.0.0.5",
        "192.168.1.1",
        "24.236.252.67",
        "1.2.3.4"
    ]

    print("\n--- Запуск фільтрації IP-адрес ---")
    print(f"Дозволені IP для фільтрації: {allowed_ips_for_test}")
    success = filter_ips(input_log_file, output_filtered_ips_file, allowed_ips_for_test)

    if success:
        print(f"Перевірте файл '{output_filtered_ips_file}' для перегляду результатів.")

    else:
        print("Операція фільтрації IP-адрес завершилася з помилками.")
    print("-" * 30)

    print("\n--- Тест на відсутній вхідний файл ---")
    filter_ips("non_existent_input.txt", "dummy_output.txt", allowed_ips_for_test)
    print("-" * 30)

    print("\n--- Очищення тимчасових файлів ---")
    for f_name in [input_log_file, output_filtered_ips_file, "dummy_output.txt"]:
        if os.path.exists(f_name):
            os.remove(f_name)
            print(f"Видалено: '{f_name}'")