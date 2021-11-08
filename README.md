# Сокращение ссылок с помощью сайта bit.ly
Скрипт предназначен для преобразования длинной ссылки в битлинк вида bit.ly/1ABCdef. В случае ввода вашего битлинка отображает количество переходов по данной ссылке за все время. Ссылка передается в качестве аргумента:

```python bitly.py [-h] <url> ```
### Как установить
Требуется установленный Python3.x.
Рекомендуется использовать виртуальное окружение [virtualenv/venv](https://docs.python.org/3/
library/venv.html) для изоляции проекта.
Для установки необходимых зависимостей введите в консоли:

```pip install -r requirements.txt```

Либо (в случае конфликта с python2.x):

```pip3 install -r requirements.txt```

Для работы с API сайта потребуется ключ доступа. По адресу [dev.bitly.com](https://dev.bitly.com/) можно сгенерировать токен. Его следует сохранить в переменной ```BITLY_TOKEN``` в файле .env в директории скрипта:

```BITLY_TOKEN=abcdefghjiklmnopqrstuvwxyz1234567890abcd```
### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/)
