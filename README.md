# FITNESSPRO - веб-приложение для фитнесс программ, учета питательных веществ и контроля питания.

## Описание проекта
FITNESSPRO - это комплексное веб-приложение, разработанное для того, 
чтобы помочь пользователям управлять своим занятием фитнесом и целями в области питания. 
Приложение предоставляет персонализированные планы тренировок, отслеживание питания и 
рекомендации по тренировкам с помощью искусственного интеллекта.

## Основные функции

### Аутентификация и профиль
- Регистрация нового пользователя
- Авторизация существующего пользователя
- Редактирование профиля
- Установка фитнес-целей
- Внесение личных данных (вес, рост, возраст и т.д.)

### Тренировки
- Библиотека упражнений с описаниями и gif
- Создание персональных тренировок
- Генерация тренировок с помощью ИИ на основе целей и уровня подготовки
- Список имеющихся тренировок

### Питание
- Каталог рецептов здорового питания
- Детальные страницы рецептов с пошаговыми инструкциями
- Дневник питания с подсчетом калорий, белков, жиров и углеводов
- Отслеживание водного баланса

## Технологический стек
- Backend: Python 3.9+, Django 4.2+
- Frontend: HTML, CSS, JavaScript
- База данных: PostgreSQL
- Шаблонизатор: Django Templates
- AI: Google generativeai

# Установка и запуск

## Требования
- Python 3.9 или выше
- pip (Python package manager)
- PostgreSQL
- virtualenv или venv

## Установка
1. Клонировать репозиторий:
   ```
   git clone https://github.com/kilona57/HealthFit.git
   ```
2. Перейдите в каталог проекта:
   ```
   cd HealthFit
   ```
3. Создание и активация виртуального окружения
   ### Windows
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

   ### Linux/macOS
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Установка зависимостей
   ```
   pip install -r requirements.txt
   ```
5. Создайте файл .env в корневой директории
   ```
   touch .env
   ```
6. Настройка базы данных
   ### Создайте базу данных PostgreSQL
   ```
   createdb fitlife
   ```
   
   ### Выполните миграции
   ```
   python manage.py migrate
   ```
   
   ### Создайте суперпользователя
   ```
   python manage.py createsuperuser
   ```

## Запуск
   ### Запуск сервера разработки
   ```
   python manage.py runserver
   ```

## Зависимости
   Основные зависимости проекта (requirements.txt):
   ```
   crispy-bootstrap5==2024.10
   Django==5.1.2
   django-crispy-bootstrap==0.1.1.1
   django-crispy-forms==2.3
   openai==1.54.3
   psycopg2==2.9.10
   pydantic==2.9.2
   pydantic_core==2.23.4
   requests==2.32.3
   ```
## Способствование

Мы приветствуем ваше участие! Если вы обнаружите какие-либо проблемы или у вас есть предложения по улучшению, пожалуйста, не стесняйтесь сообщать о проблеме или отправлять запрос на обновление.


## Контакты
[github](https://github.com/kilona57)</br>
[gmail](kondrashka04@gmail.com)

