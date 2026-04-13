# VirusTotal Scanner

## Установка
pip install -r requirements.txt

## Настройка
Создать .env:
VT_API_KEY=your_key

## Запуск
# Консольный ввод (CLI):

python scanner.py --file test.exe
python scanner.py --url https://example.com
python scanner.py --hash <sha256>

<img width="541" height="368" alt="Снимок экрана 2026-04-12 230315" src="https://github.com/user-attachments/assets/c6efa8df-4888-4902-ae22-d64f565174f8" />

<img width="740" height="137" alt="Снимок экрана 2026-04-13 213401" src="https://github.com/user-attachments/assets/a12ce0aa-4bbf-4b6b-8169-c89f3bfef648" />

# Интерактивный режим:
python scanner.py

<img width="529" height="410" alt="Снимок экрана 2026-04-13 213756" src="https://github.com/user-attachments/assets/e601f900-2f6a-4aa5-9048-e9cff9cdb0ec" />

## Ограничения
- 4 запроса в минуту
- 500 в день
- файл до 32MB
