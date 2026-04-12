import hashlib
import base64


def calculate_sha256(file_path: str) -> str:
    """Вычисляет SHA-256 файла"""
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def base64_url_encode(url: str) -> str:
    """Кодирует URL в base64 (для VirusTotal)"""
    return base64.urlsafe_b64encode(url.encode()).decode().strip("=")


def parse_stats(stats: dict) -> str:
    """Форматирует статистику"""
    return (
        f"Malicious: {stats.get('malicious', 0)}\n"
        f"Suspicious: {stats.get('suspicious', 0)}\n"
        f"Harmless: {stats.get('harmless', 0)}\n"
        f"Undetected: {stats.get('undetected', 0)}"
    )