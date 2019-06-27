# nekidaem-blog

### Test assignment for nekidaem.ru
Реализовать бэкенд с минимальным фронтендом (можно на голом HTML):

1. Имеется база стандартных пользователей Django (добавляются через админку, 
регистрацию делать не надо).

2. У каждого пользователя есть персональный блог. Новые создавать он не может.

3. Пост в блоге — элементарная запись с заголовком, текстом и временем 
создания.

4. Пользователь может подписываться (отписываться) на блоги других 
пользователей (любое количество).
5. У пользователя есть персональная лента новостей, в которой в обратном 
хронологическом порядке выводятся посты из блогов, на которые он подписан.

6. Пользователь может помечать посты в ленте прочитанными.

7. При добавлении/удалении подписки содержание ленты меняется (при удалении 
подписки пометки о "прочитанности" сохранять не нужно).

8. При добавлении поста в ленту — подписчики получают почтовое уведомление со 
ссылкой на новый пост.

9. Изменение содержания лент подписчиков (и рассылка уведомлений) должно 
происходить как при стандартной публикации поста пользователем через интерфейс сайта, так при добавлении/удалении поста через админку.

Техника:
Python 3.x, Django > 1.11.х, Postgresql или SQLite. 
Проект должен быть на гитхабе и отражать процесс разработки.
Код максимально приближенный к боевому (насколько получится).
Реализовать на Class-based views.

Проект желательно упаковать в докер. Запускать через docker-compose.

Срок выполнения 1-2 дня.

Результат выложить на github или bitbucket и прислать ссылку на info@nekidaem.ru.



### Configuration Backend

Environment variables

```.sh
$ cd docker/django
$ nano .env.local # See to table environment variables
```

### Environment variables backend

| Key    | Description   |    Default value  |
| :---         |     :---      |          :--- |
| `DJANGO_SECRET_KEY`  | mysecretkey  | secret-key              |
| `DJANGO_DEBUG`  | Debug mode True or False  | True              |
| `DEFAULT_DATABASE_URL`  | postgres://user:password@host:port/database_name | postgres://postgres:postgres@db:5432/starnavi |
| `POSTGRES_USER`  | Postgres username |   postgres   |
| `POSTGRES_PASSWORD`  | Postgres password |  postgres    |
| `POSTGRES_DB`  | Postgres database name | postgres |
| `PGDATA`  | Postgres volume | /var/lib/postgresql/data |
| `REDIS_HOST`  | Redis host | redis |
| `REDIS_PORT`  | Redis port | 6379 |
| `REDIS_DB`  | Redis database | 0 |


### Run local project 

```.bash
$ docker-compose -f dev.yml up
```
