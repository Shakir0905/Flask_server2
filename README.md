# Веб-сервис на Flask для вывода персонализированных сообщений

## Задача

Создать веб-сервис, который будет выводить персонализированные сообщения на основе GET-параметров `name` и `message`. Сервис должен быть доступен по URL вида:

```
http://xx.xx.xx.xx:8080/?name=Rekruto&message=Давай дружить
```

При переходе по такому URL должно выводиться сообщение:

```
Rekruto! Давай дружить!
```

## Решение

Для решения задачи использован язык программирования Python и фреймворк Flask.

### Установка зависимостей

Перед началом работы установите Flask:

```bash
pip install Flask
```

### Код

Создайте файл `app.py` и добавьте в него следующий код:

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    name = request.args.get('name', 'World')
    message = request.args.get('message', 'Hello')
    return f'{name}! {message}!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```

### Запуск

Запустите ваше приложение командой:

```bash
python app.py
```

## Результаты

При переходе по URL вида `http://xx.xx.xx.xx:8080/?name=Rekruto&message=Давай дружить` на странице отображается сообщение "Rekruto! Давай дружить!".

Здесь `xx.xx.xx.xx` — это IP-адрес вашего сервера.
