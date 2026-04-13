import argparse
import os
import time

from utils import calculate_sha256, base64_url_encode, parse_stats
from vt_api import *
from logger import logger


def scan_file(file_path):
    if not os.path.exists(file_path):
        print("Файл не найден")
        return

    if os.path.getsize(file_path) > 32 * 1024 * 1024:
        print("Файл слишком большой (>32MB)")
        return

    print("Вычисляем SHA-256...")
    file_hash = calculate_sha256(file_path)

    report = get_file_report(file_hash)

    if report:
        stats = report["data"]["attributes"]["last_analysis_stats"]
        print(parse_stats(stats))
    else:
        print("Файл не найден в VT. Загружаем...")
        result = upload_file(file_path)
        analysis_id = result["data"]["id"]

        print("Ожидаем анализ...")
        time.sleep(20)

        analysis = get_analysis(analysis_id)
        stats = analysis["data"]["attributes"]["stats"]
        print(parse_stats(stats))


def scan_url_func(url):
    print("Отправляем URL на анализ...")

    result = scan_url(url)
    analysis_id = result["data"]["id"]

    print("Ожидаем анализ...")
    time.sleep(20)

    analysis = get_analysis(analysis_id)
    stats = analysis["data"]["attributes"]["stats"]

    print(parse_stats(stats))


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--file")
    parser.add_argument("--url")
    parser.add_argument("--hash")

    args = parser.parse_args()

    if args.file:
        scan_file(args.file)
    elif args.url:
        scan_url_func(args.url)
    elif args.hash:
        report = get_file_report(args.hash)
        if report:
            stats = report["data"]["attributes"]["last_analysis_stats"]
            print(parse_stats(stats))
        else:
            print("Не найдено")
    else:
        interactive_mode()

def interactive_mode():
    while True:
        print("\n=== VirusTotal Scanner ===")
        print("1 — Проверить файл")
        print("2 — Проверить URL")
        print("3 — Проверить по хешу")
        print("0 — Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            file_path = input("Введите путь к файлу: ")
            scan_file(file_path)

        elif choice == "2":
            url = input("Введите URL: ")
            scan_url_func(url)

        elif choice == "3":
            file_hash = input("Введите SHA-256 хеш: ")
            report = get_file_report(file_hash)
            if report:
                stats = report["data"]["attributes"]["last_analysis_stats"]
                print(parse_stats(stats))
            else:
                print("Не найдено")

        elif choice == "0":
            print("Выход...")
            break

        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()