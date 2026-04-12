# VirusTotal Scanner

## Установка
pip install -r requirements.txt

## Настройка
Создать .env:
VT_API_KEY=your_key

## Запуск
python scanner.py --file test.exe
python scanner.py --url https://example.com
python scanner.py --hash <sha256>

## Ограничения
- 4 запроса в минуту
- 500 в день
- файл до 32MB