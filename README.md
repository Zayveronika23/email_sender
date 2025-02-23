# Сервис для отправки email.           

### Краткое описание:
Приложение для отправки email с Celery.

### Сборка и запуск:

```bash
Клонируем репозиторий 
git clone git@github.com:<nickname>/Test_task.git

Переходим в директорию:
cd email_sender

Cоздаем и активируем виртуальное окружение:
python3 -m venv venv
source venv/bin/activate

Устанавливаем необходимые зависимости
pip install -r requirements.txt

Создать файл .env в корне директории и записать переменные:
EMAIL_HOST_USER = Email отправителя
EMAIL_HOST_PASSWORD = Пароль приложения 
SECRET_KEY = Secret key

Выполнить миграции:
cd email_sender
python3 manage.py makemigrations
python3 manage.py migrate

Запускаем проект:
python3 manage.py runserver
python -m celery -A email_sender worker
redis-server

Для запуска Flower:
celery -A email_sender flower
```
Далее в браузере открываем страницу http://127.0.0.1:8000/send_emails/
