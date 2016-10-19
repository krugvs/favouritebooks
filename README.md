# favouritebooks
Туториал по питону: http://pythontutor.ru/

Интерпретатор языка Python для Windows: https://www.python.org/ftp/python/2.7.12/python-2.7.12.msi, скачать и установить

IDE для Python - PyCharm: https://www.jetbrains.com/pycharm/

Туториал Django, легкий вариант: https://tutorial.djangogirls.org/ru/

Туториал Django, нормальный вариант(англ): https://docs.djangoproject.com/en/1.10/intro/tutorial01/

Туториал Django на русском: http://djbook.ru/rel1.9/

Туториал по GIT: https://githowto.com/ru

Туториалы по html/css и javascrypt прикреплять не буду, так как по идее мы это уже должны знать. При особом желании можно и загуглить.



Для запуска проекта:

1). Клонируем проект в удобное место - git clone https://github.com/krugvs/favouritebooks.git

2). Переходим в папку проекта в терминале или командной строке.

3). Создаем виртуальное окружение - virtualenv venv

3.1). Устанавливаем необхдимые пакеты: pip install -r requirements.txt 

4). Активируем виртуальное окружение: source venv/bin/activate для Linux и venv\Scripts\activate для Windows

5). Создаем в mysql базу данных и меняем в файле settings.py настройки базы данных на свои.

6). Применяем миграции: python manage.py migrate для пользователей Linux и venv/Scripts/python manage.py migrate

7). Создаем суперпользователя: python manage.py createsuperuser для Linux и venv/Scripts/python manage.py createsuperuser для Windows и
    заполняем необходимые поля
    
8). Запускаем сервер: python manage.py runserver для Linux и venv/Scripts/python manage.py runserver для Windows.

9). http://127.0.0.1:8000 открываем в браузере и смотрим на результат.
