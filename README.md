# **README**

## Django проект для Интенсива

[![ExampleProject on PyPI](https://img.shields.io/pypi/v/dohq-example-project.svg)](https://pypi.python.org/pypi/dohq-example-project) [![Python package](https://github.com/miheisv/DjangoY/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/miheisv/DjangoY/actions/workflows/python-package.yml) [![Codacy Badge](https://app.codacy.com/project/badge/Grade/1926cd65460f4e8ca7c4c276885562fa)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=miheisv/DjangoY&amp;utm_campaign=Badge_Grade)

> ### 0. Preparation.
Убедитесь, что у вас установлены:
- Python 3.8 / Python 3.9 / Python 3.10
- pip последней версии  


> ### I. Установка
- скачайте проект(ветку main)
- распакуйте архив в удобное для вас место
- в папке проекта(ветка main) откройте cmd(за другие оболочки не ручаюсь)
- создайте виртуальное окружение, введя команду `python -m venv venv`
- запустите виртуальное окружение, введя команду `cd venv/Scripts/`, а затем `...\activate.bat`
- вернитесь в основную ветку(в папку DjangoY-main), введя команду `cd *полный путь до папки*`
- установите зависимости, введя команду `pip install -r requirements.txt` 
- закройте командную строку  

> ### I//II. Установка базы данных из фикстур.
*если вам необходимо провести установку базы данных в ручном режиме*
- перейдите в папку lyceum и откройте командную строку
- введите `python manage.py loaddata data`

> ### II. Запуск
- после установки зависимостей перейдите в папку `lyceum` и откройте командную строку
- в командной строке введите `py manage.py runserver`
- проект запустится на http://127.0.0.1:8000/
- не забудьте, закончив, прекратите работу программы, закройте команду строку  


> ## Общая информация о проекте
> Вся критичная для проекта информация помещена в .env, вы можете использовать готовый .env-exmpl
