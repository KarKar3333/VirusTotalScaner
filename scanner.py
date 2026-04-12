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
    encoded = base64_url_encode(url)

    result = scan_url(url)
    url_id = result["data"]["id"]

    time.sleep(20)

    report = get_url_report(url_id)
    stats = report["data"]["attributes"]["last_analysis_stats"]

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
        print("Используй --file или --url или --hash")


if __name__ == "__main__":
    main()