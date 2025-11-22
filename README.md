# Furniture Store - Интернет-магазин мебели на фреймворке Django

Веб-приложение интернет-магазина мебели на Django с современным стеком технологий.

## Технологический стек

- **Backend**: Django 4.2 + Django REST Framework
- **Database**: PostgreSQL 17
- **App Server**: Gunicorn
- **Web Server**: Nginx
- **Orchestration**: Docker Compose

## Особенности

- Корзина покупок
- Каталог товаров с категориями (django-tree-queries)
- Гибкая система атрибутов товаров (django-eav2)
- Обработка изображений (django-imagekit)
- Production-ready деплой (Nginx + Gunicorn)
- Docker-поддержка

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/EgorGurtsiev/furniture_store.git
cd furniture_store
```

2. Настройте окружение, отредактировав .env файл
3. Запустите сервисы:
```bash
docker compose up -d --build
```
4. Примените миграции:

```bash
docker exec -it django python manage.py migrate
```
## Доступ
Локально: http://localhost

Демо-сервер: http://45.90.218.115

Зависимости
См. requirements.txt

Docker сервисы
| Сервис  | Описание                | Порт  |
|---------|-------------------------|-------|
| db      | PostgreSQL 17           | 5432  |
| django  | Django + Gunicorn       | 8000  |
| nginx   | Веб-сервер              | 80    |
