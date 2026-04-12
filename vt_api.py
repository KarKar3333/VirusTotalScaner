import time
import requests
from config import API_KEY, BASE_URL
from logger import logger

HEADERS = {"x-apikey": API_KEY}


def rate_limit():
    """Ограничение: 4 запроса в минуту"""
    time.sleep(15)


def get_file_report(file_hash: str):
    """Получить отчёт по файлу"""
    url = f"{BASE_URL}/files/{file_hash}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return None
    else:
        response.raise_for_status()


def upload_file(file_path: str):
    """Загрузить файл"""
    url = f"{BASE_URL}/files"

    with open(file_path, "rb") as f:
        files = {"file": f}
        response = requests.post(url, headers=HEADERS, files=files)

    response.raise_for_status()
    return response.json()


def get_analysis(analysis_id: str):
    """Получить результат анализа"""
    url = f"{BASE_URL}/analyses/{analysis_id}"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()


def scan_url(encoded_url: str):
    """Отправить URL"""
    url = f"{BASE_URL}/urls"
    data = {"url": encoded_url}

    response = requests.post(url, headers=HEADERS, data=data)
    response.raise_for_status()
    return response.json()


def get_url_report(url_id: str):
    """Получить отчёт по URL"""
    url = f"{BASE_URL}/urls/{url_id}"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()