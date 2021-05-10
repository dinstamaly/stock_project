# STOCK HISTORY 

> REST сервис, который выполняет парсинг данных компаний с finance.yahoo.com
> и сохраняет в базу данных

 ## Требования для продакшен сервера (боевой сервер)
- PostgreSQL
- Python 3.6 и выше

## Переменные окружения 
> Переменные среды - это глобальные системные переменные, доступные для всех 
> процессов / пользователей, работающих под управлением операционной 
> системы (ОС), например Windows, macOS и Linux.

> Для примера в качестве операционной системы был выбран OS Linux.
> Необходмо перед запуском тестового сервера или продакшен сервера, 
> экспортировать переменные что внизу в таблице в окружение операционной системы

| Key              | Description                        | Default value  |
| :---             | :---                               | :---           |
| `DB_USER`        | postgres database user (not root)  | postgres       |
| `DB_PASS`        | postgres database password         | postgres       |
| `DB_NAME`        | postgres database name             | False          |
| `DB_HOST`        | postgres service host              | localhost      |
| `DB_PORT`        | postgres service port              | 5432 (default) |
| `DJANGO_ALLOWED_HOSTS`        | allowed host              | localhost  |

## Иструкция по подняю проекта локально
> 1. Необходимо склонить проект из локального репоризитория: 
> https://github.com/dinstamaly/stock_project.git
> 2. Пройти в директорию склоненного проекта:
``` bash
$ cd stock_project/
```

> 3. Создать виртуальное окружение и установить все с requirements.txt
> 4. Создать пользователя, базу данных (БД), кастомную схему в БД:
``` bash
$ psql postgres

psql (13.1)
Type "help" for help.

postgres=# CREATE USER stock_user WITH ENCRYPTED PASSWORD 'user_pass';
postgres=# GRANT ALL PRIVILEGES ON DATABASE stock_history_db TO youruser;
postgres=# CREATE SCHEMA core;
```
> После сделать команды для миграции:
``` bash
$ python manage.py migrate 
$ python manage.py makemigrations # Создает версию миграции в папке migrations
```
> После успешной миграции, можно запустить локальный сервер.
> протестить можно по этому url localhost:8000/api

# Документация по API
## Компании
>ticker - `Список компаний(get-method)`
> <details><summary>Show more</summary>
> 
> input:
> 
> {}
> 
> output:
> 
>  {
>    "id": 1,
>    "title": "PD"
>  },
>  {
>    "id": 2,
>    "title": "ZUO"
>  },
>  {
>    "id": 3,
>    "title": "PINS"
>  },
>  {
>    "id": 4,
>    "title": "ZM"
>  },
>  {
>    "id": 6,
>    "title": "DOCU"
>  },
>  {
>    "id": 7,
>    "title": "RUN"
>  },
>  {
>    "id": 8,
>    "title": "PVTL"
>  }
> 
> </details>
> 

> ticker - `Создание компания(post-method)`
> <details><summary>Show more</summary>
>
> input:
>   
> {
>   title: PD
> }
> 
> output:
> 
> {
>    "id": 1,
>    "title": "PD"
>  }
> 
> </details>

## History

> history - `Список всех историй(get-method)`
> <details><summary>Show more</summary>
>
> input:
>   
> {
> }
> 
> output:
> 
> 
> {
>    "id": 1,
>    "ticker": {
>      "id": 1,
>      "title": "PD"
>    },
>    "datetime": "2019-04-11T00:00:00",
>    "high": 39.610001,
    "low": 36,
    "close": 38.25,
    "adj_close": 38.25,
    "volume": 38.25
  },
  {
    "id": 2,
    "ticker": {
      "id": 1,
      "title": "PD"
    },
    "datetime": "2019-04-12T00:00:00",
    "high": 40.880001,
    "low": 37.398998,
    "close": 39.5,
    "adj_close": 39.5,
    "volume": 39.5
>  },
> ..........
> {
>    "id": 4546,
>    "ticker": {
>      "id": 7,
>      "title": "RUN"
>    },
>    {
>    "datetime": "2021-05-07T00:00:00",
>    "high": 49.919998,
>    "low": 45.130001,
>    "close": 45.639999,
>    "adj_close": 45.639999,
>    "volume": 45.639999
>  }
> </details>

> ticker/1/get_history/ - `Парсинг данных - создание и получение данных
> для компании(на примере для компании с id = 1)(post-method)`
> <details><summary>Show more</summary>
>
> input: 
> {
> }
> 
> output:
> [
> "created";
>  {
>    "id": 1,
>    "ticker": {
>      "id": 1,
>      "title": "PD"
>    },
>    "datetime": "2019-04-11T00:00:00",
>    "high": 39.610001,
>    "low": 36,
>    "close": 38.25,
>    "adj_close": 38.25,
>    "volume": 38.25
>  },..........
> > </details>
